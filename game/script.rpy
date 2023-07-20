init python:

    #Generate seperate audio channel from voice for beeps.
    renpy.music.register_channel(name='beeps', mixer='voice')

    def z(event, **kwargs):
        if event == "begin": 
            build_sentence(_last_say_what, "zeke")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def h(event, **kwargs):
        if event == "show": 
            build_sentence(_last_say_what, "horace")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")
    def t(event, **kwargs):
        if event == "show": 
            build_sentence(_last_say_what, "taiga")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def s(event, **kwargs):
        if event == "show": 
            build_sentence(_last_say_what, "shamir")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def c(event, **kwargs):
        if event == "show": 
            build_sentence(_last_say_what, "claire")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def r(event, **kwargs):
        if event == "begin": 
            build_sentence(_last_say_what, "robin")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

define z = Character("[z_name]", callback=z, what_font="z.ttf", what_size=40)
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

default h_count = 1
default t_count = 1
default s_count = 1
default c_count = 1
default day = 1
default todayTalk = ""
default bShamir = True;

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
    with fade
    play music "music/bar.wav" fadein 1.0
    
    "A small dingey bar, kept afloat by its regulars, who have been coming here since before I was even born."

    "Said regulars are all within their cliques, or are glued to the telly, watching... something."

    "I sit and stir my Black Russian. Not in idle bordem, but rather in tense, sharp, anxiety."

    "My mind is racing, soaring through the air, beyond the wit of man."

    "My mind comes careening back down to reality, when the glass of solitude is shattered by a familiar voice."

    z "Hey."

    show z front at S_C
    with dissolve

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

    z "Doesn't {bt}someone{/bt} here have a job now?"

    z "And didn't {bt}two{/bt} people here just graduate from college?"

    show z side  at S_C

    z "So we should celebrate. Full stop."

    r "Please dont remind me."

    z "Remind you of what?"

    show z front at S_C

    "I bury my face into the table"

    r "{sc}Please dont remind me about my job.{/sc}"

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

    stop music fadeout 1.0
    scene black
    with fade
    

    jump dayOne_morning

label dayOne_morning:

    "..."

    "..."

    r "Ugh..."

    scene bg home
    with fade
    play music "music/home (Morning).wav" fadein 1.0

    "I roll out of bed, falling onto the floor"

    "I pick myself up, while rubbing my eyes."

    "Dread strikes as I slowly realize that today"

    "...is the first day of my new life."

    stop music fadeout 1.0
    scene bg officeoutside:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with pixellate
    play music "music/Sludge (Office outside morning).wav" fadein 1.0


    "After parking my car, I walk over to the front of the building. "

    "I'm well aware that this is just my own stress messing with me, but the atmosphere here..."

    "It just feels different. Otherworldly, almost."

    "I collect myself, straighten out my outfit, and walk into the front door."

    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Glop (Front Desk morning).wav" fadein 1.0

    "Upon walking in, I am greeted by a lady sitting at the front desk."

    "She seems to be flipping through a magazine."

    show s front at S_C 
    with dissolve

    s "..."

    r "Hello, my name is Robin."

    s "..."

    show s back at S_C

    "She picks up the landline phone beside her"

    s "Security? Some freakshow just came in and started talking to me."

    r "{sc}WHAT ARE YOU DOING?!{/sc}"

    show s side at S_C

    s "..."

    show s back at S_C

    s "They seem to be getting aggressive..."

    r "{sc}I WORK HERE! THIS IS MY FIRST DAY!{/sc}"

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
    
    show h front

    h "Sorry about that. You must be Robin."
    
    h "Nice to meet you."

    r "Yes! I-It's great to meet you too, Horace."

    h "That's Boss to you."

    $ h_name = "Boss (Horace)"

    r "Ah, s-sorry boss."

    show h side

    h "By the way, the lady who just tried to get you kicked out was Shamir."

    show h front

    h "She's our HR lady. So please get along."

    r "HR? Why are you at the front desk?"

    s "Budget cuts."

    "I-I see..."

    h "Here, Robin."

    hide s with dissolve
    show h front at apron
    with dissolve

    "Horace steps forward and extends their hand, and I reach to shake it."

    "But I instead grab something fuzzy and soft. I look down at my hand."

    h "I wasn't trying to shake your hand. This is a towel. You're sweating like mad."

    r "H-huh?"

    show h side

    h "I can understand. You must be nervous about your first day."

    h "Let me put all doubts to rest for you, Robin."

    h "Whatever you're imagining your work will be like..."

    show h front

    h "{sc}It's worse.{/sc}"

    h "{sc}...{/sc}"

    h "Come with me."

    hide h front
    with dissolve

    scene bg hallway:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    "Horace quickly moves down the hallway, I wipe my face off with the towel while following them down the hall."

    "We wisk by endless offices and meeting rooms, only breifly slowing down to turn corners."

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Morning).wav" fadein 1.0

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

    $ c_name = "Claire"

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

    scene bg hallway:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    show c back at S_C

    c "Where have you been so far?"

    r "Besides the front desk and the office, nowhere else."

    c "Got it. I'll show you the cafeteria and the way to Hori's office"

    r "Mind if I ask why do you call Horace Hori?"

    c "..."

    r "..."

    "The air grew unusually thick."

    stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/gloop (Cafe).wav" fadein 1.0

    show c front at  DS_C

    c "H-Here's the cafe!"

    r "Wow! This place looks really nice!"

    c "Right? Wanna know what the best part is?"

    r "Oh? What's that?"

    show c side

    c "There are cameras around that scan everything you eat and drink..."

    show c front

    c "And they automatically deduct the price of what you ate from your salary!"

    c "Isn't the information age just the best!?"

    r "Yeah... the best! Hahaha!"

    c "Welp! Next is your boss' office."


    c "If all goes well, you'll never have to set foot in there again."

    show c back

    c "And that's a very big if, mind you."

    "{sc}Gulp...{/sc}"

    stop music fadeout 1.0
    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Grime (Boss).wav" fadein 1.0

    show c front at S_L
    with move

    c "And here we are! Hi Horace!"

    show h front at S_C
    with dissolve

    h "What are you two doing here."

    show c side

    c "We're on the tour, Robin has to know where their boss' office is!"

    h "I see. Robin, how is your first day so far?"

    r "Oh, not that bad, actually..."

    show h back

    h "That's very unfortunate. I'll assign you some extra morning work to help rectify this issue."

    show h side

    h "Did you need anything else?"

    r "N-No... Not really..."

    show h front at DS_C

    h "Then get out. The tour is over."

    "Horace shoves both Claire and I out of the office."

    scene bg hallway:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    r "Oof!"

    "SLAM" #sfx here maybe?

    show c side at S_C

    c "Welp! Guess the tour is over then!"

    show c front

    c "Let's head back to our desks and get to work."

    hide c with dissolve

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Morning).wav" fadein 1.0

    "I plop down into my chair and face my computer."

    "...It seems like Horace has already given me a lot of things to do."

    "Welp, time to get to it..."

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    r "Phew... finally lunch time."

    "I could get to know my coworkers better if I talked to them during lunch..."

    menu:
        "Who should I try and talk to?"

        "Taiga":
            jump taiga
        "Claire":
            jump claire
        "Horace":
            jump horace
        "Shamir":
            jump shamir 
