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
	fromapi = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=" + number)
	carddata = json.loads(fromapi.text)
	cards = carddata['cards']
	
	i = number
	i = int(i)
	print(type(i), flush=True)
	while i > 0:
		i = str(i)
		cardnum = "card"+ i
		try:
			cardnum = cards[i-1]
		except:
			cardnum = None
	i = int(i)
	print(type(i), flush=True)
	i = i - 1



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
	
	# card2 = cards[1]
	# cardimage2 = card2['image']
	# card3 = cards[2]
	# cardimage3 = card3['image']
	#return cardimage
	return render_template(
		'output.html', 
		number=number, 
		cardimage1=cardimage1,
		cardimage2=cardimage2,
		cardimage3=cardimage3
		)






app.run()