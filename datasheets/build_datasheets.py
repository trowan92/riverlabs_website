#!/usr/bin/env python3
"""Build Riverlabs product datasheets (HTML -> PDF via headless Chrome),
matching the layout of the existing Ultrasonic_Sensor_Datasheet.pdf.

Usage:  python3 datasheets/build_datasheets.py   (requires Google Chrome)
Edit the LIDAR / BUOY dicts below to change content, then re-run."""
import base64, pathlib, subprocess, sys

SITE = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(__file__).parent
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

LOGO = b64(SITE / 'images/riverlabs-logo.svg', 'image/svg+xml')

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  width: 210mm; height: 297mm; padding: 12mm 16mm 12mm 16mm; overflow: hidden;
  font-family: "Segoe UI", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 8.6pt; line-height: 1.34; color: #333; position: relative;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
.header { display: flex; justify-content: space-between; align-items: flex-end;
  border-bottom: 1.6pt solid #00aab5; padding-bottom: 4mm; margin-bottom: 5mm; }
.header img { height: 13mm; }
.header .title { text-align: right; }
.header h1 { margin: 0; font-size: 16.5pt; font-weight: 700; color: #006880; letter-spacing: -0.01em; }
.header .sub { margin: 1.5mm 0 0; font-size: 8pt; color: #333; }
.tag { display: inline-block; font-size: 6.5pt; font-weight: 700; letter-spacing: .06em; text-transform: uppercase;
  color: #006880; border: 0.8pt solid #00aab5; border-radius: 2pt; padding: 0.4mm 1.6mm; margin-top: 1.5mm; }
.intro { display: flex; gap: 8mm; align-items: flex-start; }
.intro .text { flex: 1; text-align: justify; }
.intro .text p { margin: 0 0 2.2mm; }
.intro .pic { width: 42mm; flex: none; text-align: center; }
.intro .pic img { max-width: 42mm; max-height: 46mm; }
h2 { font-size: 11.5pt; color: #006880; margin: 4.5mm 0 2.5mm; padding-bottom: 1mm; border-bottom: 0.8pt solid #d9e6ea; font-weight: 700; }
.specs { display: flex; gap: 8mm; align-items: flex-start; }
.specs .tbl { flex: 1.35; }
.specs .fig { flex: 0.9; padding: 2mm 4mm 0; }
table { width: 100%; border-collapse: collapse; font-size: 7.2pt; }
th { background: #006880; color: #fff; text-align: left; padding: 1.3mm 2mm; font-weight: 700; }
td { padding: 1.1mm 2mm; border-bottom: 0.5pt solid #e3e8ea; vertical-align: top; }
td:first-child { font-weight: 700; width: 33%; }
tr:nth-child(even) td { background: #f7fafb; }
.cols { display: flex; gap: 10mm; }
.cols > div { flex: 1; }
ul { margin: 0; padding-left: 5mm; }
li { margin: 0 0 1mm; }
li ul { margin-top: 1.3mm; list-style: circle; }
li ul li { margin-bottom: 0.6mm; }
.footer { position: absolute; left: 16mm; right: 16mm; bottom: 9mm; text-align: center; font-size: 7pt; color: #666; }
.footer p { margin: 0 0 1.6mm; }
.footer a { color: #0067a5; text-decoration: none; }
.footer .copy { color: #888; }
.note { font-size: 7pt; color: #666; margin-top: 2mm; }
svg text { font-family: "Segoe UI", "Helvetica Neue", Helvetica, Arial, sans-serif; }
"""

def page(title, subtitle, tag, intro_html, pic_data, spec_rows, fig_svg, features_html, options_html, note='', pic_width='42mm'):
    rows = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in spec_rows)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><style>{CSS}</style></head>
<body>
<div class="header">
  <img src="{LOGO}" alt="Riverlabs">
  <div class="title"><h1>{title}</h1><p class="sub">{subtitle}</p>{('<span class="tag">'+tag+'</span>') if tag else ''}</div>
</div>
<div class="intro">
  <div class="text">{intro_html}</div>
  <div class="pic" style="width:{pic_width}"><img src="{pic_data}" alt="{title}" style="max-width:{pic_width}; max-height:{pic_width}"></div>
</div>
<h2>Technical Specifications</h2>
<div class="specs">
  <div class="tbl"><table><tr><th>Parameter</th><th>Specification</th></tr>{rows}</table>{('<p class="note">'+note+'</p>') if note else ''}</div>
  {('<div class="fig">'+fig_svg+'</div>') if fig_svg else ''}
</div>
<div class="cols">
  <div><h2>Key Features</h2>{features_html}</div>
  <div><h2>Available Options</h2>{options_html}</div>
</div>
<div class="footer">
  <p><b>Web:</b> <a href="https://github.com/ICHydro/Riverlabs">github.com/ICHydro/Riverlabs</a> &nbsp;&nbsp; <b>Email:</b> <a href="mailto:info@riverlabs.uk">info@riverlabs.uk</a> &nbsp;&nbsp; <b>Documentation:</b> <a href="https://ichydro.github.io/Riverlabs/">ichydro.github.io/Riverlabs</a></p>
  <p class="copy">&copy; 2026 Riverlabs Ltd. All rights reserved. Specifications subject to change without notice.</p>
</div>
</body></html>"""

# ---------------------------------------------------------------- LiDAR
LIDAR_FIG = """
<svg viewBox="0 0 260 250" width="100%" xmlns="http://www.w3.org/2000/svg" font-size="9">
  <defs><marker id="a" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#333"/></marker></defs>
  <!-- bridge / mounting structure -->
  <rect x="0" y="0" width="14" height="250" fill="#e6e6e6"/>
  <path d="M0 0 L14 0 M0 250 L14 250" stroke="#999"/>
  <path d="M0 12 L14 0 M0 36 L14 24 M0 60 L14 48 M0 84 L14 72 M0 108 L14 96 M0 132 L14 120 M0 156 L14 144 M0 180 L14 168 M0 204 L14 192 M0 228 L14 216 M0 250 L14 240" stroke="#bbb" stroke-width="0.8"/>
  <!-- bracket + logger -->
  <rect x="14" y="20" width="22" height="4" fill="#666"/>
  <rect x="36" y="8" width="30" height="26" rx="2" fill="#f2f2f2" stroke="#333"/>
  <rect x="42" y="34" width="18" height="10" rx="1" fill="#333"/>
  <!-- vertical beam -->
  <line x1="51" y1="44" x2="51" y2="196" stroke="#d33" stroke-width="1.2"/>
  <circle cx="51" cy="197" r="1.8" fill="#d33"/>
  <!-- angled beam -->
  <line x1="51" y1="44" x2="180" y2="197" stroke="#d33" stroke-width="1.2" stroke-dasharray="3 2"/>
  <circle cx="180" cy="197" r="1.8" fill="#d33"/>
  <!-- angle arc -->
  <path d="M51 76 A32 32 0 0 1 71 68" fill="none" stroke="#333" stroke-width="0.8"/>
  <text x="56" y="86" fill="#333">up to 40&#176;</text>
  <!-- range dimension -->
  <line x1="215" y1="46" x2="215" y2="195" stroke="#333" stroke-width="0.8" marker-start="url(#a)" marker-end="url(#a)"/>
  <line x1="66" y1="44" x2="215" y2="44" stroke="#999" stroke-width="0.5" stroke-dasharray="2 2"/>
  <text x="209" y="122" fill="#333" font-weight="600" text-anchor="end">0.05 &#8211; 35 m</text>
  <!-- water surface -->
  <path d="M14 200 q12 -5 24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0" fill="none" stroke="#00aab5" stroke-width="1.4"/>
  <path d="M14 208 q12 -4 24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0" fill="none" stroke="#8ccfb7" stroke-width="1"/>
  <text x="200" y="230" fill="#006880" font-size="8">water surface</text>
</svg>"""

LIDAR = dict(
    title='Wari LiDAR Water Level Logger',
    subtitle='Long-Range Non-Contact Water Level Monitoring',
    tag='',
    intro_html="""
<p>The Riverlabs Wari LiDAR Water Level Logger is an automatic logger system built around a Garmin LIDAR-Lite v3HP laser distance sensor. The logger is based on a low-power Atmel ATmega328P microprocessor combined with a real-time clock, 512&nbsp;Kbit internal EEPROM memory, 64&nbsp;Mbit flash memory and a MicroSD card reader.</p>
<p>With a range of up to 35&nbsp;m the LiDAR logger is suited to larger rivers, bridges and high-bank installations that are beyond the reach of ultrasonic sensors. Because the laser beam has very low divergence, the sensor can be mounted at angles of up to 40&deg; from vertical with minimal loss of accuracy and does not require clearance from nearby banks or structures.</p>
<p>The firmware is fully open source and written in the Arduino programming language, so the user can adapt it to specific purposes using the freely available Arduino IDE. By default the logger measures distance to the water surface, internal temperature and battery voltage; measurements are stored in EEPROM and flushed to the SD card at regular intervals or whenever the logger is reset.</p>""",
    pic_data=b64(SITE / 'images/Lidar.png', 'image/png'),
    spec_rows=[
        ('Measurement Range', '0.05 m &ndash; 35 m (dependent on target reflectivity)'),
        ('Water Level Resolution', '1 cm'),
        ('Water Level Accuracy', '~ 5 cm'),
        ('Measurement Angle', 'Up to 40&deg; from vertical'),
        ('Temperature Resolution', '0.25&deg;C'),
        ('Voltage Resolution', '0.01 V'),
        ('Sensor', 'Garmin LIDAR-Lite v3HP'),
        ('Microprocessor', 'ATmega328P (Arduino compatible, MiniCore bootloader)'),
        ('Memory', '512 Kbit EEPROM + 64 Mbit internal flash + MicroSD card'),
        ('Clock', 'Internal high-precision real-time clock'),
        ('Power Supply', '1 x 3.7 V Li-ion battery (18650), or<br>1 x 3.7 V Li-ion battery (14500) for the 5G option'),
        ('Solar Charging', '2 W / 6 V solar panel (cellular options)'),
        ('Water Resistance', 'IP67'),
    ],
    fig_svg=LIDAR_FIG,
    features_html="""<ul>
<li>Long-range measurement up to 35 m &ndash; suitable for large rivers and high mounting points</li>
<li>Narrow laser beam: install at angles up to 40&deg; with no bank clearance required</li>
<li>Low power consumption and long battery life</li>
<li>Fully customisable open-source firmware</li>
<li>Dual memory storage (EEPROM + SD)</li>
<li>IP67 waterproof enclosure</li>
<li>Real-time clock</li>
<li><b>Measured parameters:</b> distance to water surface, internal temperature, battery voltage</li>
</ul>""",
    options_html="""<ul>
<li>SD card storage only</li>
<li>LoRaWAN radio module &ndash; including antenna</li>
<li>3G data connection &ndash; XBee modem</li>
<li>4G NB-IoT / LTE-M modem</li>
<li>5G modem</li>
<li>Solar charging &ndash; 2 W 6 V solar panel and power regulator (included with cellular options)</li>
</ul>""",
)

# ---------------------------------------------------------------- Buoy
BUOY_FIG = """
<svg viewBox="0 0 260 250" width="100%" xmlns="http://www.w3.org/2000/svg" font-size="9">
  <defs><marker id="b" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#333"/></marker></defs>
  <!-- water body -->
  <rect x="0" y="100" width="260" height="150" fill="#eef7f9"/>
  <path d="M0 100 q13 -5 26 0 t26 0 t26 0 t26 0 t26 0 t26 0 t26 0 t26 0 t26 0 t26 0" fill="none" stroke="#00aab5" stroke-width="1.4"/>
  <!-- river bed -->
  <path d="M0 232 q40 -10 80 -4 t80 8 t100 -6 L260 250 L0 250 z" fill="#d8d0c4"/>
  <!-- buoy hull (self-righting teardrop) -->
  <path d="M130 62 C 108 62, 96 84, 96 104 C 96 130, 116 146, 130 146 C 144 146, 164 130, 164 104 C 164 84, 152 62, 130 62 z" fill="#3a3a3a" stroke="#222"/>
  <path d="M130 62 C 118 66, 110 84, 110 104" fill="none" stroke="#666" stroke-width="0.8"/>
  <!-- lid + antenna -->
  <ellipse cx="130" cy="64" rx="10" ry="3" fill="#555"/>
  <line x1="130" y1="62" x2="130" y2="40" stroke="#333" stroke-width="1.4"/>
  <circle cx="130" cy="39" r="2" fill="#333"/>
  <text x="137" y="44" fill="#333" font-size="8">LoRaWAN antenna</text>
  <!-- keel weight -->
  <ellipse cx="130" cy="143" rx="12" ry="4" fill="#8a8a8a"/>
  <text x="147" y="147" fill="#333" font-size="8">keel weight</text>
  <!-- sensors below waterline -->
  <line x1="112" y1="122" x2="70" y2="122" stroke="#333" stroke-width="0.6"/>
  <line x1="112" y1="132" x2="70" y2="132" stroke="#333" stroke-width="0.6"/>
  <text x="14" y="120" fill="#333" font-size="8">turbidity</text>
  <text x="14" y="131" fill="#333" font-size="8">temperature</text>
  <text x="14" y="142" fill="#333" font-size="8">conductivity</text>
  <line x1="112" y1="139" x2="70" y2="139" stroke="#333" stroke-width="0.6"/>
  <!-- hitching point + mooring -->
  <circle cx="97" cy="98" r="2.5" fill="none" stroke="#333" stroke-width="1"/>
  <path d="M95 99 C 70 120, 50 170, 40 226" fill="none" stroke="#555" stroke-width="1" stroke-dasharray="4 2"/>
  <path d="M30 226 l10 0 l5 8 l-20 0 z" fill="#777"/>
  <text x="52" y="222" fill="#333" font-size="8">mooring / anchor</text>
  <text x="172" y="82" fill="#333" font-size="8">single hitching point</text>
  <line x1="170" y1="84" x2="100" y2="96" stroke="#333" stroke-width="0.5"/>
  <text x="200" y="118" fill="#006880" font-size="8">water surface</text>
</svg>"""

BUOY = dict(
    title='Wari Water Quality Buoy',
    subtitle='Self-Righting Floating Logger for Turbidity, Temperature and Conductivity',
    tag='Development model',
    intro_html="""
<p>The Riverlabs Wari Water Quality Buoy is a compact, self-righting floating logger for continuous in-situ monitoring of water quality in rivers, lakes and reservoirs. Each buoy carries turbidity, water temperature and electrical conductivity sensors, and is designed to be deployed individually or as a low-cost swarm across a catchment.</p>
<p>The buoy is built on the same low-power ATmega328P logger platform as the Wari water level loggers, combined with a high-precision real-time clock, 512&nbsp;Kbit EEPROM and 64&nbsp;Mbit flash memory. The hull is 3D-printed ABS with an epoxy coating and a closed-cell neoprene seal, with a keel weight to keep the buoy upright and the sensors submerged. A single hitching point at the bow allows mooring to a fixed structure or anchor.</p>
<p>Firmware is fully open source and programmed in the Arduino environment, so the sampling interval can be adapted to each project. Data is stored internally and retrieved via an FTDI cable, or transmitted in near real time with the optional LoRaWAN radio module. Every buoy is individually calibrated against laboratory standards before dispatch.</p>""",
    pic_data=b64(SITE / 'images/Bouy.png', 'image/png'),
    spec_rows=[
        ('Turbidity', '0 &ndash; 4000 NTU (resolution 5 NTU, accuracy &plusmn;10 %)'),
        ('Temperature', '&minus;55 &ndash; 315&deg;C (resolution 0.1&deg;C, accuracy &plusmn;1 %)'),
        ('Conductivity (FEC)', '0 &ndash; 2000 &micro;S/cm (resolution 2 &micro;S/cm, accuracy &plusmn;10 %)'),
        ('Sampling Interval', 'User configurable'),
        ('Microprocessor', 'ATmega328P (Arduino compatible, MiniCore bootloader)'),
        ('Memory', '512 Kbit EEPROM + 64 Mbit internal flash (FTDI read-out)'),
        ('Clock', 'High-precision real-time clock with coin-cell backup'),
        ('Power Supply', '1 x 3.7 V Li-ion battery (14500)'),
        ('Hull &amp; Seal', 'Epoxy-coated ABS, self-righting with keel weight; closed-cell neoprene gasket'),
        ('Mooring', 'Single hitching point'),
        ('Weight', 'Approx. 300 g'),
    ],
    fig_svg='',  # installation sketch omitted for now (see BUOY_FIG)
    pic_width='54mm',
    features_html="""<ul>
<li>Three water quality parameters in one compact floating logger</li>
<li>Self-righting hull keeps sensors submerged and antenna above water</li>
<li>Low cost &ndash; designed for swarm deployments across a catchment</li>
<li>Fully customisable open-source firmware</li>
<li>Individually calibrated against laboratory standards</li>
<li>Simple maintenance &ndash; wipe clean and download data monthly</li>
<li><b>Measured parameters:</b> turbidity, water temperature, electrical conductivity, battery voltage</li>
</ul>""",
    options_html="""<ul>
<li>Internal storage only</li>
<li>LoRaWAN radio module &ndash; including antenna</li>
<li>Additional sensors (e.g. optical pH) under development &ndash; contact us</li>
</ul>""",
)

def build(name, spec):
    html = OUT / f'{name}.html'
    pdf = OUT / f'{name}.pdf'
    html.write_text(page(**spec))
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                    f'--print-to-pdf={pdf}', str(html)], check=True, capture_output=True)
    html.unlink()
    print('built', pdf)

if __name__ == '__main__':
    build('Lidar_Sensor_Datasheet', LIDAR)
    build('Water_Quality_Buoy_Datasheet', BUOY)