label dayOne_afternoon:

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0
    

    r "test"

    r "test 2"

    r "this is day 1 afternoon"

    return

label dayTwo_morning:
label dayTwo_afternoon:

label dayThree_morning:
label dayThree_afternoon:

label dayFour_morning:
label dayFour_afternoon:

label dayFive_morning:
label dayFive_afternoon:

label taiga:
    if t_count == 1:
        jump taiga1
    elif t_count == 2:
        jump taiga2
    elif t_count == 3:
        jump taiga3
    elif t_count == 4:
        jump taiga4
    elif t_count == 5:
        jump taiga5
    elif t_count == 6:
        jump taigaEnding
    else:
        python:
            renpy.error("Invalid taiga link!")
label horace:
    if t_count == 1:
        jump horace1
    elif t_count == 2:
        jump horace2
    elif t_count == 3:
        jump horace3
    elif t_count == 4:
        jump horace4
    elif t_count == 5:
        jump horace5
    elif t_count == 6:
        jump horaceEnding
    else:
        python:
            renpy.error("Invalid horace link!")
label shamir:
    if t_count == 1:
        jump shamir1
    elif t_count == 2:
        jump shamir2
    elif t_count == 3:
        jump shamir3
    elif t_count == 4:
        jump shamir4
    elif t_count == 5:
        if bShamir:
            jump shamir5A
        else:
            jump shamir5B
    elif t_count == 6:
        if bShamir:
            jump shamirEndingA
        else:
            jump shamirEndingB
    else:
        python:
            renpy.error("Invalid shamir link!")
label claire:
    if t_count == 1:
        jump claire1
    elif t_count == 2:
        jump claire2
    elif t_count == 3:
        jump claire3
    elif t_count == 4:
        jump claire4
    elif t_count == 5:
        jump claire5
    elif t_count == 6:
        jump claireEnding
    else:
        python:
            renpy.error("Invalid claire link!")

label returnToDay:
    if day == 1:
        jump dayOne_afternoon
    elif day == 2:
        jump dayTwo_afternoon
    elif day == 3:
        jump dayThree_afternoon
    elif day == 4:
        jump dayFour_afternoon
    elif day == 5:
        jump dayFive_afternoon
    else:
        python:
            renpy.error("Invalid day!")

    return

label taiga1:
    #Talking to Taiga after working in the morning
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    r "Phew. That's this morning's work done and dusted!"

    r "How are you holding up, Taiga?"

    show t side at S_C
    with dissolve

    t "..."

    show t front

    t "Hmph, what do you think? I did all my work flawlessly an hour ago."

    r "Figures."

    r "Hey, by the way, where did you go to college?"

    t "I got a scholarship to Flitington, how about you?"

    r "{sc}Flitington?{/sc}"

    r "W-Wow, I've never met someone who went to Flitington."

    show t side

    t "Naturally, we're the best of the best."

    r "I went to Blighty U, I had a great time there."

    t "Heh, Blighty? That preschool?"

    t "I'm shocked you even know how to use a computer."

    "Ugh... that's a low blow."

    r "A-Anyways Taiga, wanna go get lunch together?"

    show t back

    t "Nope. See you."

    hide t back 
    with dissolve

    "Taiga walks out"

    "..."

    r "Welp. Guess I'll be eating lunch alone..."

    show t front at S_C
    with dissolve

    t "..."

    r "Taiga?"

    t "I'll be nice and let you eat lunch with me this once."

    r "Huh? Why the sudden change of heart."

    show t side

    t "As coworkers, we should be able to work together well."

    show t front

    t "If you know more about me, you'll be able to bolster me up higher."

    t "And..."

    show t back

    t "..."

    t "The reason isn't important. Let's go to the cafe."

    "{bt}You got a little closer to Taiga today.{/bt}"

    $ t_count+=1
    $ todayTalk = "Taiga"

    jump returnToDay
