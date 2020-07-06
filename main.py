import uuid
import json
import time
import requests
from flask import (
	Flask, 
	request,
	Response,
	render_template
)


pileid = uuid.uuid1()
print(pileid)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def getcards():
	number = int()
	return render_template('input.html', number=number)


@app.route('/', methods=['POST'])
def getcards_post():
	number = request.form['number']
	num = (int(number))
	fromapi = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=" + number)
	carddata = json.loads(fromapi.text)
	cards = carddata['cards']
	
	try:
			card1 = cards[0]
	except:
			card1 = None


	try:
			card2 = cards[1]
	except:
			card2 = None


	try:
			card3 = cards[2]
	except:
			card3 = None


	try:
			card4 = cards[3]
	except:
			card4 = None


	try:
			card5 = cards[4]
	except:
			card5 = None


	try:
			card6 = cards[5]
	except:
			card6 = None


	try:
			card7 = cards[6]
	except:
			card7 = None


	try:
			card8 = cards[7]
	except:
			card8 = None


	try:
			card9 = cards[8]
	except:
			card9 = None


	try:
			card10 = cards[9]
	except:
			card10 = None


	try:
			card11 = cards[10]
	except:
			card11 = None


	try:
			card12 = cards[11]
	except:
			card12 = None


	try:
			card13 = cards[12]
	except:
			card13 = None


	try:
			card14 = cards[13]
	except:
			card14 = None


	try:
			card15 = cards[14]
	except:
			card15 = None


	try:
			card16 = cards[15]
	except:
			card16 = None


	try:
			card17 = cards[16]
	except:
			card17 = None


	try:
			card18 = cards[17]
	except:
			card18 = None


	try:
			card19 = cards[18]
	except:
			card19 = None


	try:
			card20 = cards[19]
	except:
			card20 = None


	try:
			card21 = cards[20]
	except:
			card21 = None


	try:
			card22 = cards[21]
	except:
			card22 = None


	try:
			card23 = cards[22]
	except:
			card23 = None


	try:
			card24 = cards[23]
	except:
			card24 = None


	try:
			card25 = cards[24]
	except:
			card25 = None


	try:
			card26 = cards[25]
	except:
			card26 = None


	try:
			card27 = cards[26]
	except:
			card27 = None


	try:
			card28 = cards[27]
	except:
			card28 = None


	try:
			card29 = cards[28]
	except:
			card29 = None


	try:
			card30 = cards[29]
	except:
			card30 = None


	try:
			card31 = cards[30]
	except:
			card31 = None


	try:
			card32 = cards[31]
	except:
			card32 = None


	try:
			card33 = cards[32]
	except:
			card33 = None


	try:
			card34 = cards[33]
	except:
			card34 = None


	try:
			card35 = cards[34]
	except:
			card35 = None


	try:
			card36 = cards[35]
	except:
			card36 = None


	try:
			card37 = cards[36]
	except:
			card37 = None


	try:
			card38 = cards[37]
	except:
			card38 = None


	try:
			card39 = cards[38]
	except:
			card39 = None


	try:
			card40 = cards[39]
	except:
			card40 = None


	try:
			card41 = cards[40]
	except:
			card41 = None


	try:
			card42 = cards[41]
	except:
			card42 = None


	try:
			card43 = cards[42]
	except:
			card43 = None


	try:
			card44 = cards[43]
	except:
			card44 = None


	try:
			card45 = cards[44]
	except:
			card45 = None


	try:
			card46 = cards[45]
	except:
			card46 = None


	try:
			card47 = cards[46]
	except:
			card47 = None


	try:
			card48 = cards[47]
	except:
			card48 = None


	try:
			card49 = cards[48]
	except:
			card49 = None


	try:
			card50 = cards[49]
	except:
			card50 = None


	try:
			card51 = cards[50]
	except:
			card51 = None


	try:
			card52 = cards[51]
	except:
			card52 = None


	if card1 != None:
			cardimage1 = card1['image']
	else:
			cardimage1 = None


	if card2 != None:
			cardimage2 = card2['image']
	else:
			cardimage2 = None


	if card3 != None:
			cardimage3 = card3['image']
	else:
			cardimage3 = None


	if card4 != None:
			cardimage4 = card4['image']
	else:
			cardimage4 = None


	if card5 != None:
			cardimage5 = card5['image']
	else:
			cardimage5 = None


	if card6 != None:
			cardimage6 = card6['image']
	else:
			cardimage6 = None


	if card7 != None:
			cardimage7 = card7['image']
	else:
			cardimage7 = None


	if card8 != None:
			cardimage8 = card8['image']
	else:
			cardimage8 = None


	if card9 != None:
			cardimage9 = card9['image']
	else:
			cardimage9 = None


	if card10 != None:
			cardimage10 = card10['image']
	else:
			cardimage10 = None


	if card11 != None:
			cardimage11 = card11['image']
	else:
			cardimage11 = None


	if card12 != None:
			cardimage12 = card12['image']
	else:
			cardimage12 = None


	if card13 != None:
			cardimage13 = card13['image']
	else:
			cardimage13 = None


	if card14 != None:
			cardimage14 = card14['image']
	else:
			cardimage14 = None


	if card15 != None:
			cardimage15 = card15['image']
	else:
			cardimage15 = None


	if card16 != None:
			cardimage16 = card16['image']
	else:
			cardimage16 = None


	if card17 != None:
			cardimage17 = card17['image']
	else:
			cardimage17 = None


	if card18 != None:
			cardimage18 = card18['image']
	else:
			cardimage18 = None


	if card19 != None:
			cardimage19 = card19['image']
	else:
			cardimage19 = None


	if card20 != None:
			cardimage20 = card20['image']
	else:
			cardimage20 = None


	if card21 != None:
			cardimage21 = card21['image']
	else:
			cardimage21 = None


	if card22 != None:
			cardimage22 = card22['image']
	else:
			cardimage22 = None


	if card23 != None:
			cardimage23 = card23['image']
	else:
			cardimage23 = None


	if card24 != None:
			cardimage24 = card24['image']
	else:
			cardimage24 = None


	if card25 != None:
			cardimage25 = card25['image']
	else:
			cardimage25 = None


	if card26 != None:
			cardimage26 = card26['image']
	else:
			cardimage26 = None


	if card27 != None:
			cardimage27 = card27['image']
	else:
			cardimage27 = None


	if card28 != None:
			cardimage28 = card28['image']
	else:
			cardimage28 = None


	if card29 != None:
			cardimage29 = card29['image']
	else:
			cardimage29 = None


	if card30 != None:
			cardimage30 = card30['image']
	else:
			cardimage30 = None


	if card31 != None:
			cardimage31 = card31['image']
	else:
			cardimage31 = None


	if card32 != None:
			cardimage32 = card32['image']
	else:
			cardimage32 = None


	if card33 != None:
			cardimage33 = card33['image']
	else:
			cardimage33 = None


	if card34 != None:
			cardimage34 = card34['image']
	else:
			cardimage34 = None


	if card35 != None:
			cardimage35 = card35['image']
	else:
			cardimage35 = None


	if card36 != None:
			cardimage36 = card36['image']
	else:
			cardimage36 = None


	if card37 != None:
			cardimage37 = card37['image']
	else:
			cardimage37 = None


	if card38 != None:
			cardimage38 = card38['image']
	else:
			cardimage38 = None


	if card39 != None:
			cardimage39 = card39['image']
	else:
			cardimage39 = None


	if card40 != None:
			cardimage40 = card40['image']
	else:
			cardimage40 = None


	if card41 != None:
			cardimage41 = card41['image']
	else:
			cardimage41 = None


	if card42 != None:
			cardimage42 = card42['image']
	else:
			cardimage42 = None


	if card43 != None:
			cardimage43 = card43['image']
	else:
			cardimage43 = None


	if card44 != None:
			cardimage44 = card44['image']
	else:
			cardimage44 = None


	if card45 != None:
			cardimage45 = card45['image']
	else:
			cardimage45 = None


	if card46 != None:
			cardimage46 = card46['image']
	else:
			cardimage46 = None


	if card47 != None:
			cardimage47 = card47['image']
	else:
			cardimage47 = None


	if card48 != None:
			cardimage48 = card48['image']
	else:
			cardimage48 = None


	if card49 != None:
			cardimage49 = card49['image']
	else:
			cardimage49 = None


	if card50 != None:
			cardimage50 = card50['image']
	else:
			cardimage50 = None


	if card51 != None:
			cardimage51 = card51['image']
	else:
			cardimage51 = None


	if card52 != None:
			cardimage52 = card52['image']
	else:
			cardimage52 = None
		
	return render_template(
		'output.html', 
		number=number, 
		num=num,
		cardimage1=cardimage1,
		cardimage2=cardimage2,
		cardimage3=cardimage3,
		cardimage4=cardimage4,
		cardimage5=cardimage5,
		cardimage6=cardimage6,
		cardimage7=cardimage7,
		cardimage8=cardimage8,
		cardimage9=cardimage9,
		cardimage10=cardimage10,
		cardimage11=cardimage11,
		cardimage12=cardimage12,
		cardimage13=cardimage13,
		cardimage14=cardimage14,
		cardimage15=cardimage15,
		cardimage16=cardimage16,
		cardimage17=cardimage17,
		cardimage18=cardimage18,
		cardimage19=cardimage19,
		cardimage20=cardimage20,
		cardimage21=cardimage21,
		cardimage22=cardimage22,
		cardimage23=cardimage23,
		cardimage24=cardimage24,
		cardimage25=cardimage25,
		cardimage26=cardimage26,
		cardimage27=cardimage27,
		cardimage28=cardimage28,
		cardimage29=cardimage29,
		cardimage30=cardimage30,
		cardimage31=cardimage31,
		cardimage32=cardimage32,
		cardimage33=cardimage33,
		cardimage34=cardimage34,
		cardimage35=cardimage35,
		cardimage36=cardimage36,
		cardimage37=cardimage37,
		cardimage38=cardimage38,
		cardimage39=cardimage39,
		cardimage40=cardimage40,
		cardimage41=cardimage41,
		cardimage42=cardimage42,
		cardimage43=cardimage43,
		cardimage44=cardimage44,
		cardimage45=cardimage45,
		cardimage46=cardimage46,
		cardimage47=cardimage47,
		cardimage48=cardimage48,
		cardimage49=cardimage49,
		cardimage50=cardimage50,
		cardimage51=cardimage51,
		cardimage52=cardimage52
		)






app.run()