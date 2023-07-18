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

default h_count = 1
default t_count = 1
default s_count = 1
default c_count = 1
default day = 1
default todayTalk = ""

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
    
    "A small dingey bar, kept afloat by its regulars, who have been coming here since before I was even born."

    "Said regulars are all within their cliques, or are glued to the telly, watching... something."

    "I sit and stir my Black Russian. Not in idle bordem, but rather in tense, sharp, anxiety."

    "My mind is racing, soaring through the air, beyond the wit of man."

    "My mind comes careening back down to reality, when the glass of solitude is shattered by a familiar voice."

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

    scene black
    with fade

    jump dayOne_morning

label dayOne_morning:

    "..."

    "..."

    r "Ugh..."

    scene bg home
    with fade

    "I roll out of bed, falling onto the floor"

    "I pick myself up, while rubbing my eyes."

    "Dread strikes as I slowly realize that today"

    "...is the first day of my new life."

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

    show c back at US_C

    c "Where have you been so far?"

    r "Besides the front desk and the office, nowhere else."

    c "Got it. I'll show you the cafeteria and the way to Hori's office"

    r "Actually, I've been meaning to ask, why do you call Horace Hori?"
    
    r "And why do they hate that?"

    c "..."

    r "..."

    "The air grew unusually thick."

    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

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

    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    show c front at S_L
    with move

    c "And here we are! Hi Horace!"

    show h front at S_C
    with dissolve

    h "What are you two doing here."

    show c side

    c "We're on the tour, Robin has to know where their boss' office is!"

    h "I see. Did you need anything else?"

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

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

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


label taiga:
    if t_count == 0:
        jump taiga1
    elif t_count == 1:
        jump taiga2
    elif t_count == 2:
        jump taiga3
    elif t_count == 3:
        jump taiga4
    elif t_count == 4:
        jump taiga5
    elif t_count == 5:
        jump taigaEnding
    else:
        python:
            renpy.error("Invalid taiga link!")

label horace:
    if t_count == 0:
        jump horace1
    elif t_count == 1:
        jump horace2
    elif t_count == 2:
        jump horace3
    elif t_count == 3:
        jump horace4
    elif t_count == 4:
        jump horace5
    elif t_count == 5:
        jump horaceEnding
    else:
        python:
            renpy.error("Invalid horace link!")

label shamir:
    if t_count == 0:
        jump shamir1
    elif t_count == 1:
        jump shamir2
    elif t_count == 2:
        jump shamir3
    elif t_count == 3:
        jump shamir4
    elif t_count == 4:
        jump shamir5
    elif t_count == 5:
        jump shamirEnding
    else:
        python:
            renpy.error("Invalid shamir link!")

label claire:
    if t_count == 0:
        jump claire1
    elif t_count == 1:
        jump claire2
    elif t_count == 2:
        jump claire3
    elif t_count == 3:
        jump claire4
    elif t_count == 4:
        jump claire5
    elif t_count == 5:
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
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

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

    show t front
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

    "You got a little closer to Taiga today."

    $ t_count+=1
    $ todayTalk = "Taiga"

    jump returnToDay
label taiga2:
    #Lunch with Taiga, says he has no interests
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    r "Hey Taiga, wanna go get lunch again?"

    show t side at S_C
    with dissolve

    r "To uh, bolster your status higher or whatever?"

    show t front

    t "Fine. Lets go."

    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    show t back at apron
    with dissolve

    t "..."

    r "..."

    r "S-So Taiga, do you have any interests... besides work?"

    show t side

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

    "You got a little closer to Taiga today."

    $ t_count+=1
    $ todayTalk = "Taiga"

    jump returnToDay
label taiga3:
    #Talking to Taiga and being interrupted by Shamir about art
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

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

    if s_count > 0:
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

    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

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

    "You got a little closer to Taiga today."

    $ t_count+=1
    $ todayTalk = "Taiga"

    jump returnToDay
label taiga4:
    #Talking to Taiga about art
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    r "H-Hey Taiga, I'm free today..."

    show t front at S_C
    with dissolve

    t "..."

    show t back

    t "Come with me."

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

    "You got a little closer to Taiga today."

    $ t_count+=1
    $ todayTalk = "Taiga"

    jump returnToDay
