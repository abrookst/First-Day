
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

define z = Character("[z_name]", callback=z)
define h = Character("[h_name]", callback=h)
define t = Character("[t_name]", callback=t)
define s = Character("[s_name]", callback=s)
define c = Character("[c_name]", callback=c)
define r = Character("Robin", callback=r)


label start:


    "May 28th 201X, 11:18 P.M."

    scene bg bar
    
    "Birdley's Bar. A small dingey bar, kept afloat by its regulars, who have been coming here since before I was even born."

    "Said regulars are all within their cliques, or are glued to the telly, watching... something."

    "I sit and stir my Black Russian. Not in idle bordem, but rather in tense, sharp, anxiety."

    "My mind is racing, soaring through the air, beyond the wit of man."

    "My mind comes careening back down to reality, when the glass of solitude is shattered by a"

    z "Hey."

    show z front

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

    return