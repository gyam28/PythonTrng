book = 24.95
quantity = 60
bookstore = (book * 60) / 100
firstShipping = 3
totalShipping = firstShipping + ((quantity - 1)* 0.75)
total = (bookstore * quantity) + totalShipping
print("The price from store is {} for a book" .format(bookstore))
print("The price for 60 pcs is %d" %total)

#################################################################

startH = 6
startM = 52
easyPace = (8 * 60) + 15
hardTempo = (7 * 60) + 12
totalEasyTempo = easyPace * 2
totalHardTempo = hardTempo * 3
totalTimeOut = totalEasyTempo + totalHardTempo
tm = totalTimeOut / 60
ts = totalTimeOut - (tm * 60)

endM = (startM+tm)%60
endH = startH + (startM+tm)/60

print("The time spent out is %dm%ds" %(tm, ts))
print("I get home for breakfast at %d:%d" %(endH, endM))

#alternative solving
start = 6.52
easy_pace = 8.15
tempo = 7

minute = 60
tempo_second = tempo * minute + 12
easy_second = easy_pace * minute + 15
total_mile = easy_second *1 + tempo_second * 3 + easy_pace *1
total_minutes = total_mile/60
print(total_minutes) #got different result, wtf?
