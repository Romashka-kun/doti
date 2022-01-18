define с = Character("Саша",color = "#c8ffc8")
define л = Character("Лена",color = "#c8ffc8")
define е = Character("Егор",color = "#c8ffc8")

#команды
transform s:
        alpha 0.0 xalign .5 yalign .52
        ease 2 alpha 1.0 yalign .50
        ease 2 alpha 0.0 yalign .48

#----------------------------------------------------------------------------------------------------------------------------------
label start:
  
  scene day1 with fade
  music in-his-room.ogg
  $ renpy.pause(3.3)
  scene room1 with fade
  $ pause_ = 4
  show text "Комната Саши" at s
  $ renpy.pause (pause_, hard=True)
