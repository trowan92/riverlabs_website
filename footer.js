// Footer component
document.addEventListener('DOMContentLoaded', function() {
    const footerHTML = `
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Riverlabs</h4>
                    <p>Environmental monitoring solutions from Imperial College London research</p>
                </div>
                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="sensors.html">Sensors</a></li>
                        <li><a href="science.html">Science</a></li>
                        <li><a href="consultancy.html">Consultancy</a></li>
                        <li><a href="about.html">About</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Connect</h4>
                    <ul>
                        <li><a href="#">Contact</a></li>
                        <li><a href="#">GitHub</a></li>
                        <li><a href="#">LinkedIn</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Riverlabs Ltd. All rights reserved.</p>
            </div>
        </div>
    </footer>
    `;
    
    // Insert footer at the end of body
    document.body.insertAdjacentHTML('beforeend', footerHTML);
});
