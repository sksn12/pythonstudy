from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
#pip list사용하면 설치된 pip들을 보여줌 (터미널에서 사용해야함)
# https://pypi.org 사이트에서 사용할 프로젝트를 복사해 터미널에서 설치하고 사용