document.addEventListener('DOMContentLoaded', () => {
    // Inject Team Members
    const teamGrid = document.getElementById('team-grid');
    const roles = [
        "Director Creativo", "Productor", "Lead Programmer", "Game Designer",
        "Lead Artist", "3D Generalist", "Animator", "UI/UX Designer",
        "Audio Director", "Composer", "Writer", "QA Tester"
    ];
    
    // Generate 12 team members
    for (let i = 0; i < 12; i++) {
        const memberDiv = document.createElement('div');
        memberDiv.className = 'team-member';
        memberDiv.innerHTML = `
            <img src="assets/avatar_placeholder.jpg" alt="Miembro del equipo" class="team-avatar">
            <h3 class="team-name">Nemea Dev ${i + 1}</h3>
            <p class="team-role">${roles[i]}</p>
        `;
        teamGrid.appendChild(memberDiv);
    }

    // Scroll Animation Observer
    const fadeElements = document.querySelectorAll('.fade-in');

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    fadeElements.forEach(el => {
        observer.observe(el);
    });

    // Make the hero section visible immediately on load
    setTimeout(() => {
        const hero = document.querySelector('.hero-content');
        if (hero) hero.classList.add('visible');
    }, 100);
});
