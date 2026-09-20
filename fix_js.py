import re

with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace the broken openTimelineMain entirely
new_func = """function openTimelineMain(sectionId) {
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

js = re.sub(r'function openTimelineMain\(sectionId\) \{.*?\}\n\}\n', new_func, js, flags=re.DOTALL)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)
