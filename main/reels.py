"""Client work reels (9:16 videos) shown across the site.

These are the reels from the previous Trend Crafters site (github.com/Unisha0/trendcrafters),
hosted on UploadThing. To add or reorder reels, edit this list; every reel carousel and the
Work page read from it.
"""

_HOST = "https://qqazonq8eu.ufs.sh/f/"

REELS = [
    {"client": "Changan Nepal", "category": "Brand Film", "tag": "Luxury & Innovation",
     "blurb": "Sleek storytelling capturing premium cars and refined design.",
     "src": _HOST + "y5kFsPOhkGJ6HRbCTzNvGdX03ip8MAQBcZ4wlVmRq5aPoxub", "kind": "brand"},
    {"client": "Threads & Trends", "category": "Lifestyle Visuals", "tag": "Modern Fashion",
     "blurb": "Bold visuals redefining trendy footwear with motion and contemporary aesthetics.",
     "src": _HOST + "y5kFsPOhkGJ6489y4U1rTardS8zBRVWmHfJYchFPovxg9X0G", "kind": "social"},
    {"client": "PIEC", "category": "Brand Campaign", "tag": "Study Abroad Excellence",
     "blurb": "Empowering learners' international dreams with cinematic storytelling.",
     "src": _HOST + "y5kFsPOhkGJ6F3tYLxjfLXlSO27gtJBnqy9Dd8acQiuIW3YH", "kind": "ads"},
    {"client": "International Study Partners", "category": "Educational Branding", "tag": "Global Vision",
     "blurb": "Inspiring students through compelling visuals and global education stories.",
     "src": _HOST + "y5kFsPOhkGJ6DnMg7AIQgZr30ctV2ndkOsuFP4EBUNCSlaYH", "kind": "ads"},
    {"client": "Newmew", "category": "Brand Campaign", "tag": "Youth & Streetwear",
     "blurb": "Vibrant visuals celebrating youth, confidence and street style.",
     "src": _HOST + "y5kFsPOhkGJ6y5DuE5OhkGJ6pd7VSWlaOxzjirYQPLeBvmt9", "kind": "social"},
    {"client": "Himalayan Java", "category": "Brand Storytelling", "tag": "Cafe Culture",
     "blurb": "Warm visuals reflecting the aroma, ambience and creative spirit of Java.",
     "src": _HOST + "y5kFsPOhkGJ6EIXaMBWSRyJMXNj5nQbvwBsVqAKx4392k8H6", "kind": "social"},
    {"client": "Threads & Trends", "category": "Product Reel", "tag": "Everyday Comfort",
     "blurb": "Step into style: premium feel, trendy looks, everyday comfort, for every budget.",
     "src": _HOST + "y5kFsPOhkGJ6mWOvjkoaM4wlpbq3GPYL0HAScux7thnreCiz", "kind": "ads"},
]


def _pick(client, category):
    return next(r for r in REELS if r["client"] == client and r["category"] == category)


# Home and Work pages only: own-hosted reels mixed with a few of the reels above.
# Other pages (Digital Marketing, Branding, etc.) keep using REELS unchanged.
# "static"/"poster" are paths under static/main/; videos are synced by deploy/release.sh.
HOME_REELS = [
    {"client": "Vermi Perfume", "category": "Brand Film", "tag": "Luxury Fragrance",
     "blurb": "Moody close-ups and warm light that make the fragrance feel premium.",
     "static": "main/videos/reel-brand-film.mp4", "poster": "main/images/home/reel-brand-film-poster.jpg", "kind": "brand"},
    _pick("Changan Nepal", "Brand Film"),
    {"client": "Ford", "category": "Automotive Lifestyle", "tag": "Modern Driving",
     "blurb": "Bold visuals redefining adventure and style with motion and cutting-edge design.",
     "static": "main/videos/reel-ford.mp4", "poster": "main/images/home/reel-ford-poster.jpg", "kind": "brand"},
    {"client": "Wildfire by Mount Everest Distillery", "category": "Product Film", "tag": "Spirits & Beverages",
     "blurb": "A cinematic unboxing that shows off the bottle, the label and the brand.",
     "static": "main/videos/reel-wildfire.mp4", "poster": "main/images/home/reel-wildfire-poster.jpg", "kind": "ads"},
    _pick("Threads & Trends", "Product Reel"),
    _pick("Himalayan Java", "Brand Storytelling"),
    {"client": "CNC Metal & Wood Craft", "category": "Process Reel", "tag": "Precision Manufacturing",
     "blurb": "Machines, sparks and craftsmanship, filmed to show the skill behind every piece.",
     "static": "main/videos/reel-cnc.mp4", "poster": "main/images/home/reel-cnc-poster.jpg", "kind": "brand"},
]