label taiga2:
    #Lunch with Taiga, says he has no interests
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    r "Hey Taiga, wanna go get lunch again?"

    show t side at S_C
    with dissolve

    r "To uh, bolster your status higher or whatever?"

    show t front

    t "Fine. Lets go."

    stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/gloop (Cafe).wav" fadein 1.0

    show t side at apron
    with dissolve

    t "..."

    r "..."

    r "S-So Taiga, do you have any interests... besides work?"

    show t front

    t "None. Next question."

    r "Huh? You really don't do anything besides work?"

    show t front

    t "Nope."

    r "Wow, that's sounds like a really sad life."

    t "If I wanted to know what a sad life was like, I'd ask you."

    r "Very funny, Taiga."

    t "I wasn't being funny."

    "...ah"

    r "So wait, what do you do once you get off of work?"

    t "I usually work out."

    r "Ah! See? That's something! You like working out"

    show t side

    t "Working out isn't something I enjoy."

    t "It's something I do to stay in peak mental and physical fitness."

    show t front

    t "Same with my piano playing and cooking."

    t "I play the piano to excercise my mind."
    
    t "And I cook my own meals after workouts to maximize the benefits."

    show t side

    t "And speaking of cooking, if you wanna be more like me Robin..."

    r "Hm?"

    show t front

    t "You should lay off the fast food."

    "I sheepishly put down the burger I was about to shove into my mouth."

    r "Well... that's a very interesting way to lead your life."

    r "Do you derrive joy from anything, Taiga"

    show t side

    t "..."

    show t front

    t "Crushing the opposition."

    "{sc}Gulp...{/sc}"

    t "I used to enjoy some things when I was a little kid..."

    show t side

    t "But I'm an adult now, and my parents taught me how to focus on what matters in life."

    r "..."

    show t front

    t "We should probably get going."

    r "Ah, you're right."

    hide t front
    with dissolve

    t "I'll be seeing you."

    "{bt}You got a little closer to Taiga today.{/bt}"

    $ t_count+=1
    $ todayTalk = "Taiga"

    jump returnToDay
label taiga3:
    #Talking to Taiga and being interrupted by Shamir about art
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    r "Hey Taiga, lunch again?"

    show t front at S_C
    with dissolve

    t "My, aren't you persistent."

    show t back

    t "Fine, let's-"

    show s front at S_C
    with dissolve
    show t side at S_L
    with move

    s "Excuse me."

    r "Shamir, what are you doing here?"

    if s_count > 2:
        show s side
        s "I'm here to talk about art again."
    else:
        s "Robin. Can I ask you an art question?"

        r "Huh? You like art?"

        s "...Yes"

        r "Why me?"

        show s side

        s "You seem like you would have an eye for it. No other reason, really."

    r "Well, what did you wanna talk about?"

    s "I recently found this piece in my closet."

    s "I have no room for it, would you like to keep it?"

    r "Ooh! Mind if I see?"

    show s front

    s "Here you go."

    r "Oh wow! This is beautiful."

    s "Hm? Taiga?"

    show t back

    r "Hm? Is something wrong Taiga?"

    s "Taiga..."

    show s side

    s "Are you crying?"

    show t front

    t "{sc}!!!{/sc}"

    hide t front

    "Taiga bolted out of the room."

    r "{sc}TAIGA!{/sc}"

    s "Woah, what's up with the egomaniac?"

    r "I-I'll go after him!"

    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Glop (Front Desk afternoon).wav" fadein 1.0

    r "Taiga! Wait!"

    show t back at S_C

    t "...What is it?"

    r "What happened there? You just sprinted off!"

    t "..."

    r "Do you wanna talk about it?"

    show t front

    t "Next time you're free at lunch..."

    show t side

    t "Bring that painting, please."

    show t front

    t "And don't tell anyone about this."

    r "S-Sure..."

    show t back

    t "I'm heading home for the day."

    hide t back
    with dissolve

    t "Bye."

    "{bt}You got a little closer to Taiga today.{/bt}"

    $ t_count+=1
    $ todayTalk = "Taiga"

    jump returnToDay
label taiga4:
    #Talking to Taiga about art
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    r "H-Hey Taiga, I'm free today..."

    show t front at S_C
    with dissolve

    t "..."

    show t back

    t "Come with me."

    stop music fadeout 1.0
    scene bg officeoutside:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    show t front at DS_C
    with dissolve

    t "Did you bring it?"

    r "Yeah, here's the painting."
    
    show t back

    t "..."

    r "Taiga? Mind telling me whats up?"

    show t front

    t "..."

    show t side

    t "Remember when I said I used to love something when I was a kid..."

    show t front

    t "And my parents taught me better?"

    r "Mhm."

    t "That was art."

    t "I used to... want to be an artist."

    r "I-I see..."

    t "Didn't expect that, huh?"

    show t side

    t "Neither did my parents."

    t "\"Art doesn't make money\" they said."

    t "Every time I would make art, in any way, shape, or form."

    t "They would strip it away from me, and send me up to my room to do another sheet of math problems."

    t "Eventually, I gave up."

    t "And eventually... I started to become someone I wasn't."

    show t front

    t "When I got into Flitington, it was town news."

    t "\"Did you hear Taiga got into Flitington? A full ride too.\""

    t "\"He must be so..."

    show t side

    t "...Happy\""

    "..."

    t "When I saw that painting. I remembered."

    t "I had nearly forgotten."

    t "How much making art, seeing art, and just... loving art gave me unbridled joy."

    "..."

    show t front

    t "Well. Now you know."

    t "Feel free to mock me when I'm not looking."

    t "I'll be going \"back to normal\" after this."

    t "I'm scared to do anything else but go back to normal."

    t "And I suggest you do the same with me. Horace would probably notice."

    t "Thanks for listening."

    show t back

    t "Goodbye, Robin."

    hide t back
    with dissolve

    "..."

    "{bt}You got a little closer to Taiga today.{/bt}"

    $ t_count+=1
    $ todayTalk = "Taiga"

    jump returnToDay
