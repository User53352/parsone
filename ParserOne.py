
>>> import requests # импорт необходимых библиотек для добычи данных
>>> from bs4 import BeautifulSoup 
>>> url = "https://scrapingclub.com/exercise/detail_basic/" # ресурс для тренировок
>>> soup = BeautifulSoup(url.text, "lxml") # без ошибок никуда
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'text'
>>> response = requests.get(url) 
>>> soup = BeautifulSoup(response.text, "lxml")
>>> print(soup) # получаем структуру html-файла из которого в дальнейшем будем вытаскивать данные
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<link href="/static/img/icon.611132651e39.png" rel="icon" type="image/png"/>
<meta content="Web scraping using XPath or CSS expression" name="description"/><title>Basic Info Scraping | ScrapingClub</title>
<!-- Bootstrap core CSS -->
<link href="/static/bootstrap/css/bootstrap.min.a9766a313743.css" rel="stylesheet"/>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
<link href="/static/css/custom.e6122d0f915e.css" rel="stylesheet"/>
</head>
<body>
<nav class="navbar navbar-expand-lg fixed-top navbar-dark bg-primary">
<div class="container">
<a class="navbar-brand" href="/">
<img alt="ScrapingClub" class="nav-logo" src="/static/img/brand-logo.ad7a4888d334.png"/>
</a>
<button aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#navbarCollapse" data-toggle="collapse" type="button">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="navbarCollapse">
<ul class="navbar-nav mr-auto">
<li class="nav-item">
<a class="nav-link" href="/">Home
            <span class="sr-only">(current)</span>
</a>
</li>
<li class="nav-item">
<a class="nav-link" href="/blog/">Blog</a>
</li>
<li class="nav-item">
<a class="nav-link" href="/about/">About</a>
</li>
<li class="nav-item">
<a class="nav-link" href="/contact/">Contact</a>
</li>
<li class="nav-item">
<a class="nav-link" href="https://leanpub.com/ultimateguidetoscrapy/" target="_blank">eBook</a>
</li>
<li class="nav-item active">
<a class="nav-link" href="//eepurl.com/dmPGn9"><i class="fa fa-send"></i> Subscribe</a>
</li>
</ul>
</div>
</div>
</nav>
<!-- Page Content -->
<div class="container mt-4">
<div class="row">
<div class="col-lg-8">
<div class="my-4">
<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Donation</h4>
<p>This project was built to help people and I did not earn money from my work.
                But you can still support my work
              </p>
<ul>
<li><a href="//buymeacoff.ee/0JqEZkHre" target="_blank">Buy me a coffee!</a></li>
<li><a href="https://leanpub.com/ultimateguidetoscrapy/" target="_blank">Ultimate Guide To Scrapy (eBook)</a></li>
</ul>
</div>
</div>
<div class="alert alert-info my-4" role="alert">
<p>Right now there are mainly four typical methods for you to extract data.</p>
<ol>
<li><code>CSS extraction</code></li>
<li><code>XPath extraction</code></li>
<li><code>Regex extraction</code></li>
<li><code>Custom methods</code> shipped with some package such as <code>find_all</code> in <code>BeautifulSoup</code></li>
</ol>
<p>You can choose the one you like to extract the info, in this exercise, try to extract this product detail such as title, desc and price.</p>
<p>Tips:</p>
<ol>
<li>I recommend you to learn XPath if you have no idea where to start, <a href="/blog/scrapy-tutorial-7-how-use-xpath-scrapy/">How to use XPath with Scrapy</a></li>
</ol>
</div>
<div class="card mt-4 my-4">
<img alt="Long-sleeved Jersey Top" class="card-img-top img-fluid" src="/static/img/73840-Q.jpg"/>
<div class="card-body">
<h3 class="card-title">Long-sleeved Jersey Top</h3>
<h4>$12.99</h4>
<p class="card-text">CONSCIOUS. Fitted, long-sleeved top in stretch jersey made from organic cotton with a round neckline. 92% cotton, 3% spandex, 3% rayon, 2% polyester.</p>
</div>
</div>
<!-- /.card -->
</div>
<!-- /.col-lg-8 -->
<div class="col-lg-4">
<div class="card card-outline-secondary my-4">
<div class="card-header">
       Exercise List 
    </div>
