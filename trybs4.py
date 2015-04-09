from bs4 import BeautifulSoup
import xlsxwriter
workbook= xlsxwriter.Workbook("data.xlsx")
worksheet = workbook.add_worksheet()

f = open('rough.html',"r")
data=f.read()
soup=BeautifulSoup(data)
div = soup.find('div', {"class":'dataTables_scroll'})
table=div.find('table')
tbody=div.find('tbody')
rows=tbody.find_all('tr')

rowno = 0
for row in rows:
	a=row.find_all('a')
	td=row.find_all('td')
	worksheet.write(rowno, 1, a[2].text)
	worksheet.write(rowno, 2, td[3].text[td[3].text.find('P:'):])
	worksheet.write(rowno, 3, a[3].text)
	worksheet.write(rowno, 4, a[4].text)
	worksheet.write(rowno, 5, a[3].text)
	worksheet.write(rowno, 6, td[6].text)
	rowno=rowno+1

workbook.close()
print "Done"