label taiga5:
    #Seeing the real Taiga and setting up ending
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    r "Hey, Taiga."

    show t back at S_C
    with dissolve

    t "..."

    r "Taiga."

    t "..."

    r "Ugh... just... come with me you mope."

    show t side

    t "Fine."

    stop music fadeout 1.0
    scene bg officeoutside:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Sludge (Office outside afternoon).wav" fadein 1.0

    show t side at DS_C
    with dissolve

    t "What do you want."

    r "Here."

    show t front

    t "What's this?"

    r "Two tickets for an art gallery, this Saturday."

    t "{sc}WHAT?!?!?!{/sc}" 

    r "Woah! Calm down there Taiga."

    t "..."

    r "Taiga. You need to stop shelling yourself up like this."

    r "You aren't your parents. You have the right to do what you enjoy."

    r "Even if its just off hours."

    show t back

    r "So we're going to the art gallery this weekend, okay?"

    hide t front
    with dissolve

    t "Fine."

    "..."

    "{bt}You got a little closer to Taiga today.{/bt}"

    $ t_count+=1
    $ todayTalk = "Taiga"

    jump returnToDay
label taigaEnding:
    #Going with taiga to art studio


label claire1:
    #Getting help from Claire and talking about work

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    "Ack, wait. I still need to get this done."

    "And I have no clue how to do this..."

    "Maybe I should ask Claire?"

    r "Hey, Claire?"

    show c front at S_C
    with dissolve

    c "What's up?"

    r "Mind helping me out with this?"

    r "I have no clue how to do this, to be perfectly honest with you."

    c "Sure! Lemme see what you got"

    show c side at DS_C

    "Claire takes a look at my computer."

    c "Ooooh... One of these, here, let me show you how to do this."

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    r "I see! Wow, thank you so much Claire!"

    show c front at S_C 

    c "No problem, Robin!"

    c "It really is quite easy once it gets explained to you."

    r "It really is..."

    c "But I'm glad I could help, and you can call me anytime you need a hand."

    r "Thanks Claire!"

    r "You're probably the nicest person here, hands down."

    "And probably the most normal..."

    c "Aww, thanks! I know how nice it is to get help you need, so why not pay it forward?"

    r "Those are words to live by, for sure!"

    show c side

    c "Anyways, it's about high time we got to lunch, right?"

    r "Right! Would you like to go get lunch together?"

    show c front

    c "Sounds good!"

    show c back

    c "Let's go eat, I'm starving!"
    
    "{bt}You got a little closer to Claire today.{/bt}"
    $ c_count+=1
    $ todayTalk = "Claire"

    jump returnToDay
label claire2:
    #Talking to Claire about food over lunch
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    r "Hey, Claire, wanna go get lunch again today?"

    show c front at S_C
    with dissolve

    c "Sure! Let's head over!"

    stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/gloop (Cafe).wav" fadein 1.0

    show c front at DS_C
    with dissolve

    c "Alright, time to eat!"

    "We start to dig into our food."

    r "So Claire, when did you start working here?"

    c "Oh... about 6 or so years ago?"

    r "Congrats on 6 years, then!"

    r "You plan on staying here for a while longer?"

    c "Yeah... probably. I've got a lot of... ties here."

    r "I see... That does come with a lot of benefits!"

    r "You'll probably get a promotion, if you havent already."

    show c side

    c "Yeah... A promotion..."

    r "Is something the matter?"

    c "Nah, don't worry about it."

    show c front

    c "Actually I have a question for you."

    r "Hm? What's up?"

    show c front at apron
    with dissolve

    "Claire leans forward"

    c "This is an extremely important question."

    r "Wh-What is it?"

    c "What's your favorite food?"

    r "...huh"

    c "What's your favorite food?"

    r "Y-Yeah I heard you I just, wasn't expecting that."

    c "{sc}It's an extremely important question.{/sc}"

    menu:
        r "L-Lemme think... My favorite food is..."

        "Hambugers":
            r "Probably hamburgers, can never beat a good smashburger."
            pass
        "Chilaquiles":
            r "Probably Chilaquiles, but only my dad's recepie, for sure."
            pass
        "Moules-Frites":
            r "Definitely Moules-Frites, an unexpectedly fantastic combo."
            pass
        "Maafe":
            r "A long simmered Maafe with a pile of rice can't be beat."
            pass
        "Shawarma":
            r "Shawarma, for sure. I could probably eat the meat off the spit."
            pass
        "Chana Masala":
            r "Ooh... gotta be Chana Masala. Especially with some extra spice."
            pass
        "Tteokbokki":
            r "Tteokbokki. For sure, it's so easy to make, but so delicious."
            pass

    c "I see! A really great choice."

    show c side at DS_C
    with dissolve

    c "Mine is probably... Steak!"

    r "I see! That's also a great choice, you can never go wrong with steak."

    c "Can you see how someone's favorite food says a lot about them?"

    r 'I... kinda see what you mean!'

    r "I have a good college friend, his name is Zeke, and I remember how much my perception of him changed when he said his favorite food was mashed potatos."

    c "Riiight? Glad you see what I mean."

    c "Anyways, it's about high time we got back, don't you think?"

    r "Yep, let's head over then!"

    "{bt}You got a little closer to Claire today.{/bt}"
    $ c_count+=1
    $ todayTalk = "Claire"

    jump returnToDay
