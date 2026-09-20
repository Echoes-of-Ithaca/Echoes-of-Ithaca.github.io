// Language translation logic
function setLanguage(lang) {
    document.querySelectorAll('[data-es]').forEach(el => {
        if(el.getAttribute('data-' + lang)) {
            el.innerHTML = el.getAttribute('data-' + lang);
        }
    });

    const btnEs = document.getElementById('btn-es');
    const btnEn = document.getElementById('btn-en');
    
    if (btnEs && btnEn) {
        btnEs.classList.remove('active');
        btnEn.classList.remove('active');
        const activeBtn = document.getElementById('btn-' + lang);
        if(activeBtn) activeBtn.classList.add('active');
    }
    localStorage.setItem('lang', lang);
}

function slideLeft() {
    const track = document.getElementById('slider-track');
    if (!track || track.isAnimating) return;
    track.isAnimating = true;
    const lastItem = track.lastElementChild;
    track.insertBefore(lastItem, track.firstElementChild);
    track.style.transition = 'none';
    track.style.transform = 'translateX(-332px)';
    void track.offsetWidth;
    track.style.transition = 'transform 0.4s ease';
    track.style.transform = 'translateX(0)';
    setTimeout(() => { track.isAnimating = false; }, 400);
}

function slideRight() {
    const track = document.getElementById('slider-track');
    if (!track || track.isAnimating) return;
    track.isAnimating = true;
    track.style.transition = 'transform 0.4s ease';
    track.style.transform = 'translateX(-332px)';
    setTimeout(() => {
        const firstItem = track.firstElementChild;
        track.appendChild(firstItem);
        track.style.transition = 'none';
        track.style.transform = 'translateX(0)';
        track.isAnimating = false;
    }, 400);
}

