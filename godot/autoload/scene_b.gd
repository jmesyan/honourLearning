extends Panel

# Class member variables go here, for example:
# var a = 2
# var b = "textvar"

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here.
	pass

func _on_goto_scene_pressed():
	get_node("/root/global").goto_scene("res://scene_a.tscn")