label claire3:
    #Getting help and getting walked in by Horace
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    "Ugh... wait... I'm getting this weird issue on my e-mail app... What's going on?"

    "Before I go to lunch, I should probably get this sorted out, e-mails are way too important..."

    r "Uh... Claire? Mind if I ask for a little more help?"

    show c front at S_C
    with dissolve

    c "Sure! What's up?"

    r "My e-mail app is acting up, I have no clue what's wrong..."

    c "I haven't seen this before... Let me take a closer look."

    show c side at S_L
    with move

    show h front at s_count
    with dissolve

    "Seemingly from the shadows, Horace steps in."

    h "Let me have a look."

    "..."

    show h back

    h "Done. I'll be going then."

    show c front

    c "Hori! You're gonna stop by without saying hi, darling?"

    h "..."

    h "Why are you still clinging on, Claire?"

    show h front

    h "...Isn't it about time you let go?"

    c "!" #sfx here maybe?

    show h side

    h "Ill be seeing you Robin."

    show h back 

    h "Goodbye, Claire. And I don't want to say that again."

    hide h back
    with dissolve

    "..."

    r "...Claire?"

    show c back

    c "I'll um..."

    c "I'll talk about it later."

    c "N-Next lunch, okay?"

    c "A-And don't worry about me, I'm fine!"

    hide h back
    with dissolve

    c "S-See you!"

    "..."

    "{bt}You got a little closer to Claire today.{/bt}"
    $ c_count+=1
    $ todayTalk = "Claire"

    jump returnToDay
label claire4:
    #Learning about Claire and Horace
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    show c front at DS_C 
    with dissolve

    c "Hey, Robin?"

    r "What's up, Claire?"

    c "Remember what happened last time, with Horace?"

    r "Ah, y-yeah..."

    c "Mind if I vent to you about that? I kinda want to get it all off my chest."

    r "Oh, sure! W-Wanna go to the cafeteria?"

    c "That would be fantastic."

    stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    show c front at apron
    with dissolve

    r "So what did you want to vent about."

    c "Alright, so..."

    show c side

    c "..ugh, for once I'm at a loss for words."

    show c front

    c "Let's just start at the beginning. Me and Horace started on the same day."

    c "We were desk to desk, and obviously ended up talking a lot."

    c "Eventually, we started hanging out outside of work."

    show c side

    c "And, y'know... One thing led to another... and we started dating."

    c "..."

    show c front

    c "But one day, Horace came to my place, right after work."

    c "And something seemed off, they weren't their usual self."

    c "They told me that we had to break up, and before I could even respond..."

    c "Horace said \"Goodbye, Claire\" before leaving."

    r "I'm so sorry to hear that Claire..."

    show c side

    c "And I was oblivious to it until then but..."

    c "There's something strange going on here, and I can't quite put my finger on it."

    "..."

    c "I really do loathe this job. Nothing here sits right with me, even from the start."

    c "I've always wanted to quit, but I just can't give up Horace."

    c "And there's no need to tell me that staying at a job I hate for unrequited love is dumb."

    show c front

    c "I've head that one enough from my mom."

    show c side

    c "Anyways, it's about high time we left. Sorry for dumping that all on you."

    r "Y-You're all good! I'm glad I was able to help you get that off your chest!"

    c "Yeah... It was really nice telling someone all of that..."
    
    c "Thanks, Robin."

    "..."

    "{bt}You got a little closer to Claire today.{/bt}"
    $ c_count+=1
    $ todayTalk = "Claire"

    jump returnToDay
label claire5:
    #Wrap up, talking about work and life, set up ending
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    show c front at S_C
    with dissolve

    c "Hey, Robin! Down for lunch again today?"

    r "Sure! Let's go!"

    stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/gloop (Cafe).wav" fadein 1.0

    show c front at DS_C
    with dissolve

    c "Y'know, I'm feeling a lot better after our talk last time."

    r "I'm glad to hear it, Claire!"

    c "By the way, would you wanna meet up sometime this weekend?"

    c "We could celebrate your first week of work!"

    "W-Wow, I didnt even realize it's been a week..."

    r "That sounds good! Do you have a place in mind?"

    c "Ever heard of a bar called Birdley's?"

    r "Oh yeah! I love Birdley's, I'm a regular myself!"

    c "Oh really? Well then, it's set!"

    r "Sounds great!"

    c "Now, I'm sorry to cut our little lunch short, but I've got somewhere to be."

    r "Really? Where?"

    c "Oh, I just have a lunch meeting. I'll see you around the office later."

    r "Alright, I'll see you!"

    show c back

    c "See you!"

    hide c back

    "..."

    "{bt}You got a little closer to Claire today.{/bt}"
    $ c_count+=1
    $ todayTalk = "Claire"

    jump returnToDay
label claireEnding:
    #Chatting at bar says she might leave


label horace1:
    #Talking in their office
    stop music fadeout 1.0
    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Grime (Boss).wav" fadein 1.0

    show h front at S_C
    with dissolve

    h "..."

    r "..."

    h "Why are you here."

    r "Oh! I-It's lunch, and I wanted to talk to you."

    show h back

    h "Well, you talked to me. I'll be leaving now."

    r "{sc}W-WAIT!{/sc}"

    show h side

    h "What is it."

    r "U-Uh, building a strong co-worker relationship is important to a strong company..?"

    h "..."

    show h front

    h "Do you have a source for that?"

    r "N-No but... Let's just try and talk, okay?"

    h "... Fine."

    r "How was your day?"

    show h side

    h "Efficient yet suffocatingly bland with a tinge of abject misery and horror."

    h "Just like the last 10,227 days of my agonizing existance."

    show h front

    h "...How about you..?"

    "..."

    "..."

    "I'm stunned... I can't... say anything..."

    show h side

    h "You're not very good at this talking thing. Hopefully that isnt on your CV."

    h "Though. I do seem to understand you a bit better."

    show h front

    h "This was a good idea. Thanks, Robin."

    show h back

    h "I'll actually be going now."

    hide h back
    with dissolve

    h "Bye."

    "..."

    "..."

    "...is this what death feels like?"

    "{bt}You got a little closer to Horace today.{/bt}"
    $ h_count+=1
    $ todayTalk = "Horace"

    jump returnToDay
