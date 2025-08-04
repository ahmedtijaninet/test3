const animatedScrollObserver = new IntersectionObserver(
    (entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    },
    { threshold: 0.1 }
);

export default {
    mounted(el) {
        el.classList.add('fade-in-element');
        animatedScrollObserver.observe(el);
    }
}
