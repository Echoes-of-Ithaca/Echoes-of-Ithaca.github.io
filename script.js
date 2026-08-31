// Language translation logic
function setLanguage(lang) {
    // Replace text in all elements with data-es / data-en
    document.querySelectorAll('[data-es]').forEach(el => {
        if(el.getAttribute('data-' + lang)) {
            el.innerHTML = el.getAttribute('data-' + lang);
        }
    });

    // Update active state on toggle buttons safely
    const btnEs = document.getElementById('btn-es');
    const btnEn = document.getElementById('btn-en');
    
    if (btnEs && btnEn) {
        btnEs.classList.remove('active');
        btnEn.classList.remove('active');
        const activeBtn = document.getElementById('btn-' + lang);
        if(activeBtn) activeBtn.classList.add('active');
    }

    // Save preference
    localStorage.setItem('lang', lang);
}

// Slider Logic for index.html
function slideLeft() {
    const track = document.getElementById('slider-track');
    if (track) {
        track.scrollBy({ left: -320, behavior: 'smooth' });
    }
}

function slideRight() {
    const track = document.getElementById('slider-track');
    if (track) {
        track.scrollBy({ left: 320, behavior: 'smooth' });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Inject Team Members (only on team.html)
    const teamGrid = document.getElementById('team-grid-container');
    
    if (teamGrid) {
        const teamMembers = [
            { name: "Nombre Apellido", role_es: "Director Creativo", role_en: "Creative Director", bio_es: "Apasionado por la narrativa emergente y los mitos clásicos.", bio_en: "Passionate about emergent narrative and classic myths.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role_es: "Productor", role_en: "Producer", bio_es: "Organizando el caos creativo.", bio_en: "Organizing the creative chaos.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role_es: "Lead Programmer", role_en: "Lead Programmer", bio_es: "Arquitecto de los sistemas detrás de la magia.", bio_en: "Architect of the systems behind the magic.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role_es: "Game Designer", role_en: "Game Designer", bio_es: "Creando mecánicas que desafíen la mente.", bio_en: "Creating mechanics that challenge the mind.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role_es: "Lead Artist", role_en: "Lead Artist", bio_es: "Dando color pastel a los paisajes.", bio_en: "Giving pastel colors to the landscapes.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role_es: "3D Generalist", role_en: "3D Generalist", bio_es: "Esculpiendo monstruos marinos.", bio_en: "Sculpting sea monsters.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role_es: "Animator", role_en: "Animator", bio_es: "Dando vida a la furia de los dioses.", bio_en: "Bringing the gods' fury to life.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role_es: "UI/UX Designer", role_en: "UI/UX Designer", bio_es: "Haciendo la interfaz funcional y bella.", bio_en: "Making the interface functional and beautiful.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role_es: "Audio Director", role_en: "Audio Director", bio_es: "Creando el paisaje sonoro de Odiseo.", bio_en: "Creating Odysseus' soundscape.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role_es: "Composer", role_en: "Composer", bio_es: "Escribiendo notas para el corazón.", bio_en: "Writing notes for the heart.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role_es: "Writer", role_en: "Writer", bio_es: "Forjando diálogos épicos.", bio_en: "Forging epic dialogues.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role_es: "QA Tester", role_en: "QA Tester", bio_es: "Buscando los bugs del barco.", bio_en: "Hunting the ship's bugs.", linkedin: "#", portfolio: "#" }
        ];
        
        teamMembers.forEach(member => {
            const memberDiv = document.createElement('div');
            memberDiv.className = 'team-card';
            memberDiv.innerHTML = `
                <img src="assets/avatar_placeholder.jpg" alt="${member.name}" class="team-avatar">
                <h3 style="font-family: var(--font-heading); color: var(--color-text); font-size: 1.3rem;">${member.name}</h3>
                <p style="color: var(--color-accent); font-weight: 600; font-size: 0.9rem; margin-bottom: 0.5rem;" data-es="${member.role_es}" data-en="${member.role_en}">${member.role_es}</p>
                <p style="font-size: 0.95rem; color: var(--color-text-light); line-height: 1.4;" data-es="${member.bio_es}" data-en="${member.bio_en}">${member.bio_es}</p>
                <div class="team-links">
                    <a href="${member.portfolio}" target="_blank">Portfolio</a>
                    <span>|</span>
                    <a href="${member.linkedin}" target="_blank">LinkedIn</a>
                </div>
            `;
            teamGrid.appendChild(memberDiv);
        });
    }

    // Initialize language on load for all pages
    const savedLang = localStorage.getItem('lang') || 'es';
    setLanguage(savedLang);
});