label horace2:
    #Talking over lunch 
    stop music fadeout 1.0
    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Grime (Boss).wav" fadein 1.0

    r "{sc}BOSS!{/sc}"

    show h front at S_C
    with dissolve

    h "Hm?"

    r "I-I'm ready to try talking again!"

    h "Sure. Does lunch sound good?"

    r "Yes! That sounds great!"

    h "Then let's head out."

    stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/gloop (Cafe).wav" fadein 1.0

    show h front at DS_C

    "..."

    "..."

    r "So... Boss... Are you gonna get any food? You just have a cup of coffee."

    h "No. I woln't."

    r "Well uh, what's your favorite food then?"

    h "It's coffee."

    if c_count > 2:
        "W-Wow, Claire was right. Favorite food does say a lot about a person..."

    r "So, Boss, what are your favorite things to do? What's your passion?"

    h "Probably laying off employees. Either that or writing e-mails."

    r "S-So you like writing?"

    show h side

    h "I suppose, just e-mails, however."

    r "Have you tried writing anything else besides e-mails?"

    show h front

    h "No. I can't really see a reason why you would write for any other reason than for a work context."

    show h side

    h "Spending hours and hours of time outside of work to write a bunch of made up characters just sounds like a waste of time."

    "Touche..."

    r "Well... just give it a try!"

    show h front

    h "...Fine."

    "I'm really shocked at how many times Horace has said yes to something I've suggested..."

    h "I'll report back to you next time we have some free time about my findings."

    show h back

    h "I'll have to cut our meeting short. I have something a bit more pressing."

    r "Ah, got it! I'll see you then."

    hide h back
    with dissolve

    h "Yeah... I'll see you."

    "..."

    "{bt}You got a little closer to Horace today.{/bt}"
    $ h_count+=1
    $ todayTalk = "Horace"

    jump returnToDay
label horace3:
    #Talking but Claire pushes plot forward
    stop music fadeout 1.0
    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Grime (Boss).wav" fadein 1.0

    r "Hey Boss!"

    show h front at S_C
    with dissolve

    h "Hello Robin. My findings are finished."

    r "Woah, you really went and wrote something?"

    h "Yes. Here. Have a look."

    r "Let me see..."

    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    "..."

    "..."

    "...This is awful."

    "I have never seen such spectacularly bad writing."

    h "Are you finished?"

    r "Y-Yeah..."

    show h front at DS_C
    with dissolve

    h "Now it is time for the user feedback. What did you think of this?"

    menu:
        "Urk... What do I say?"

        "It was fantastic":
            r "T-This is fantastic, Boss!"
            r "I was enraptured all the way through, excelent work."
            pass
        "It was okay":
            r "This was pretty alright, Boss."
            r "I think it could use a bit of... work..."
            r "But this is a great start!"
            pass
        "It was awful":
            r "I'm not gonna mince words with you, Boss."
            r "This was truly awful."
            r "You know you don't need to end every character dialouge with \"Sincerely, Horace\" right?"
            r "And why did everyone get fired at the end? None of them even worked at a company...??"
            r "You've got a long way to go."
            pass

    h "...I see. I will add this feedback to my report."

    show t front at S_C
    with dissolve

    c "Hey Boss. What's this?"

    "Horace slams the laptop shut"

    show h back

    h "This is a private buisness afair. Please leave, Taiga."

    show h front

    c "Ah. G-Got it, Boss."

    show t back

    c "See you..."

    hide c back

    "..."

    r "H-Hey Boss..."

    r "Why do you usually... push people away?"

    h "..."

    r "You've warmed up to me a little bit, but we don't even know what Taiga came in for. And yet you-"

    h "This is irrelevant."

    h "I'll have to ask you to leave too."

    r "Ah, alright."

    r "See you then."

    "..."

    "{bt}You got a little closer to Horace today.{/bt}"
    $ h_count+=1
    $ todayTalk = "Horace"

    jump returnToDay
label horace4:
    #Backstory dump (basically)
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    "Phew. Time to get to lunch, finally."

    show h front at DS_C
    with dissolve

    h "Robin."

    r "{sc}ACK{/sc}"

    r "B-Boss! Wh-What's up?"

    show h back

    h "Need you in my office in 5."

    hide h back
    with dissolve

    h "Bye."

    "Guess I'll get over there..."
    stop music fadeout 1.0
    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    show h front at DS_C
    with dissolve

    h "Thank you for coming, Robin."

    r "What did you need, Boss?"

    show h side

    h "I want to talk to you about something."

    r "W-What's up?"

    h "Just a bit about my past."

    show h front

    h "You see. When I first came here, I was much more open to people."

    h "I had befriended a majority of the office, and had even started seeing someone."

    "...I honestly can't imagine that."

    show h side

    h "But my work suffered as a result. I was all play and no work."

    h "And one day. My Boss came to me with a ultimatum."

    h "Either focus on my work wholly, and gain a large promotion"

    h "...or get laid off."

    h "He saw potential in me, and knew that this potential would not be drawn out in my current state."

    show h front

    h "As you can see, I've made my choice."

    h "Additionally, I am currently caring for a lot of people."

    h "I am the \"breadwinner\" so to speak."

    r "So if you got laid off..."

    h "Yes. We would have starved."
    
    h "That is why I keep nobody close."

    show h side

    h "This is why I would also like to say one additonal thing"
    
    h "I have decided that these lunch excursions will cease henceforth."

    h "I hope you understand."

    r "Wait, but-"

    show h front

    h "Sorry, Robin, Boss' orders."

    h "Now I will have to ask you to leave."

    "..."
    
    "{bt}You got a little closer to Horace today.{/bt}"
    $ h_count+=1
    $ todayTalk = "Horace"

    jump returnToDay