label taiga5:
    #Seeing the real Taiga and setting up ending
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    r "Hey, Taiga."

    show t back at S_C
    with dissolve

    t "..."

    r "Taiga."

    t "..."

    r "Ugh... just... come with me you mope."

    show t side

    t "Fine."

    scene bg officeoutside:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    show t side
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

    r "So we're going to the art gallery this weekend, okay?"

    hide t front
    with dissolve

    t "Fine."

    "..."

    "You got a little closer to Taiga today."

    $ t_count+=1
    $ todayTalk = "Taiga"

    jump returnToDay
label taigaEnding:
    #Going with taiga to art studio


label claire1:
    #Getting help from Claire and talking about work

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

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

    c "Sounds good!"

    show c back

    c "Let's go eat, I'm starving!"
    
    "You got a little closer to Claire today."
    $ c_count+=1
    $ todayTalk = "Claire"

    jump returnToDay
label claire2:
    #Talking to Claire about food over lunch

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

    r "Hey, Claire, wanna go get lunch again today?"

    show c front at S_C
    with dissolve

    c "Sure! Let's head over!"

    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
        function WaveShader(period=1.25, amp=12.0, speed=1.3, direction='y')
    with fade

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

    "You got a little closer to Claire today."
    $ c_count+=1
    $ todayTalk = "Claire"

    jump returnToDay
label claire3:
    #Getting help and getting walked in by Horace
    "You got a little closer to Claire today."
    $ c_count+=1
    $ todayTalk = "Claire"

    jump returnToDay
label claire4:
    #Learning about Claire and Horace
    "You got a little closer to Claire today."
    $ c_count+=1
    $ todayTalk = "Claire"

    jump returnToDay
label claire5:
    #Wrap up, talking about work and life, set up ending
    "You got a little closer to Claire today."
    $ c_count+=1
    $ todayTalk = "Claire"

    jump returnToDay
label claireEnding:
    #Chatting at bar says she might leave


label horace1:
    #Talking in their office
    "You got a little closer to Horace today."
    $ h_count+=1
    $ todayTalk = "Horace"

    jump returnToDay
label horace2:
    #Talking over lunch
    "You got a little closer to Horace today."
    $ h_count+=1
    $ todayTalk = "Horace"

    jump returnToDay
label horace3:
    #Talking but Claire pushes plot forward
    "You got a little closer to Horace today."
    $ h_count+=1
    $ todayTalk = "Horace"

    jump returnToDay
label horace4:
    #Backstory dump (basically)
    "You got a little closer to Horace today."
    $ h_count+=1
    $ todayTalk = "Horace"

    jump returnToDay
label horace5:
    #Chat and setup for ending
    "You got a little closer to Horace today."
    $ h_count+=1
    $ todayTalk = "Horace"

    jump returnToDay
label horaceEnding:
    #Chat and talk about how your work has been so far and how they’ve changed


label shamir1:
    #Talking to Shamir and learning about her and her enjoyment of art
    "You got a little closer to Shamir today."
    $ s_count+=1
    $ todayTalk = "Shamir"

    jump returnToDay
label shamir2:
    #Talking to Shamir and learning about how her art never took off because it's “foreign”
    "You got a little closer to Shamir today."
    $ s_count+=1
    $ todayTalk = "Shamir"

    jump returnToDay
label shamir3:
    #Talking to Shamir and getting interrupted by Boss, showing her suspicion
    "You got a little closer to Shamir today."
    $ s_count+=1
    $ todayTalk = "Shamir"

    jump returnToDay
label shamir4:
    #Learning about her suspicion of the company (maybe even leaving to the bar)
    "You got a little closer to Shamir today."
    $ s_count+=1
    $ todayTalk = "Shamir"

    jump returnToDay 
label shamir5:
    #Chatting and setup for ending 
    "You got a little closer to Shamir today."
    $ s_count+=1
    $ todayTalk = "Shamir"

    jump returnToDay
label shamirEnding:
    #Talk about how she’s picking up art again, and how she quit, 
    #realizing that it's impossible for someone like her to take down a company