<div class="card-body">
<p>
<a class="" href="/exercise/detail_basic/">Basic Info Scraping</a>
</p>
<p>Web scraping using XPath or CSS expression</p>
<hr/>
<!-- <small class="text-muted">Posted by Anonymous on 3/1/17</small> -->
<!-- <a href="#" class="btn btn-success">Leave a Review</a> -->
<p>
<a class="" href="/exercise/detail_json/">Analyze JSON</a>
</p>
<p>Load JSON string and extract data</p>
<hr/>
<!-- <small class="text-muted">Posted by Anonymous on 3/1/17</small> -->
<!-- <a href="#" class="btn btn-success">Leave a Review</a> -->
<p>
<a class="" href="/exercise/list_basic/">Recursively Scraping pages</a>
</p>
<p>Not only crawl products but also handle pagination</p>
<hr/>
<!-- <small class="text-muted">Posted by Anonymous on 3/1/17</small> -->
<!-- <a href="#" class="btn btn-success">Leave a Review</a> -->
<p>
<a class="" href="/exercise/detail_ajax/">Mimicking Ajax requests</a>
</p>
<p>Inspect Ajax requests and mimic them</p>
<hr/>
<!-- <small class="text-muted">Posted by Anonymous on 3/1/17</small> -->
<!-- <a href="#" class="btn btn-success">Leave a Review</a> -->
<p>
<a class="" href="/exercise/detail_header/">Inspect HTTP request</a>
</p>
<p>Learn to inspect the fields of HTTP request</p>
<hr/>
<!-- <small class="text-muted">Posted by Anonymous on 3/1/17</small> -->
<!-- <a href="#" class="btn btn-success">Leave a Review</a> -->
<p>
<a class="" href="/exercise/list_infinite_scroll/">Scraping Infinite Scrolling Pages (Ajax)</a>
</p>
<p>Learn to scrape infinite scrolling pages</p>
<hr/>
<!-- <small class="text-muted">Posted by Anonymous on 3/1/17</small> -->
<!-- <a href="#" class="btn btn-success">Leave a Review</a> -->
<p>
<a class="" href="/exercise/detail_cookie/">Find gold in cookie</a>
</p>
<p>Make your spider can work with the cookie</p>
<hr/>
<!-- <small class="text-muted">Posted by Anonymous on 3/1/17</small> -->
<!-- <a href="#" class="btn btn-success">Leave a Review</a> -->
<p>
<a class="" href="/exercise/basic_login/">Login form</a>
</p>
<p>Scrape data behind login form</p>
<hr/>
<!-- <small class="text-muted">Posted by Anonymous on 3/1/17</small> -->
<!-- <a href="#" class="btn btn-success">Leave a Review</a> -->
<p>
<a class="" href="/exercise/basic_captcha/">Solve Captcha</a>
</p>
<p>Learn to scrape data behind a captcha</p>
<hr/>
<!-- <small class="text-muted">Posted by Anonymous on 3/1/17</small> -->
<!-- <a href="#" class="btn btn-success">Leave a Review</a> -->
<p>
<a class="" href="/exercise/detail_sign/">Decode minified javascript</a>
</p>
<p>Learn how to analyze minimized or compressed javascript</p>
<hr/>
<!-- <small class="text-muted">Posted by Anonymous on 3/1/17</small> -->
<!-- <a href="#" class="btn btn-success">Leave a Review</a> -->
</div>
</div>
</div>
<!-- /.col-lg-4 -->
</div>
</div>
<!-- /.container -->
<!-- Footer -->
<footer class="py-4 bg-primary">
<div class="container">
<p class="m-0 text-center text-white">Made with <span class="sh-red">❤</span> by <a href="https://blog.michaelyin.info/">MichaelYin</a></p>
</div>
<!-- /.container -->
</footer>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-39890589-8"></script>
<script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'UA-39890589-8');
    </script>
<!-- Bootstrap core JavaScript -->
<script src="/static/jquery/jquery.min.a09e13ee94d5.js"></script>
<script src="/static/bootstrap/js/bootstrap.min.14d449eb8876.js"></script>
</body>
</html>

>>> soup.title
<title>Basic Info Scraping | ScrapingClub</title>
>>> soup.title.name
'title'
>>> soup.title.string 
'Basic Info Scraping | ScrapingClub'
>>> soup.h1 # так не правильно! 
>>> print(soup.h1)
None
>>> print(soup.p)
<p>This project was built to help people and I did not earn money from my work.
                But you can still support my work
              </p>
>>> soup.a
<a class="navbar-brand" href="/">
<img alt="ScrapingClub" class="nav-logo" src="/static/img/brand-logo.ad7a4888d334.png"/>
</a>
>>> soup.href
>>> soup.div
<div class="container">
<a class="navbar-brand" href="/">
<img alt="ScrapingClub" class="nav-logo" src="/static/img/brand-logo.ad7a4888d334.png"/>
</a>
<button aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#navbarCollapse" data-toggle="collapse" type="button">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="navbarCollapse">
<ul class="navbar-nav mr-auto">
<li class="nav-item">
<a class="nav-link" href="/">Home
            <span class="sr-only">(current)</span>