label horace5:
    #Chat and setup for ending
    stop music fadeout 1.0
    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Grime (Boss).wav" fadein 1.0

    "..."

    show h front at S_C
    with dissolve

    h "Was I not clear yesterday?"

    r "No, you were very clear, as usual."

    r "I'm here as an employee to ask you one thing."
    
    r "Consider it an HR request."

    show h side

    h "Did you take this up with Shamir?"

    r "Y-Yeah..."

    h "Well then..."

    show h front

    h "What is it?"

    r "I belive you need to have a better work life balance."

    h "...What?"

    r "You need to learn to balance your life and work more!"

    r "Do stuff outside of work! Talk to your coworkers! Pick up a hobby!"

    h "...Robin, do you know what a work life balance is?"

    r "{sc}n-no...{/sc} But that's besides the point!"

    r "Horace, I can tell, this is hurting you."

    h "!"

    r "You woln't last much longer shutting yourself away like this."

    r "And if you wanna keep working, then you gotta do whats best for you."

    r "You gotta open up a bit more!"

    h "..."

    r "..."

    h "..."

    "Ugh! This feels like when we first talked at lunch! This silence is killing me."

    h "Birdley's."

    r "Huh..?"

    h "Saturday, Birdley's."

    r "W-Wait I-"

    show h back

    h "Speak of this to nobody."

    hide h back
    with dissolve

    h "Bye."

    r "..."

    r "D-Did Horace just ask me to hang out this weekend?"

    "..."

    "{bt}You got a little closer to Horace today.{/bt}"
    $ h_count+=1
    $ todayTalk = "Horace"

    jump returnToDay
label horaceEnding:
    #Chat and talk about how your work has been so far and how they’ve changed


label shamir1:
    #Talking to Shamir about day one incident
    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Glop (Front Desk afternoon).wav" fadein 1.0

    r "Hey Shamir!"

    show s front at S_C
    with dissolve

    s "..."

    s "Hey, Robin."

    r "Wanna get lunch together?"

    show s side

    s "Hmmmmm..."

    show s front

    s "Sure. Why not. I owe it to you anyways."

    r "Owe me? For what?"

    s "Remember the whole security incident on your first day?"

    s "Yeah. Sorry about that."

    r "Oh! I-It's fine..."

    r "...Why did you think I didn't work here?"

    show s side

    s "I'll try to put this in the nicest way possible..."

    show s front 

    s "You need to do a lot of work on your face."

    r "T-That wasn't nice at all..."

    show s side

    s "Hmmm... How to put it..."

    show s front

    s "You just seem like the kinda person who would be a danger to those around them."

    s "Like if I was infront of you in a line, I might take a few steps away, you know?"

    r "That... was worse, Shamir."

    show s back

    s "Let's just forget everything I said and go get lunch."

    r "...yeah."

    "{bt}You got a little closer to Shamir today.{/bt}"
    $ s_count+=1
    $ todayTalk = "Shamir"

    jump returnToDay
label shamir2:
    #Talking to Shamir and learning about how her art never took off because it's “foreign”
    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Glop (Front Desk afternoon).wav" fadein 1.0

    r "Hey Shamir! Wanna go get lunch?"

    show s front at S_C
    with dissolve

    s "Sure. Again, I owe you after last time."

    r "L-Let's just drop the \"I owe you\" stuff and get lunch, yeah?"

    s "Sure."

        stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/gloop (Cafe).wav" fadein 1.0

    show s front at DS_C

    r "So Shamir, what do you do outside of work?"

    show s side

    s "I do art, mostly."

    r "Wow, really? Do you sell any of your pieces?"

    show s front

    s "I try to, but its really hard to here."

    r "Here? What do you mean?"

    show s side

    s "Ah, I don't think I've ever told you."

    show s front

    s "I'm an immigrant. I came here from overseas."

    r "I see, but what does that have to do with your art?"

    s "Well, my art is very telling of where I came from."

    s "And a lot of people here aren't quite used to that."

    s "Food is one thing, yknow? But are people as likely to buy an expensive painting?"

    show s side
    
    s "Not so much."

    r "Well, can I see your paintings? Maybe I'll buy one!"

    show s front

    s "Sure. Have a look."

    "Shamir pulls out her phone and swipes through some paintings."

    r "W-Wow! These are amazing! I'd love to buy one when I get paid!"

    s "Thank you, Robin. That means a lot to me."

    s "I'll see what I can sell to you."

    show s side

    s "But it looks like lunch is wrapping up, let's head back."

    r "Ah, you're right. See you, Shamir!"

    "..."

    "{bt}You got a little closer to Shamir today.{/bt}"
    $ s_count+=1
    $ todayTalk = "Shamir"

    jump returnToDay