# Work page: every finished video we have. "group" drives the filter chips on /work/
# (brand | product | social | bts); "poster" paths are under static/main/.
def _hosted(client, category, group, poster):
    return {**_pick(client, category), "group": group, "poster": "main/images/work/" + poster}


WORK_REELS = [
    {**HOME_REELS[0], "group": "brand"},  # Vermi Perfume
    _hosted("Changan Nepal", "Brand Film", "brand", "poster-changan-nepal-brand-film.jpg"),
    {**HOME_REELS[2], "group": "brand"},  # Ford
    {"client": "Whiteline Pickup", "category": "Automotive Film", "tag": "Off-road & Adventure",
     "blurb": "Forest roads, low angles and a glowing grille: a pickup filmed like a hero.",
     "static": "main/videos/reel-whiteline.mp4", "poster": "main/images/work/reel-whiteline-poster.jpg", "group": "brand"},
    {"client": "MediQuest Diagnostic", "category": "Brand Storytelling", "tag": "Healthcare",
     "blurb": "A personal story about family health, told in Nepali with warmth and trust.",
     "static": "main/videos/reel-mediquest.mp4", "poster": "main/images/work/reel-mediquest-poster.jpg", "group": "social"},
    {**HOME_REELS[3], "group": "product"},  # Wildfire
    {"client": "Blue Spot by Mount Everest Distillery", "category": "Product Film", "tag": "Spirits & Cocktails",
     "blurb": "Ice, lime and a slow pour: a cocktail film that sells the drink in seconds.",
     "static": "main/videos/reel-blue-spot.mp4", "poster": "main/images/work/reel-blue-spot-poster.jpg", "group": "product"},
    _hosted("Himalayan Java", "Brand Storytelling", "social", "poster-himalayan-java-brand-storytelling.jpg"),
    _hosted("Threads & Trends", "Product Reel", "product", "poster-threads-trends-product-reel.jpg"),
    {**HOME_REELS[6], "group": "product"},  # CNC
    _hosted("PIEC", "Brand Campaign", "social", "poster-piec-brand-campaign.jpg"),
    _hosted("Threads & Trends", "Lifestyle Visuals", "social", "poster-threads-trends-lifestyle-visuals.jpg"),
    _hosted("International Study Partners", "Educational Branding", "social", "poster-international-study-partners-educational-branding.jpg"),
    _hosted("Newmew", "Brand Campaign", "social", "poster-newmew-brand-campaign.jpg"),
    {"client": "Mingma David Sherpa", "category": "Behind the Scenes", "tag": "Studio Interview",
     "blurb": "Lights, camera and crew on the set of the Mingma David Sherpa film.",
     "static": "main/videos/reel-bts-studio.mp4", "poster": "main/images/work/reel-bts-studio-poster.jpg", "group": "bts"},
    {"client": "Trend Crafters", "category": "Behind the Scenes", "tag": "Our Crew",
     "blurb": "A day on set with our team, from setup to the final take.",
     "static": "main/videos/team-behind-the-scenes.mp4", "poster": "main/images/home/bts-video-poster.jpg", "group": "bts"},
]

# Landscape films shown large at the top of /work/.
WORK_FILMS = [
    {"client": "Mingma David Sherpa", "category": "Brand Film", "tag": "Legendary Mountaineer",
     "blurb": "Fourteen 8,000 metre peaks, one name written above the clouds.",
     "static": "main/videos/story-mingma-david-sherpa.mp4", "poster": "main/images/br/mingma-poster.jpg"},
    {"client": "Sasurali Restaurant", "category": "Venue Film", "tag": "Hospitality",
     "blurb": "Drone and ground footage that shows the view, the space and the food.",
     "static": "main/videos/film-sasurali.mp4", "poster": "main/images/work/film-sasurali-poster.jpg"},
]