</a>
</li>
<li class="nav-item">
<a class="nav-link" href="/blog/">Blog</a>
</li>
<li class="nav-item">
<a class="nav-link" href="/about/">About</a>
</li>
<li class="nav-item">
<a class="nav-link" href="/contact/">Contact</a>
</li>
<li class="nav-item">
<a class="nav-link" href="https://leanpub.com/ultimateguidetoscrapy/" target="_blank">eBook</a>
</li>
<li class="nav-item active">
<a class="nav-link" href="//eepurl.com/dmPGn9"><i class="fa fa-send"></i> Subscribe</a>
</li>
</ul>
</div>
</div>
>>> soup.div['class']
['container']
>>> soup.find_all(p)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'p' is not defined
>>> soup.find_all('p')
[<p>This project was built to help people and I did not earn money from my work.
                But you can still support my work
              </p>, <p>Right now there are mainly four typical methods for you to extract data.</p>, <p>You can choose the one you like to extract the info, in this exercise, try to extract this product detail such as title, desc and price.</p>, <p>Tips:</p>, <p class="card-text">CONSCIOUS. Fitted, long-sleeved top in stretch jersey made from organic cotton with a round neckline. 92% cotton, 3% spandex, 3% rayon, 2% polyester.</p>, <p>
<a class="" href="/exercise/detail_basic/">Basic Info Scraping</a>
</p>, <p>Web scraping using XPath or CSS expression</p>, <p>
<a class="" href="/exercise/detail_json/">Analyze JSON</a>
</p>, <p>Load JSON string and extract data</p>, <p>
<a class="" href="/exercise/list_basic/">Recursively Scraping pages</a>
</p>, <p>Not only crawl products but also handle pagination</p>, <p>
<a class="" href="/exercise/detail_ajax/">Mimicking Ajax requests</a>
</p>, <p>Inspect Ajax requests and mimic them</p>, <p>
<a class="" href="/exercise/detail_header/">Inspect HTTP request</a>
</p>, <p>Learn to inspect the fields of HTTP request</p>, <p>
<a class="" href="/exercise/list_infinite_scroll/">Scraping Infinite Scrolling Pages (Ajax)</a>
</p>, <p>Learn to scrape infinite scrolling pages</p>, <p>
<a class="" href="/exercise/detail_cookie/">Find gold in cookie</a>
</p>, <p>Make your spider can work with the cookie</p>, <p>
<a class="" href="/exercise/basic_login/">Login form</a>
</p>, <p>Scrape data behind login form</p>, <p>
<a class="" href="/exercise/basic_captcha/">Solve Captcha</a>
</p>, <p>Learn to scrape data behind a captcha</p>, <p>
<a class="" href="/exercise/detail_sign/">Decode minified javascript</a>
</p>, <p>Learn how to analyze minimized or compressed javascript</p>, <p class="m-0 text-center text-white">Made with <span class="sh-red">❤</span> by <a href="https://blog.michaelyin.info/">MichaelYin</a></p>]
>>> soup.find_all('p', class_='text')
[]
>>> soupText = soup.find_all('p') # луяше использовать переменные и выведем просто текст
>>> for i in soupText:
...     print(i.text)
... 
This project was built to help people and I did not earn money from my work.
                But you can still support my work
              
Right now there are mainly four typical methods for you to extract data.
You can choose the one you like to extract the info, in this exercise, try to extract this product detail such as title, desc and price.
Tips:
CONSCIOUS. Fitted, long-sleeved top in stretch jersey made from organic cotton with a round neckline. 92% cotton, 3% spandex, 3% rayon, 2% polyester.

Basic Info Scraping

Web scraping using XPath or CSS expression

Analyze JSON

Load JSON string and extract data

Recursively Scraping pages

Not only crawl products but also handle pagination

Mimicking Ajax requests

Inspect Ajax requests and mimic them

Inspect HTTP request

Learn to inspect the fields of HTTP request

Scraping Infinite Scrolling Pages (Ajax)

Learn to scrape infinite scrolling pages

Find gold in cookie

Make your spider can work with the cookie

Login form

Scrape data behind login form

Solve Captcha

Learn to scrape data behind a captcha

Decode minified javascript

Learn how to analyze minimized or compressed javascript
Made with ❤ by MichaelYin
>>> 
