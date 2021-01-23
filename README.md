<h1>python-project-lvl2</h1>
<div>
<p><a href="https://codeclimate.com/github/sdemikhov/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/2112654519a56e92571a/maintainability" /></a>
<a href="https://travis-ci.org/sdemikhov/python-project-lvl2"><img src="https://travis-ci.org/sdemikhov/python-project-lvl2.svg?branch=master" /></a></p>
<p>Gendiff is a python CLI tool to find the difference between two JSON/YAML files. See also <a href="https://github.com/sdemikhov/python-project-lvl2">node.js version</a>.</p>
<h2>Install gendiff:</h2>
<pre>pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.python.org/pypi/ sdemikhov-gendiff</pre>
<ul><li>use pip install --user to install packages into your day-to-day default Python environment.</li></ul>
<h2>Run gendiff:</h2>
<pre>usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file            location in a file system for first file
  second_file           location in a file system for second file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        Output format: 'nested', 'plain', 'json' (default
                        nested)
</pre>
<p>You can also use gendiff as a library in your code:</p>
<pre>>>> from gendiff import generate_diff
>>> diff = generate_diff('before.json', 'after.json')
>>> print(diff)
{
    host: hexlet.io
  + timeout: 20
  - timeout: 50
  - proxy: 123.234.53.22
  + verbose: True
}</pre>
<h2>Development process:</h2>
<ul>
  <li>
    <p>Comparison of plain files (JSON):</p>
    <p><a href="https://asciinema.org/a/V2F2qBXuXhSvMpjR6giEdyRJW" target="_blank"><img src="https://asciinema.org/a/V2F2qBXuXhSvMpjR6giEdyRJW.svg" /></a></p>
  </li>
  <li>
    <p>Comparison of plain files (YAML):</p>
    <p><a href="https://asciinema.org/a/f96PUYIT3vzzQdgIwT6OcqlHR" target="_blank"><img src="https://asciinema.org/a/f96PUYIT3vzzQdgIwT6OcqlHR.svg" /></a></p>
  </li>
   <li>
    <p>Recursive comparsion of complex nested files (YAML, JSON):</p>
    <p><a href="https://asciinema.org/a/NHZoftKjlnyPKrlitPAd2cvHO" target="_blank"><img src="https://asciinema.org/a/NHZoftKjlnyPKrlitPAd2cvHO.svg" /></a></p>
  </li>
   <li>
    <p>Plain output format:</p>
    <p><a href="https://asciinema.org/a/ZZ73v5fi1puM8RzWI15lx8NSg" target="_blank"><img src="https://asciinema.org/a/ZZ73v5fi1puM8RzWI15lx8NSg.svg" /></a></p>
  </li>
   <li>
    <p>JSON compatible output format:</p>
    <p><a href="https://asciinema.org/a/mCh0r0IPX0KHNd26c4rzSqhrV" target="_blank"><img src="https://asciinema.org/a/mCh0r0IPX0KHNd26c4rzSqhrV.svg" /></a></p>
  </li>
</ul>
</div>
