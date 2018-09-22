extends CanvasLayer

# class member variables go here, for example:
# var a = 2
# var b = "textvar"
signal start_game
var pomelo
var httpClient

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	pomelo = $"../global".pomelo
	httpClient = $"../global".httpClient

#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass
func show_message(text):
	$MessageLabel.text = text
	$MessageLabel.show()
	$MessageTimer.start()
	
func show_game_over():
	show_message("Game Over")
	yield($MessageTimer, "timeout")
	$StartButton.show()
	$MessageLabel.text = "Dodge the 	Creeps"
	$MessageLabel.show()
	
func update_score(score):
	$ScoreLabel.text = str(score)
	


func _on_MessageTimer_timeout():
	$MessageLabel.hide()


func _on_StartButton_pressed():
	$StartButton.hide()
	emit_signal("start_game")
	pomelo.request("connector.user.login",{ "uid": 10027,"un":"162AB976-3615-C2FD-FDFC-ABB37A7F5D27@mobile","nn":"幸福中的菜菜","key":"cd8655806f6cce663b68a6de49b84d95|1||zh_CN"},self,"_on_query_entry")
	#host,port,path,msg,cb,isRaw
#	httpClient.post('http://sh.17dmj.com',80,'/mobile/weeklyRankingsAward',{token='flwARWKrY-UX6HTho1vMmSBtt5guNtkP41wwBbl.eZ3eXHcGdvFyOsj7VFUhlXxTBE.SLfUxdxL9WRYUK5bvgIlKRIlNdJRT51bHjeqq64yDCeBhw7Gr1Q'},{instance=self,f='_button2rep'})
	$HTTPRequest.request("http://sh.17dmj.com/mobile/weeklyRankingsAward?token=flwARWKrY-UX6HTho1vMmSBtt5guNtkP41wwBbl.eZ3eXHcGdvFyOsj7VFUhlXxTBE.SLfUxdxL9WRYUK5bvgIlKRIlNdJRT51bHjeqq64yDCeBhw7Gr1Q")

func _on_query_entry(msg):
	print(msg)
	print(msg.code)

func _button2rep(data):
	#get_node('Button2').set_text(data)
	print('#################################')
	print(data)


func _on_HTTPRequest_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	print(json.result)

