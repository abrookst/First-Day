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

define z = Character("[z_name]", callback=z, what_font="z.ttf", what_size=90)
define h = Character("[h_name]", callback=h, what_font="h.ttf")
define t = Character("[t_name]", callback=t, what_font="t.ttf")
define s = Character("[s_name]", callback=s, what_font="s.ttf")
define c = Character("[c_name]", callback=c, what_font="c.ttf")
define r = Character("Robin", callback=r)

default z_name = "????"
default h_name = "????"
default t_name = "????"
default s_name = "????"
default c_name = "????"

transform US_L:
    zoom 0.25 
    xalign .1
    yalign 1.0
transform US_C:
    zoom 0.25 
    xalign .5
    yalign 1.0
transform US_R:
    zoom 0.25 
    xalign 0.9
    yalign 1.0

transform S_L:
    zoom 0.5
    xalign .1
    yalign 1.0
transform S_C:
    zoom 0.5
    xalign .5
    yalign 1.0
transform S_R:
    zoom 0.5
    xalign 0.9
    yalign 1.0

transform DS_L:
    zoom 0.75
    xalign .1
    yalign 0
transform DS_C:
    zoom 0.75
    xalign .5
    yalign 0
transform DS_R:
    zoom 0.75
    xalign 0.9
    yalign 0
transform apron:
    zoom 1
    xalign .5
    yalign 0



label start:

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

    r "Oh, hey Zeke. Go ahead."

    $ z_name = "Zeke"

    show z back at S_C

    "He takes a seat, while gesturing at the waiter"

    show z side at S_C

    z "Two glasses of Dom P"

    r "Are you mad? How much even is that a glass?"#maybe sfx?

    r "Does this place even carry Dom P?"
    
    z "It doesnt really matter, after all..."

    show z front at S_C

    z "Doesn't {i}someone{/i} here have a job now?"

    z "And didn't {i}two{/i} people here just graduate from college?"

    show z side  at S_C

    z "So we should celebrate. Full stop."

    r "Please dont remind me."

    z "Remind you of what?"

    show z front at S_C

    "I bury my face into the table"

    r "Please dont remind me about my job."

    z "What?"

    "I hear two glasses and a bottle hit the table"

    z "How can you not like having a job? That makes literally no sense."

    r "I'm just... not a fan of change."

    r "I got used to college, and even moreso to school."

    r "This is just... different. And I really dont like that."

    show z side  at S_C

    z "To each their own, I guess."

    r "Exactly. Now can we stop talking about it and just drink?"

    z "Fair enough. Cheers."

    r "Cheers."

    show z back  at S_C

    "Our glasses tap, before we take a long sip of the Champage"

    r "Wow. This really is good."

    show z side  at S_C

    z "See? Worth every penny."

    r "Well I wouldnt say {i}that{/i}. A beer is just fine."

    z "We'll switch to beer after this, lets enjoy this while we're still sober."

    hide z with dissolve

    "The night went on long, we drank ceaselessly, while talking about our college memories."

    "Thinking about college was a nice respite from what was to come tomorrow."

    scene black
    with fade

    jump dayOne

label dayOne:
    #title here probably

    "..."

    "..."

    r "Ugh..."

    scene bg home
    with pixellate

    "I roll out of bed, falling onto the floor"

    r "Hmmmm... This isn't the worst hangover..."

    "I get up, rubbing my eyes, and start to get ready for work."

    "...Maybe drinking the night before my first day of work wasn't the best idea in the world."

    scene bg officeoutside:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with pixellate


    "After parking my car, I walk over to the front of the building. "

    "I'm well aware that this is just my own stress messing with me, but the atmosphere here..."

    "It just feels different. Otherworldly, almost."

    "I collect myself, straighten out my outfit, and walk into the front door."

    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    
    "Upon walking in, I am greeted by a lady sitting at the front desk."

    "She seems to be flipping through a magazine."

    show s front at S_C 
    with dissolve

    s "..."

    r "Ah, h-hello, my name's Robin. I was hoping to uh-"

    s "..."

    show s back at S_C

    "She picks up the landline phone beside her"

    s "Security? Some freakshow just came in and started talking to me."

    r "W-WAIT WHAT ARE YOU DOING?!"

    show s side at S_C

    s "..."

    show s back at S_C

    s "They seem to be getting aggressive..."

    r "I WORK HERE! THIS IS MY FIRST DAY!"

    "I rummage though my bag to grab my ID."

    "But before I can show it to her, someone comes in and grabs the phone from her hands."

    show s side at S_L
    with move

    show h back at S_C
    with dissolve

    h "Hello? This is Horace."

    $ h_name = "Horace"

    h "Shamir was lying. You don't have to come to the front desk."

    $ s_name = "Shamir"

    "They put the phone down into its cradle."

    hide s with dissolve
    show h front at DS_C
    with dissolve

    h "You must be Robin. Nice to meet you."

    r "Yes! I-It's great to meet you too, Horace."

    h "That's Boss to you."

    $ h_name = "Boss (Horace)"

    r "Ah, s-sorry boss."

    show h front at apron
    with dissolve

    "They step forward and extend their hand, and I reach to shake it."

    "But I instead grab something fuzzy and soft. I look down at my hand."

    h "I wasn't trying to shake your hand. This is a towel. You're sweating like mad."

    r "H-huh?"

    h "Come with me."

    hide h front
    with dissolve

    scene bg hallway:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    "They quickly move down the hallway, I wipe my face off with the towel while following them down the hall."

    "We wisk by endless offices and meeting rooms, only breifly slowing down to turn corners."

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    show h front at S_C
    with dissolve

    h "This is your office."

    r "G-Got it. Which of the two empty desks is mine?"

    show h side at S_C

    h "The one on the right. The left one belongs to the other person starting today."

    r "Oh? There's someone else starting with me?"

    show h back at S_C

    h "Yep. And speak of the devil."

    "Horace steps to the side, as a tall man walks in"

    show t front at S_L
    with dissolve
    show h front

    h "This is Taiga. He's the other employee starting today."

    $ t_name = "Taiga"

    t "Hi. And your name is?"

    r "Robin. Nice to meet you!"

    "I extend my hand towards Taiga"

    t "Yeah... no. I'm not shaking your hand."

    show t side

    t "Try not to get in my way, okay?"
    
    show t front

    t "You should be happy you even get to share an office with me."

    show t side

    t "Boss, I already finished all of my work for this morning."
    
    t "I'll be off to get a head start on this afternoon's work."

    h "Impressive, Taiga."

    show h side

    h "You should learn a thing or two from Taiga, Robin."

    t "Heh, even if Robin tried to be like me, they'd simply fall short."

    "...This is gonna be a long day."

    show t back

    t "I'll be off then."

    hide t back
    with dissolve

    "Taiga steps out of the room"

    show h front

    h "Anyways, it would absolutely tickle my dying heart pink to give you a tour, but unfortunately, I have better things to do."

    show h side

    h "Hey, Claire."

    show c front at S_R
    with dissolve

    c "Yes, Hori?"

    h "Don't call me that."

    show c side

    c "Ah, sorry..."

    h "Can you give Robin a tour?"

    show c front

    c "Oh! Sure, I can do that."

    show h back

    h "Alright. I'll be off then"

    hide h back
    with dissolve

    "Horace steps out."

    show c back

    c "Alright! Follow me!"


    






