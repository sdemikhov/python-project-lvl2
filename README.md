<h1>python-project-lvl2</h1>
<div>
<p><a href="https://codeclimate.com/github/sdemikhov/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/2112654519a56e92571a/maintainability" /></a>
<a href="https://travis-ci.org/sdemikhov/python-project-lvl2"><img src="https://travis-ci.org/sdemikhov/python-project-lvl2.svg?branch=master" /></a></p>
<p>Gendiff is a CLI tool to find the difference between two plain JSON/YAML files.</p>
<h2>Install gendiff:</h2>
<pre>pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.python.org/pypi/ sdemikhov-gendiff</pre>
<ul><li>use pip install --user to install packages into your day-to-day default Python environment.</li></ul>
<h2>Run gendiff:</h2>
<p>To run gendiff use following commands:<ul><li>gendiff path/to/file1 path/to/file2</li><li>gendiff -h</li></ul></p>
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
<h2>Install and run demo:</h2>
<p><a href="https://asciinema.org/a/NHZoftKjlnyPKrlitPAd2cvHO" target="_blank"><img src="https://asciinema.org/a/NHZoftKjlnyPKrlitPAd2cvHO.svg" /></a></p>
</div>
