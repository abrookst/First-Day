init python:

    #Generate seperate audio channel from voice for beeps.
    renpy.music.register_channel(name='beeps', mixer='voice')

    def z(event, **kwargs):
        if event == "begin": 
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def h(event, **kwargs):
        if event == "show": 
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")
    def t(event, **kwargs):
        if event == "show": 
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def s(event, **kwargs):
        if event == "show": 
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def c(event, **kwargs):
        if event == "show": 
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def r(event, **kwargs):
        if event == "begin": 
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

default z_name = "????"
default h_name = "????"
default t_name = "????"
default s_name = "????"
default c_name = "????"

define z = Character("[z_name]", callback=z, what_font="z.ttf")
define h = Character("[h_name]", callback=h, what_font="h.ttf")
define t = Character("[t_name]", callback=t, what_font="t.ttf")
define s = Character("[s_name]", callback=s, what_font="s.ttf")
define c = Character("[c_name]", callback=c, what_font="c.ttf")
define r = Character("Robin", callback=r)

define gui.text_font = "gui1.ttf"
define gui.interface_text_font = "gui2.ttf"
define gui.text_size = 20

transform US_R:
    zoom 0.25 
    xalign .1
    yalign 1.0
transform US_C:
    zoom 0.25 
    xalign .5
    yalign 1.0
transform US_L:
    zoom 0.25 
    xalign 0.9
    yalign 1.0
transform S_R:
    zoom 0.5
    xalign .1
    yalign 1.0
transform S_C:
    zoom 0.5
    xalign .5
    yalign 1.0
transform S_L:
    zoom 0.5
    xalign 0.9
    yalign 1.0
transform DS_R:
    zoom 0.75
    xalign .1
    yalign 0
transform DS_C:
    zoom 0.75
    xalign .5
    yalign 0
transform DS_L:
    zoom 0.75
    xalign 0.9
    yalign 0
transform apron:
    zoom 1
    xalign .5
    yalign 0


label start:

    scene bg office2:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x')
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
        
    show z front at S_C

    "May 28th 201X\n11:18 P.M.\nBirdley's Bar"

    scene bg bar
    with pixellate
    
    "A small dingey bar, kept afloat by its regulars, who have been coming here since before I was even born."

    "Said regulars are all within their cliques, or are glued to the telly, watching... something."

    "I sit and stir my Black Russian. Not in idle bordem, but rather in tense, sharp, anxiety."

    "My mind is racing, soaring through the air, beyond the wit of man."

    "My mind comes careening back down to reality, when the glass of solitude is shattered by a"

    z "Hey."

    show z front at S_C
    

    z "Mind if I have a seat?"

    r "Oh, sure."

    show z back

    "He takes a seat, while gesturing at the waiter"

    show z side

    z "Get the Pappy from the back."

    r "Are you mad? How much even is that a glass?"#maybe sfx?
    
    z "It doesnt really matter, after all..."

    show z front 

    z "Doesn't {i}someone{/i} here have a job now?"

    z "And didn't {i}two{/i} people here just graduate from college?"

    show z side

    z "So we should celebrate. Full stop."

    r "Please dont remind me."

    z "Remind you of what? That you graduated and got a job?"

    "I bury my face into the table"

    r "Please dont remind me."

    z "How can you not like having a job? That makes no sense."

    r "I'm just... not a fan of change."

    r "I got used to college, and even moreso to school."

    r "This is just... different. And I really dont like that."

    z "To each their own, I guess."

    r "Exactly. Now can we stop talking about it and just drink?"

    z "Fair enough. Cheers."

    r "Cheers."

    scene
    with fade

    jump dayOne

label dayOne:
    "..."

