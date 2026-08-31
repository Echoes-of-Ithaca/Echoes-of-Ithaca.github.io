document.addEventListener('DOMContentLoaded', () => {
    // Inject Team Members (only on team.html)
    const teamGrid = document.getElementById('team-grid-container');
    
    if (teamGrid) {
        const teamMembers = [
            { name: "Nombre Apellido", role: "Director Creativo", bio: "Apasionado por la narrativa emergente y los mitos clásicos. Liderando la visión del estudio.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role: "Productor", bio: "Organizando el caos creativo para que el barco llegue a Ítaca.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role: "Lead Programmer", bio: "Arquitecto de los sistemas detrás de la magia de los dioses.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role: "Game Designer", bio: "Creando mecánicas que desafíen la mente y los reflejos.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role: "Lead Artist", bio: "Dando color pastel a los paisajes de la antigua Grecia.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role: "3D Generalist", bio: "Esculpiendo monstruos marinos y templos olvidados.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role: "Animator", bio: "Dando vida y movimiento a la furia de los dioses.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role: "UI/UX Designer", bio: "Asegurando que la interfaz sea tan bella como funcional.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role: "Audio Director", bio: "Creando el paisaje sonoro que acompaña a Odiseo.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role: "Composer", bio: "Escribiendo las notas que resonarán en el corazón del jugador.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role: "Writer", bio: "Forjando diálogos épicos dignos de Homero.", linkedin: "#", portfolio: "#" },
            { name: "Nombre Apellido", role: "QA Tester", bio: "Buscando los bugs que intentan hundir nuestro barco.", linkedin: "#", portfolio: "#" }
        ];
        
        teamMembers.forEach(member => {
            const memberDiv = document.createElement('div');
            memberDiv.className = 'team-card';
            memberDiv.innerHTML = `
                <img src="assets/avatar_placeholder.jpg" alt="${member.name}" class="team-avatar">
                <h3 style="font-family: var(--font-heading); color: var(--color-text); font-size: 1.3rem;">${member.name}</h3>
                <p style="color: var(--color-accent); font-weight: 600; font-size: 0.9rem; margin-bottom: 0.5rem;">${member.role}</p>
                <p style="font-size: 0.95rem; color: var(--color-text-light); line-height: 1.4;">${member.bio}</p>
                <div class="team-links">
                    <a href="${member.portfolio}" target="_blank">Portfolio</a>
                    <span>|</span>
                    <a href="${member.linkedin}" target="_blank">LinkedIn</a>
                </div>
            `;
            teamGrid.appendChild(memberDiv);
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if(target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});
