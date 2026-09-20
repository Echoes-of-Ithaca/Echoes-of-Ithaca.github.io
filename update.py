import re

with open('script.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

new_team_members = '''        const teamMembers = [
            { 
                name: "Andrea Doña", 
                role_es: "Game Director / Producer", role_en: "Game Director / Producer", 
                bio_es: "¡Hola! Soy la Producer y Directora de este proyecto, encargada de que el equipo mantenga el rumbo y de que la visión del juego cobre vida. Soy Junior Level Designer en el ámbito de juego móvil y Junior Game Producer. Mi trabajo aquí es que la visión del juego se cumpla y que el equipo tenga todo lo necesario para trabajar a gusto. Al final, lo que más me mueve es coordinar a la gente y ver cómo una idea acaba jugándose en pantalla.", 
                bio_en: "Hi! I am the Producer and Director of this project, in charge of keeping the team on track and bringing the vision of the game to life. I am a Junior Level Designer in mobile games and a Junior Game Producer. My job here is to ensure the vision of the game is fulfilled and that the team has everything they need to work comfortably. Ultimately, what drives me most is coordinating people and seeing how an idea ends up playable on screen.", 
                linkedin: "https://www.linkedin.com/in/andrea-dr/", 
                portfolio: "https://andreadr96.github.io/",
                linktree: "https://linktr.ee/andy.d"
            },
            { 
                name: "Pablo Longaron", 
                role_es: "Marketing / Lead Artist", role_en: "Marketing / Lead Artist", 
                bio_es: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
                bio_en: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
                linkedin: "#", portfolio: "#" 
            },
            { 
                name: "Marc Avante", 
                role_es: "Lead Programmer", role_en: "Lead Programmer", 
                bio_es: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
                bio_en: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
                linkedin: "#", portfolio: "#" 
            },
            { 
                name: "Carlos Suárez", 
                role_es: "Diseñador", role_en: "Designer", 
                bio_es: "Trabajo entre el diseño de niveles, de sistemas y la implementación, buscando que las ideas sean claras, jugables y fáciles de iterar.", 
                bio_en: "I work between level design, system design, and implementation, aiming to make ideas clear, playable, and easy to iterate.", 
                linkedin: "https://www.linkedin.com/in/carlos-suárez-ruiz-a88284340?utm_source=share_via&utm_content=profile&utm_medium=member_ios", 
                portfolio: "https://carlos-suarez-portfolio.netlify.app/" 
            },
            { 
                name: "Neus Gutiérrez", 
                role_es: "Concept Artist", role_en: "Concept Artist", 
                bio_es: "¡Ornitorrinco creativo! Estudió ilustración y animación, trabajó como diseñadora gráfica y se ha especializado en Concept Art. ¡La artista todoterreno del equipo!<br><br>Le gusta la naturaleza, leer, jugar, frikear siempre que se pueda y el cine con palomitas dulces.<br><br>Videojuegos favoritos: Hollow Knight, The Last of Us, Zelda Breath of the Wild, GoW, Silent Hill, WoW.", 
                bio_en: "Creative platypus! Studied illustration and animation, worked as a graphic designer, and specialized in Concept Art. The all-terrain artist of the team!<br><br>She loves nature, reading, playing, geeking out whenever possible, and movies with sweet popcorn.<br><br>Favorite video games: Hollow Knight, The Last of Us, Zelda Breath of the Wild, GoW, Silent Hill, WoW.", 
                linkedin: "#", portfolio: "#" 
            },
            { 
                name: "Pau Almendrote", 
                role_es: "Artista 3D Environment", role_en: "3D Environment Artist", 
                bio_es: "Hey! Soy Pau Almendrote Matamoros, un artista 3D centrado en environments y assets. Me gradué en la carrera que ofrece la UPC de Terrassa sobre Arte Digital, Animación y Diseño. En un principio quise ser desarrollador de videojuegos pero mediante iba avanzando el curso me di cuenta que lo mio debía ser definitivamente artista 3D. Todo este mundo me atrajo sobremanera al ver los primeros renders que salían de mi ordenador gracias a tutoriales y clases en la propia universidad y poco a poco fui desarrollando una serie de proyectos cada vez mas complejos y sin ayuda a modo de reto hasta que en un punto de mi vida me convertí en lo que hacía unos pocos años antes admiraba!", 
                bio_en: "Hey! I am Pau Almendrote Matamoros, a 3D artist focused on environments and assets. I graduated from the UPC in Terrassa in Digital Art, Animation, and Design. At first I wanted to be a game developer, but as the course progressed I realized that being a 3D artist was definitely my thing. This whole world attracted me immensely when I saw the first renders coming out of my computer thanks to tutorials and university classes, and little by little I developed a series of increasingly complex projects without help as a challenge until at one point in my life I became what I admired just a few years before!", 
                linkedin: "#", portfolio: "#" 
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
            
            let linksHTML = "";
            if(member.portfolio && member.portfolio !== "#") linksHTML += \<a href="\" target="_blank" class="btn-link">Portfolio</a>\;
            if(member.linkedin && member.linkedin !== "#") linksHTML += \<a href="\" target="_blank" class="btn-link">LinkedIn</a>\;
            if(member.linktree && member.linktree !== "#") linksHTML += \<a href="\" target="_blank" class="btn-link">Linktree</a>\;
            
            // Add placeholder buttons if none exist (for those missing links)
            if(linksHTML === "") {
                linksHTML = \<a href="#" class="btn-link">Portfolio</a><a href="#" class="btn-link">LinkedIn</a>\;
            }

            memberDiv.innerHTML = \
                <img src="assets/avatar_placeholder.jpg" alt="\" class="team-avatar">
                <div class="team-info">
                    <h3 style="font-family: var(--font-heading); color: var(--color-text); font-size: 1.5rem; margin-bottom: 0.2rem;">\</h3>
                    <p style="color: var(--color-accent); font-weight: 600; font-size: 1rem; margin-bottom: 0.8rem;" data-es="\" data-en="\">\</p>
                    <p style="font-size: 1rem; color: var(--color-text-light); line-height: 1.5;" data-es="\" data-en="\">\</p>
                    <div class="team-links">
                        \
                    </div>
                </div>
            \;'''

# Using regex to replace the old block
pattern = re.compile(r'        const teamMembers = \[.*?</div>\n            ;', re.DOTALL)
content = pattern.sub(new_team_members, content)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)
