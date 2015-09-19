self.response.write('<html><body>')
    self.response.write('<table>')
    page = requests.get('http://mlh.io/seasons/f2015/events')
    tree = html.fromstring(page.text)
    events = tree.xpath('//div[@class="event-wrapper"]/a/div/h3/text()')
    logos = tree.xpath('//div[@class="event-logo"]/img/@src')

    datesLongList = tree.xpath('//div[@class="event-wrapper"]/a/div/p/text()')

    dates = []

    for i in xrange(0,len(datesLongList),2):
        dates.append(datesLongList[i])

    i = 0
    dictMonths = {'January':0,'February':31,'March':59,'April':90,'May':120,'June':151,'July':181,'August':212,'September':243,'October':273,'November':304,'December':334}
    for date,event,logo in zip(dates,events,logos):
        sections = date.split(" ")
        dateStart = sections[1]
        daysPassed = dictMonths[sections[0]]
        daysStart = daysPassed + int(dateStart[:len(dateStart)-2])
        daysCurrent = dictMonths[datetime.datetime.now().strftime("%B")] + int(datetime.datetime.now().strftime("%d"))
        daysToEvent = daysStart - daysCurrent
        if (daysToEvent <= 21 and daysToEvent >= 0):
            i += 1
            self.response.write("<td><img hspace='20' src=%s />" % logo)
            self.response.write("<br/><p align='center'>" + event + "</p></td>")
            if (i == 3):
                self.response.write("</tr><tr>")
                i = 0
    self.response.write("</tr>")
    self.response.write("</body></html>")