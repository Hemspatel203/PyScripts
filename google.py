import bs4, webbrowser, requests, sys, pyperclip

print('googling........')

if len(sys.argv) > 1:
	#print('http://google.com/search?q='+''.join(pyperclip.paste()))
	res = requests.get('http://google.com/search?q='+''.join(sys.argv[1:]))
else:
	res = requests.get('http://google.com/search?q='+''.join(pyperclip.paste()))

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"lxml")
linkElems = soup.select('.r a')

numopen = min(5, len(linkElems))
for i in range(numopen):
	webbrowser.open('http://google.com'+ linkElems[i].get('href'))
