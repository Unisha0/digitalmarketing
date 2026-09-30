# Deploying Trend Crafters on AWS (EC2 + nginx + gunicorn)

Stack: Ubuntu 22.04/24.04 EC2 (t3.small or t3.micro is plenty) → nginx → gunicorn → Django.
Static files are served by nginx (and WhiteNoise as a fallback). There is no database to manage.

## 1. AWS setup (one time)
1. Launch an EC2 instance (Ubuntu, 20 GB gp3). Security group inbound: **22** (your IP only), **80**, **443**.
2. Allocate an **Elastic IP** and attach it to the instance.
3. DNS (Route 53 or your registrar): `A` records for `trendcrafters.global` and `www.trendcrafters.global` → the Elastic IP.

## 2. First deploy
```bash
ssh ubuntu@<elastic-ip>
git clone <your-repo-url> trendcrafters && cd trendcrafters
bash deploy/setup_ec2.sh          # installs everything, generates a SECRET_KEY, starts the app
nano .env                         # set EMAIL_HOST_PASSWORD (Gmail app password), then:
sudo systemctl restart gunicorn-trendcrafters
sudo certbot --nginx -d trendcrafters.global -d www.trendcrafters.global   # free HTTPS + auto-renew
```
Verify: `curl -I https://trendcrafters.global/health/` → `200`.

## 3. Every later deploy
```bash
cd ~/trendcrafters && bash deploy.sh
```
(pulls `main`, installs requirements, collects static files, runs `check --deploy`, reloads gunicorn, smoke-tests `/health/`.)

## Notes
- **Rotate the Gmail app password**: the old one is in git history. Create a new one and put it only in the server `.env`.
- `.env` is git-ignored. `DEBUG` must be `False` in production; the app refuses to start without `DJANGO_SECRET_KEY`.
- Videos are git-ignored except `main/static/main/videos/`. Any other `.mp4` must be copied to the server separately (e.g. `scp`).
- If you change Tailwind classes/templates: run `npm run build:css` locally and commit `tailwind-built.css` before deploying.
- Optional: put CloudFront in front for a global CDN; the `/health/` endpoint works as an ALB/target-group health check.

## After going live (SEO)
1. Google Search Console → add `https://trendcrafters.global` → submit `https://trendcrafters.global/sitemap.xml`.
2. Bing Webmaster Tools → import from Search Console.
3. Claim/verify the Google Business Profile with the same name, address and phone as the site's schema.
4. Test a page in the Rich Results Test and share a link on WhatsApp/Facebook to confirm the new 1200×630 preview image.

## SSH shortcut
`~/.ssh/config` has a `trendcraftersaws` host (13.49.74.241, user `ubuntu`, key `~/.ssh/trendcrafters-key.pem`):
```bash
ssh trendcraftersaws                                   # log in
ssh trendcraftersaws 'cd ~/trendcrafters && bash deploy.sh'   # deploy from your laptop
```
