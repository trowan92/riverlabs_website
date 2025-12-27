// Navbar component
document.addEventListener('DOMContentLoaded', function() {
    const navbarHTML = `
    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo"> <img src="images/riverlabs-logo.svg" alt="Riverlabs" height="60"></a>
            <ul class="nav-menu">
                <li><a href="index.html">Home</a></li>
                <li class="dropdown">
                    <a href="sensors.html">Sensors</a>
                    <div class="dropdown-content">
                        <a href="sensors.html#lidar">LiDAR</a>
                        <a href="sensors.html#ultrasonic">Ultrasonic</a>
                        <a href="sensors.html#water-quality">Water Quality Buoy</a>
                    </div>
                </li>
                <li><a href="science.html">Science</a></li>
                <li><a href="consultancy.html">Consultancy</a></li>
                <li><a href="about.html">About</a></li>
            </ul>
        </div>
    </nav>
    `;
    
    // Insert navbar at the beginning of body
    document.body.insertAdjacentHTML('afterbegin', navbarHTML);
    
    // Set active state based on current page
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-menu a');
    
    navLinks.forEach(link => {
        const linkPage = link.getAttribute('href').split('#')[0];
        if (linkPage === currentPage || (currentPage === '' && linkPage === 'index.html')) {
            link.classList.add('active');
        }
    });
});
