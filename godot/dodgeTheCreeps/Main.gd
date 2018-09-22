extends Node

# class member variables go here, for example:
# var a = 2
# var b = "textvar"
export(String) var host = "127.0.0.1"
export(int) var port = 3010
export (PackedScene) var Mob
var score
var pomelo
var httpClient 

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	#pomelo = get_node("/root/global").pomelo
	pomelo = $global.pomelo
	httpClient = $global.httpClient
	
	pomelo.init(host,port)
	pomelo.on("error",self,"_on_errror")
	randomize()

#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass


func game_over():
	$ScoreTimer.stop()
	$MobTimer.stop()
	$HUD.show_game_over()
	#$Music.stop()
	$DeathSound.play()

func new_game():
	 score = 0;
	 $Player.start($StartPosition.position)
	 $StartTimer.start()
	 $HUD.update_score(score)
	 $HUD.show_message("Get Ready")
	 #$Music.play()


func _on_StartTimer_timeout():
	$MobTimer.start()
	$ScoreTimer.start()


func _on_ScoreTimer_timeout():
	score+=1
	$HUD.update_score(score)


func _on_MobTimer_timeout():
	$MobPath/MobSpawnLocation.set_offset(randi())
	var mob = Mob.instance()
	add_child(mob)
	var direction = $MobPath/MobSpawnLocation.rotation + PI/2
	mob.position = $MobPath/MobSpawnLocation.position
	direction += rand_range(- PI/4, PI/4)
	mob.rotation = direction
	mob.set_linear_velocity(Vector2(rand_range(mob.min_speed,mob.max_speed),0).rotated(direction))

func _exit_tree():
	 pomelo.disconnect()