document.addEventListener('DOMContentLoaded', () => {
    const teamGrid = document.getElementById('team-grid-container');
    
    if (teamGrid) {
        const teamMembers = [
            { 
                name: "Andrea Doña", image: "assets/Nemea_References/Equipo/Andrea.png",
                role_es: "Game Director / Producer", role_en: "Game Director / Producer", 
                bio_es: "¡Hola! Soy la Producer y Directora de este proyecto, encargada de que el equipo mantenga el rumbo y de que la visión del juego cobre vida. Soy Junior Level Designer en el ámbito de juego móvil y Junior Game Producer. Mi trabajo aquí es que la visión del juego se cumpla y que el equipo tenga todo lo necesario para trabajar a gusto. Al final, lo que más me mueve es coordinar a la gente y ver cómo una idea acaba jugándose en pantalla.", 
                bio_en: "Hi! I am the Producer and Director of this project, in charge of keeping the team on track and bringing the vision of the game to life. I am a Junior Level Designer in mobile games and a Junior Game Producer. My job here is to ensure the vision of the game is fulfilled and that the team has everything they need to work comfortably. Ultimately, what drives me most is coordinating people and seeing how an idea ends up playable on screen.", 
                linkedin: "https://www.linkedin.com/in/andrea-dr/", 
                portfolio: "https://andreadr96.github.io/",
                linktree: "https://linktr.ee/andy.d"
            },
            { 
                name: "Pablo Longaron", image: "assets/Nemea_References/Equipo/Pablo.jpg",
                role_es: "Marketing / Lead Artist", role_en: "Marketing / Lead Artist", 
                bio_es: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
                bio_en: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
                linkedin: "#", portfolio: "#" 
            },
            { 
                name: "Marc Avante", image: "assets/Nemea_References/Equipo/Marc.jpg",
                role_es: "Lead Programmer", role_en: "Lead Programmer", 
                bio_es: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
                bio_en: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
                linkedin: "#", portfolio: "#" 
            },
            { 
                name: "Carlos Suárez", image: "assets/Nemea_References/Equipo/Carlos.jpg",
                role_es: "Diseñador", role_en: "Designer", 
                bio_es: "Trabajo entre el diseño de niveles, de sistemas y la implementación, buscando que las ideas sean claras, jugables y fáciles de iterar.", 
                bio_en: "I work between level design, system design, and implementation, aiming to make ideas clear, playable, and easy to iterate.", 
                linkedin: "https://www.linkedin.com/in/carlos-suárez-ruiz-a88284340?utm_source=share_via&utm_content=profile&utm_medium=member_ios", 
                portfolio: "https://carlos-suarez-portfolio.netlify.app/" 
            },
            { 
                name: "Neus Gutiérrez", image: "assets/Nemea_References/Equipo/Neus.jpg",
                role_es: "Concept Artist", role_en: "Concept Artist", 
                bio_es: "¡Ornitorrinco creativo! Estudió ilustración y animación, trabajó como diseñadora gráfica y se ha especializado en Concept Art. ¡La artista todoterreno del equipo!<br><br>Le gusta la naturaleza, leer, jugar, frikear siempre que se pueda y el cine con palomitas dulces.<br><br>Videojuegos favoritos: Hollow Knight, The Last of Us, Zelda Breath of the Wild, GoW, Silent Hill, WoW.", 
                bio_en: "Creative platypus! Studied illustration and animation, worked as a graphic designer, and specialized in Concept Art. The all-terrain artist of the team!<br><br>She loves nature, reading, playing, geeking out whenever possible, and movies with sweet popcorn.<br><br>Favorite video games: Hollow Knight, The Last of Us, Zelda Breath of the Wild, GoW, Silent Hill, WoW.", 
                linkedin: "#", portfolio: "#" 
            },
            { 
                name: "Pau Almendrote", image: "assets/Nemea_References/Equipo/Pau.png",
                role_es: "Artista 3D Environment", role_en: "3D Environment Artist", 
                bio_es: "Hey! Soy Pau Almendrote Matamoros, un artista 3D centrado en environments y assets. Me gradué en la carrera que ofrece la UPC de Terrassa sobre Arte Digital, Animación y Diseño. En un principio quise ser desarrollador de videojuegos pero mediante iba avanzando el curso me di cuenta que lo mio debía ser definitivamente artista 3D. Todo este mundo me atrajo sobremanera al ver los primeros renders que salían de mi ordenador gracias a tutoriales y clases en la propia universidad y poco a poco fui desarrollando una serie de proyectos cada vez mas complejos y sin ayuda a modo de reto hasta que en un punto de mi vida me convertí en lo que hacía unos pocos años antes admiraba!", 
                bio_en: "Hey! I am Pau Almendrote Matamoros, a 3D artist focused on environments and assets. I graduated from the UPC in Terrassa in Digital Art, Animation, and Design. At first I wanted to be a game developer, but as the course progressed I realized that being a 3D artist was definitely my thing. This whole world attracted me immensely when I saw the first renders coming out of my computer thanks to tutorials and university classes, and little by little I developed a series of increasingly complex projects without help as a challenge until at one point in my life I became what I admired just a few years before!", 
                linkedin: "https://www.linkedin.com/in/pau-almendrote-matamoros/", 
                sketchfab: "https://sketchfab.com/pau_alma_3d",
                instagram: "https://www.instagram.com/pau_alma_3d",
                artstation: "https://pau_alma.artstation.com/"
            },
            { 
                name: "Mario Casseny", 
                role_es: "Artista 3D Characters", role_en: "3D Character Artist", 
                bio_es: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
                bio_en: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
                linkedin: "#", portfolio: "#" 
            }
        ];
        
        teamMembers.forEach(member => {
            const memberDiv = document.createElement('div');
            memberDiv.className = 'team-card';
            let linksHTML = '';
            if(member.portfolio && member.portfolio !== '#') linksHTML += `<a href="${member.portfolio}" target="_blank" class="btn-link">Portfolio</a>`;
            if(member.linkedin && member.linkedin !== '#') linksHTML += `<a href="${member.linkedin}" target="_blank" class="btn-link">LinkedIn</a>`;
            if(member.linktree && member.linktree !== '#') linksHTML += `<a href="${member.linktree}" target="_blank" class="btn-link">Linktree</a>`;
            if(member.artstation && member.artstation !== '#') linksHTML += `<a href="${member.artstation}" target="_blank" class="btn-link">ArtStation</a>`;
            if(member.sketchfab && member.sketchfab !== '#') linksHTML += `<a href="${member.sketchfab}" target="_blank" class="btn-link">Sketchfab</a>`;
            if(member.instagram && member.instagram !== '#') linksHTML += `<a href="${member.instagram}" target="_blank" class="btn-link">Instagram</a>`;
            
            if(linksHTML === '') {
                linksHTML = `<a href="#" class="btn-link">Portfolio</a><a href="#" class="btn-link">LinkedIn</a>`;
            }

            const imgSrc = member.image ? member.image : 'assets/avatar_placeholder.jpg';

            memberDiv.innerHTML = `
                <img src="${imgSrc}" alt="${member.name}" class="team-avatar">
                <div class="team-info">
                    <h3 style="font-family: var(--font-heading); color: var(--color-text); font-size: 1.7rem; margin-bottom: 0.2rem;">${member.name}</h3>
                    <p style="color: var(--color-accent); font-weight: 600; font-size: 1.1rem; margin-bottom: 0.8rem;" data-es="${member.role_es}" data-en="${member.role_en}">${member.role_es}</p>
                    <p style="font-size: 1.05rem; color: var(--color-text-light); line-height: 1.6;" data-es="${member.bio_es}" data-en="${member.bio_en}">${member.bio_es}</p>
                    <div class="team-links" style="flex-wrap: wrap;">
                        ${linksHTML}
                    </div>
                </div>
            `;
            teamGrid.appendChild(memberDiv);
        });
    }

    const savedLang = localStorage.getItem('lang') || 'es';
    setLanguage(savedLang);
});

function switchTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(el => {
        el.style.display = 'none';
    });
    document.querySelectorAll('.tab-btn').forEach(el => {
        el.classList.remove('active');
    });
    
    const targetContent = document.getElementById('tab-' + tabId);
    if(targetContent) targetContent.style.display = 'block';
    
    const targetBtn = document.getElementById('btn-tab-' + tabId);
    if(targetBtn) targetBtn.classList.add('active');
}
