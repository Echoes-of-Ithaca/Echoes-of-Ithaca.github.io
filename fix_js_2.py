with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

idx = js.find("// Timeline Main Sections Logic")
js = js[:idx] + """// Timeline Main Sections Logic
function openTimelineMain(sectionId) {
    // Hide all sections
    document.querySelectorAll('.timeline-section-content').forEach(el => {
        el.style.display = 'none';
    });
    // Remove active from main menu cards
    document.querySelectorAll('.main-menu-card').forEach(el => {
        el.classList.remove('active');
    });
    
    // Show selected section
    const targetSection = document.getElementById('section-' + sectionId);
    if(targetSection) targetSection.style.display = 'block';
    
    // Activate clicked menu
    const targetMenu = document.getElementById('menu-' + sectionId);
    if(targetMenu) targetMenu.classList.add('active');
}
"""

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)
