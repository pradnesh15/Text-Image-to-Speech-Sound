<h1>Text-Image-to-Speech-Sound</h1>

<p>This project extracts text from an image and converts it into an MP3 audio file. It combines Optical Character Recognition (OCR) with text-to-speech conversion to achieve this.</p>

<h2>Features</h2>
<ul>
  <li>Extracts text from images using OCR.</li>
  <li>Converts extracted text into speech.</li>
  <li>Outputs the speech as an MP3 file.</li>
</ul>

<h2>Prerequisites</h2>
<ul>
  <li>Python 3.x</li>
  <li><code>pytesseract</code> for OCR</li>
  <li><code>gTTS</code> for text-to-speech conversion</li>
  <li><code>Pillow</code> for image handling</li>
</ul>

<h2>Installation</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/pradnesh15/Text-Image-to-Speech-Sound.git</code></pre>
  </li>
  <li>Install the required libraries:
    <pre><code>pip install pytesseract gTTS Pillow</code></pre>
  </li>
</ol>

<h2>Usage</h2>
<ol>
  <li>Place the image you want to process in the root directory.</li>
    <p>Also you can add NLP for processing the audio text if required.</p>
  <li>Run the script:
    <pre><code>python ImageText_To_Sound.py</code></pre>
  </li>
  <li>The output will be saved as <code>output.mp3</code>.</li>
</ol>

<h2>License</h2>
<p>This project is licensed under the MIT License.</p>