label shamir3:
    #Talking to Shamir and getting interrupted by Boss, showing her suspicion
    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Glop (Front Desk afternoon).wav" fadein 1.0

    show s front at S_C
    with dissolve

    r "Hey Shamir! Wanna go get lunch?"

    s "Sure, Robin. Just give a moment, I need to wrap this up."

    show h front at S_L
    with dissolve

    h "Hello Shamir. Do you need any help?"

    s "{sc}...{/sc}"

    s "I'm fine... Horace."

    h "...I see."

    show h back

    h "I'll be off then."

    hide h back
    with dissolve

    s "..."

    r "I-Is something up?"

    s "Yeah. I.. don't think I want to get lunch today."

    r "H-Huh? Why?"

    s "I had a change of heart. Sorry, Robin."

    show s back 

    s "I also need some fresh air."

    hide s back
    with dissolve

    s "I-I'll see you."

    "..."

    "{bt}You got a little closer to Shamir today.{/bt}"
    $ s_count+=1
    $ todayTalk = "Shamir"

    jump returnToDay
label shamir4:
    #Learning about her suspicion of the company (maybe even leaving to the bar)

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    r "Phew... Finally done for the day..."

    show s front at S_C
    with dissolve

    s "Hey, Robin?"

    r "O-Oh! Hey Shamir! What's up?"

    s "Mind if we chat about something?"

    r "Oh sure! Lunch?"

    s "Let's... step outside."

    r "O-Okay..."

    stop music fadeout 1.0
    scene bg officeoutside:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    show s front at apron

    r "So Shamir, what is it you wanted to talk abo-"

    s "You feel it too, don't you?"

    s "Something is wrong here."

    r "..."

    s "I can see it in your eyes, Robin. You feel the same way."

    r "Y-Yeah... I've almost forgotten because I got so absorbed in my work but..."

    r "Since the beginning, nothing has sat quite right with me here."

    s "Right. Everyone feels this way when they first come here."

    s "But everyone slowly forgets."

    s "It's driving me insane."

    s "Every day, I dig into this company more and more."

    s "Yet I feel like I know less and less."

    s "That's why I reacted the way I did around Horace. I really don't trust them at all."

    s "We used to be friends, but one day they came into work dead behind the eyes."

    s "And that was the day Horace got a massive promotion. Their spot here was secured."

    s "Robin. Before you loose your way, get out of here. As soon as you can."

    r "S-Shamir..."

    s "Did you know this company exclusively snatches up college graduates?"

    s "And yet, they never seem to leave this place. They all get caught in it's web."

    s "Our biggest department is IT, which is already an anomoly."

    s "And yet, none of our infastructure is for our work, rather its to store information about us."

    s "Don't you see it, Robin?"

    "..."

    "..."

    "..."

    s "...heh... I probably sound like a madwoman, don't I?"

    s "We have a few lunches together, I act weird around a coworker..."

    s "And here I am barfing my conspiracy theories at you."

    s "And I called you a creep. Heh..."

    s "...Robin?"

    r "..?"

    menu:
        s "Do you belive me?"

        "I Do.":
            $ bShamir = True;
            r "I-I belive you, Shamir."

            r "I never know what I'm working on, I can't seem to shake this feeling deep in my chest... I..."

            s "It's okay if you don't understand, Robin. You just have to run."

            r "N-No..."

            s "Hm?"

            r "Shamir, if you're gonna find out what's going on here. Let me help you."

            s "Robin..."

            s "T-Thank you. I really can't remember the last time I had someone on my side."
            pass
        "I Don't.":
            $ bShamir = False;
            r "..."

            s "... I see."

            show s back

            s "Forget I said anything. Let's just go back to being lunch buddies."

            "..."

            r "Alright."

            show s Front

            s "Robin?"

            r "Y-Yeah?"

            show s back

            s "I'm tired. I really don't how how much more I have left in me."

            hide s back
            with dissolve

            s "Goodbye."
            pass

    "{bt}You got a little closer to Shamir today.{/bt}"
    $ s_count+=1
    $ todayTalk = "Shamir"

    jump returnToDay 
label shamir5A:
    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Glop (Front Desk afternoon).wav" fadein 1.0

    show s front at S_C
    with dissolve

    r "Hey, Shamir!"

    show s side

    s "Robin, just the person I wanted to see."

    s "Want to go out and chat a bit more this weekend? Somewhere a bit further away than work?"

    r "Sure. Where did you have in mind?"
    
    show s front

    s "Birdley's?"

    r "Sounds good!"

    show s side

    s "Fantastic. I'll see you then."

    show s back
    s "For now, I've got something to attend to. We'll save todays chatting for then."

    r "Oh! Shamir, before you go..."

    show s front at DS_C
    with dissolve

    s "Hm?"

    r "Never forget that I'm in your corner, okay?"

    show s back

    s "...I woln't. Thank you, Robin."

    hide s back
    with dissolve

    "{bt}You got a little closer to Shamir today.{/bt}"
    $ s_count+=1
    $ todayTalk = "Shamir"
    jump returnToDay
label shamir5B:
    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade
    play music "music/Lost Deer.mp3" fadein 1.0

    show s front at S_C
    with dissolve

    r "Hey Shamir!"

    s "Hey, Robin!"

    r "Wanna go get lunch?"

    s "Absolutely! Let's go!"


    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    show s front at S_C
    with dissolve

    r "So Shamir, how was your day?"

    s "{bt}Ahahahahahaha!{/bt}"

    s "Robin you're a riot!"

    r "Haha... I... didn't say anything funny though?"

    s "Oh! My bad, everything has just been so funny to me lately, y'know?"

    r "Ahaha... Yeah..."

    show s back

    s "anyways I ought to be heading back to work."

    hide s back
    with dissolve

    s "bye."

    r "H-Huh? Wait wha-"

    "{sc}You got a little closer to Shamir today.{/sc}"
    $ s_count+=1
    $ todayTalk = "Shamir"
    jump returnToDay
    
label shamirEndingA:
    #Talk about how she’s picking up art again, and how she quit, 
    #realizing that it's impossible for someone like her to take down a company.

label shamirEndingB:

