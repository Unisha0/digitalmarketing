// Experience layer: scroll progress, back-to-top, number count-up, gentle hero parallax.
(function () {
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function ready(fn) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn); else fn(); }

    ready(function () {
        // Scroll progress bar + back to top
        var bar = document.createElement('div'); bar.id = 'scroll-progress'; bar.setAttribute('aria-hidden', 'true'); document.body.appendChild(bar);
        var top = document.createElement('button'); top.id = 'to-top'; top.type = 'button'; top.setAttribute('aria-label', 'Back to top'); top.innerHTML = '<i class="fas fa-arrow-up"></i>'; document.body.appendChild(top);
        top.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); });

        var ticking = false;
        var heroImgs = [];
        var hero = document.querySelector('main > section:first-child');
        if (false) heroImgs = Array.prototype.slice.call(hero.querySelectorAll('img.absolute.inset-0, .aspect-\\[4\\/5\\] img'));

        function onScroll() {
            var h = document.documentElement;
            var max = h.scrollHeight - h.clientHeight;
            var y = window.pageYOffset || h.scrollTop;
            bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, y / max) : 0) + ')';
            top.classList.toggle('show', y > 700);
            ticking = false;
        }
        window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
        onScroll();

        // Count-up for stat numbers like 50+, 45%, 5★
        var nums = [];
        document.querySelectorAll('.font-display').forEach(function (el) {
            var t = (el.firstChild && el.firstChild.nodeType === 3 ? el.firstChild.nodeValue : '').trim();
            if (/^\d{1,3}$/.test(t) && el.children.length <= 1 && (el.className.indexOf('gradient-text') > -1 || el.className.indexOf('text-3xl') > -1 || el.className.indexOf('text-5xl') > -1 || el.className.indexOf('text-6xl') > -1)) nums.push({ el: el, n: parseInt(t, 10), node: el.firstChild });
        });
        if (nums.length && 'IntersectionObserver' in window && !reduce) {
            var io = new IntersectionObserver(function (es) {
                es.forEach(function (e) {
                    if (!e.isIntersecting) return;
                    io.unobserve(e.target);
                    var item = nums.filter(function (x) { return x.el === e.target; })[0];
                    if (!item) return;
                    var start = null, dur = 1100;
                    function step(ts) {
                        if (!start) start = ts;
                        var p = Math.min(1, (ts - start) / dur), eased = 1 - Math.pow(1 - p, 3);
                        item.node.nodeValue = Math.round(item.n * eased);
                        if (p < 1) requestAnimationFrame(step);
                    }
                    item.node.nodeValue = '0'; item.el.classList.add('count-up'); requestAnimationFrame(step);
                });
            }, { threshold: 0.6 });
            nums.forEach(function (x) { io.observe(x.el); });
        }
    });
})();
