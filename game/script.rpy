init python:
    config.has_quicksave = False

    #Generate seperate audio channel from voice for beeps.
    renpy.music.register_channel(name='beeps', mixer='voice')

    def z(event, **kwargs):
        if event == "begin": 
            build_sentence(_last_say_what, "zeke")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def w(event, **kwargs):
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
define w = Character("????", callback=w, what_font="w.ttf")

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
default bShamir = True

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

    "May 201X\n11:18 P.M.\nBirdley's Bar"

    scene bg bar
    with fade
    play music "music/bar.wav" fadein 1.0
    
    "A small local bar, kept afloat by its regulars, who have been coming here since before I was even born."

    "Said regulars are all within their cliques or are glued to the bar's TV, watching... something."

    "I sit and stir my Black Russian. Not in idle bordem, but rather in a tense, sharp, anxiety."

    "My mind is racing, soaring through the air, beyond the wit of man."

    "My mind comes careening back down to reality when the glass of solitude is shattered by a familiar voice."

    z "Hey."

    show z front at S_C
    with dissolve

    z "Mind if I have a seat?"

    r "Oh, hey Zeke. Go ahead."

    $ z_name = "Zeke"

    show z back at S_C

    "He takes a seat while gesturing at the waiter"

    show z side at S_C

    z "A bottle of your finest Scotch."

    r "H-Hey! That's probably really expensive..."

    r "And I didn't even finish my drink..."
    
    z "It doesn't really matter, after all..."

    show z front at S_C

    z "Doesn't {bt}someone{/bt} here have a job now?"

    z "And didn't {bt}two{/bt} people here just graduate from college?"

    show z side  at S_C

    z "So we should celebrate. Full stop."

    r "Please don't remind me."

    z "Remind you of what?"

    show z front at S_C

    "I bury my face into the table"

    r "{sc}Please don't remind me about my job.{/sc}"

    z "What?"

    "I hear two glasses and a bottle hit the table"

    z "How can you not like having a job? That makes literally no sense."

    r "I'm just... not a fan of change."

    r "I got used to college, and even more so to school."

    r "This is just... different. And I really don't like that."

    show z side  at S_C

    z "To each their own, I guess."

    r "Exactly. Now can we stop talking about it and just drink?"

    z "Fair enough. Cheers."

    r "Cheers."

    show z back  at S_C

    "Our glasses tap, before we take a long sip of the whisky."

    r "Wow. This really is good."

    show z side  at S_C

    z "See? Worth every penny."

    r "Well, I wouldn't say {i}that{/i}. Beer is just fine."

    z "We'll switch to beer after this, let's enjoy this while we're still sober."

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

    "I pick myself up while rubbing my eyes."

    "Dread strikes as I slowly realize that today"

    "...is the first day of my new life."

    stop music fadeout 1.0
    scene bg officeoutside:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with pixellate
    play music "music/Sludge (Office outside morning).wav" fadein 1.0


    "After parking my car, I walk over to the front of the building. "

    "I'm well aware that this is just my own stress messing with me, but the atmosphere here..."

    "It just feels different. Otherworldly, almost."

    "I collect myself, straighten out my outfit, and walk into the front door."

    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
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

    r "{sc}WHAT ARE YOU DOING?!{/sc}" with vpunch

    show s side at S_C

    s "..."

    show s back at S_C

    s "They seem to be getting aggressive..."

    r "{sc}I WORK HERE! THIS IS MY FIRST DAY!{/sc}" with vpunch

    "I rummage through my bag to grab my ID."

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
    with fade

    "Horace quickly moves down the hallway, I wipe my face off with the towel while following them down the hall."

    "We wisk by endless offices and meeting rooms, only briefly slowing down to turn corners."

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
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

    "I extend my hand toward Taiga"

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
    with fade

    show c back at S_C

    c "Where have you been so far?"

    r "Besides the front desk and the office, nowhere else."

    c "Got it. I'll show you the cafeteria and the way to Hori's office"

    r "Mind if I ask why you call Horace Hori?"

    c "..."

    r "..."

    "The air grew unusually thick."

    stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
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
    with fade
    play music "music/Grime (Boss).wav" fadein 1.0

    show c front at S_L
    with move

    c "And here we are! Hi Horace!"

    show h front at S_C
    with dissolve

    h "What are you two doing here?"

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

    "Horace shoves both Claire and me out of the office."

    scene bg hallway:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade

    r "Oof!"

    "SLAM" #sfx here maybe?

    show c side at S_C

    c "Welp! Guess the tour is over then!"

    show c front

    c "Let's head back to our desks and get to work."

    hide c front with dissolve

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/slime (Office Morning).wav" fadein 1.0

    "I plop down into my chair and face my computer."

    "...It seems like Horace has already given me a lot of things to do."

    "Welp, time to get to it..."

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade

    r "Phew... finally lunchtime."

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
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0
    

    r "Alright! I'm back. Time to get cracking at my afternoon's work."

    show t front at S_C

    t "Hey, Robin."

    r "Hm? What's up, Taiga?"

    t "I just had a meeting with Horace, now it's your turn."

    r "A-Ah, I see."

    show t back

    t "Good luck."

    hide t back

    r "T-Thanks..."

    "Well, best I head over there..."

    stop music fadeout 1.0
    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/Grime (Boss).wav" fadein 1.0

    r "Hello?"

    show h front at S_C 

    h "Hello, Robin."

    show h side

    h "How was your morning? Did you finish all your work?"

    r "Yep! All done and dusted."

    "I'll leave out the fact I just barely finished it..."

    show h front

    h "Good. How are the sheets you were assigned looking?"

    r "They all looked good!"

    h "Any full bincalls?"

    r "Just one, but I took care of it."

    h "Excelent work, Robin."

    show h back

    h "That's all I need from you. Thanks."

    r "A-Alright, see you!"

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    r "Alright, time to get to work properly..."

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade

    r "Phew! Finally done!"

    show c front at S_C
    with dissolve

    c "Yeah, me too. Good work today, Robin!"

    r "Thanks, Claire!"

    r "I can't believe I got my first day of work done, it doesn't feel quite real yet..."

    r "How are you feeling, Taiga?"

    show t front at S_L
    with dissolve

    t "..."

    show t back

    t "I'll see you all tomorrow."

    hide t back
    with dissolve

    r "A-Ah..."

    r "W-Well, I'll see you tomorrow, Claire!"

    c "Yeah, see you!"

    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/Glop (Front Desk afternoon).wav" fadein 1.0

    show s front at S_C
    with dissolve

    r "Hey Shamir! I'll see you tomorrow!"

    s "...See you."

    stop music fadeout 1.0
    scene bg home
    with pixellate
    play music "music/home (Night).wav" fadein 1.0

    r "Phew! Finally home."

    "I fall down onto my bed."

    r "Today wasn't too bad... All things considered..."

    r "Talking with [todayTalk] was nice as well."

    r "Well... I should go to sleep."

    r "I have to get up bright and early again tomorrow."

    "..."

    stop music fadeout 1.0
    scene black
    with fade

    jump dayTwo_morning

label dayTwo_morning:
    $ day = 2
    stop music fadeout 1.0
    scene bg home
    with fade
    play music "music/home (Morning).wav" fadein 1.0

    "..."

    r "ugh..."

    "I roll over and fall on the floor, face first this time."

    r "{sc}Ow...{/sc}"

    "I slowly rise up from the floor, rubbing my face."

    r "Oof... G-Guess I better get ready for work..."

    stop music fadeout 1.0
    scene bg officeoutside:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with pixellate
    play music "music/Sludge (Office outside morning).wav" fadein 1.0

    "Ugh... Despite how well I thought yesterday went."

    "Coming back here just reminded me how {bt}creepy{/bt} this place is..."

    "It feels almost... dizzying..."

    "Did... I just get used to it yesterday?"

    w "it's best not to think too hard about things."

    r "{sc}H-HUH?{/sc}" with vpunch

    show s front at S_C
    with dissolve 

    s "Robin?"

    r "{sc}WAGH!!!{/sc}"

    r "Oh... Oh my god... It's just you, Shamir."

    show s side

    s "Did something happen?"

    r "I swear I heard someone say something... It must have been you..."

    s "...I didn't say anything."

    r "...I-I see..."

    r "Don't worry about it, then. Let's head to work, yeah?"

    show s front

    s "..."

    show s side

    s "Yeah..."

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/slime (Office Morning).wav" fadein 1.0

    r "Morning Claire! Morning Taiga!"

    show c front at S_L
    with dissolve
    show t front at S_R
    with dissolve

    c "Good morning Robin!"

    show t side

    t "...Morning"

    show t front

    t "Oh, Robin, by the way..."

    r "Hm?"

    t "Boss passed you a task. Check your Smacked, they put it there."

    show t side

    t "...Also, your fly is down."
    
    "{sc}!{/sc}"

    "This is gonna be another long day..."

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade

    r "Phew... finally lunchtime."

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
label dayTwo_afternoon:
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    "Alright! Now that I'm done with lunch, it's time to get started on this afternoon's work."

    "Let's see what's on the agenda..."

    "Licrosect the docs related to the revitalization sector..."

    "Push fatty dispositions out for QA..."

    "Hm..."

    r "Hey. Claire, Taiga..."

    show c front at S_L
    with dissolve
    show t front at S_R
    with dissolve

    c "Yeah?"

    t "What?"

    stop audio fadeout 1.0

    r "What does this company even do?"

    show t side

    t "..."

    show c side

    c "..."

    r "..."

    r "Wait... Do..." 
    
    r "Do none of us know?"

    show t back

    t "I don't really care. Work is work."

    hide t back
    with dissolve

    t "Speaking of which, I'm going to get back to work."

    show c front

    c "M-Maybe you should bring it up with Horace tomorrow?"

    r "Hm? Is Horace not in?"

    c "They're at a meeting with some higher-ups all afternoon."

    r "I see. I'll try asking tomorrow morning then."

    r "Until then... Guess we gotta get to it..."

    c "Y-Yeah..."

    scene bg home
    with pixellate
    play music "music/home (Night).wav" fadein 1.0

    r "Ugh... I'm finally done..."

    "I can't even clearly remember what happened this afternoon..."

    "I just remember talking about the company with Claire and Taiga..."

    "Oh, and I also remember talking to [todayTalk] during lunch but..."

    "That's really about it."

    "Maybe I got too absorbed in my work."

    "Or maybe... I'm not getting enough sleep..."

    "Speaking of which, best I hit the hay."

    "..."

    stop music fadeout 1.0
    scene black
    with fade

    jump dayThree_morning

label dayThree_morning:
    $ day = 3
    stop music fadeout 1.0
    scene bg home
    with fade
    play music "music/home (Morning).wav" fadein 1.0

    "..."

    r "..ugh"

    "I roll out of bed, falling onto the floor"

    "Upon impact, I hit my back in a way that takes the wind out of me."

    r "{sc}wheeze{/sc}"

    "I get up while rubbing my back."

    r "G-Guess I best get ready for work..."

    "I gotta remember to ask Horace that question too..."

    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with pixellate
    play music "music/Glop (Front Desk morning).wav" fadein 1.0

    show s front at S_C
    with dissolve

    "I come in to see Shamir at the front desk."

    r "Morning, Shamir!"

    s "...Morning"

    r "Hey, Shamir? Do you know what we do here?"

    r "L-Like, what does this company even produce?"

    show s side

    s "I see, you're curious too..."

    r "Y-Yeah, are you?"

    s "Mhm. Haven't quite figured it out yet."

    "Figured it out..?"

    r "Well, I'm gonna go ask Horace about it."

    s "I see... Good luck with that."

    r "Thanks!"

    stop music fadeout 1.0
    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/Grime (Boss).wav" fadein 1.0

    r "Hey, Boss?"

    show h front at S_C
    with dissolve

    h "Yes? What is it?"

    r "What... Does this company do?"

    show h side

    h "Energy."

    show h front

    h "We produce low-cost, efficient, and renewable energy here."

    w "but this shouldn't concern you"

    r "{sc}WAUGH!{/sc}" with vpunch

    h "Robin?"

    r "D-DID YOU HEAR THAT?" with vpunch

    h "I didn't hear anything..."

    "What is going on..?"

    h "I'm sorry to cut this meeting while you're having a breakdown, but I've got work to do."

    h "As a new hire, you do not have any PTO or sick days yet."

    h "So if you're going to lose your mind, make sure you get your work done."

    r "G-Got it... See you... Boss..."

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/slime (Office Morning).wav" fadein 1.0

    r "..."

    show c front at S_C
    with dissolve

    c "Morning Robin!"

    c "Did you ask Hori what we do here?"

    show t front at S_L
    with dissolve

    t "..."

    r "O-Oh! Y-yeah... We do uh... Energy stuff..."

    c "I-I see..."

    c "You okay, Robin?"

    r "Yeah, just tired is all."

    c "Ah, alright. If you need me to help with any  of your work, let me know."

    r "T-Thanks..."

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade

    r "Phew, finally got all my work done... At least I'm feeling a bit better!"

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
label dayThree_afternoon:
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    "Alright... All done with lunch, time to get started with this afternoon's work."

    show h front at S_C
    with dissolve

    h "Hello everyone, can I have your attention for a moment?"

    show c front at S_L
    with dissolve
    show t front at S_R
    with dissolve

    c "What's up?"

    h "Our yearly revitalization ceremony is falling on Monday. The company will take the day off."

    h "We'll also offer festivities, though you can stay at home this year."

    r "Oooh... A long weekend!"

    r "Do you guys have any plans?"

    c "It's a chance to stay in and catch up on some books for me."

    t "..."

    show t side

    t "Boss, can we come in and work anyways?"

    h "No. Take the time off."

    t "Grrr..."

    if t_count > 2:
        r "You could work out and play the piano, Taiga?"

        r "Do a bit extra on Monday, then stay later at work during the week?"

        t "... I suppose..."

    r "How about you Boss? Gonna do anything?"

    h "I'll be here running festivities."

    r "I see, good luck with that!"

    show h back

    h "That's all."

    hide h back
    with dissolve

    h "Thank you. Get back to work, please."

    c "Welp. Let's get to it!"


    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade

    "Phew... Done!"

    r "Man, everything feels a bit more tolerable now that I know we have a 3 day weekend coming up!"

    show c front at S_C
    with dissolve

    c "Right? This afternoon felt like a breeze."

    c "Welp, I'll see you two tomorrow!"

    if t_count > 3:
        show t front at S_L
        with dissolve
        t "See you, Robin."

    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/Glop (Front Desk afternoon).wav" fadein 1.0

    show s side at S_C
    with dissolve

    r "Hey Shamir! I'll see you tomorrow!"

    s "See you..."

    show s front

    s "Ah, wait."

    r "Hm? What's up?"

    s "What did Horace say?"

    if s_count > 3: 
        s "I forgot to ask you during lunch."

    r "Huh? What about Horace?"

    s "This morning, you said you would ask Horace what this company was for."

    show s side

    s "What did they say?"

    r "Oh... Something about energy I think?"

    r "I'm not sure... I'm a bit tired..."

    show s front

    s "I see. I'll see you around, Robin."

    r "See you!"

    stop audio fadeout 1.0
    scene bg home
    with pixellate
    play music "music/home (Night).wav" fadein 1.0

    r "Phew! Finally home..."

    "I fall onto my bed"

    "Today was pretty great... talking to [todayTalk] was great."

    "And the announcement of having Monday off was fantastic!"

    "Not much else happened today though... right?"

    "Yeah... Yeah..."

    "..."

    stop music fadeout 1.0
    scene black
    with fade

    jump dayFour_morning
 
label dayFour_morning:
    $ day = 4
    stop music fadeout 1.0
    scene bg home
    with fade
    play music "music/home (Morning).wav" fadein 1.0

    "..."

    r "..ugh"

    "I roll out of bed, falling onto the floor"

    "Upon impact, I hit my neck in a way that woke me up instantly."

    r "{sc}ACK{/sc}"

    "I pull myself up and start to get ready for work."

    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with pixellate
    play music "music/Glop (Front Desk morning).wav" fadein 1.0

    r "Hey, Shamir, by the way..."

    show s front at S_C
    with dissolve

    s "Hm?"

    r "What do you plan on doing during the long weekend?"

    s "Art."

    if s_count > 2:
        r "Figures."
    else:
        r "I see!"

    r "Well, I hope you have fun with that!"

    s "Thanks, hope you have a good one too."

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/slime (Office Morning).wav" fadein 1.0

    r "Morning you guys!"

    show t side at S_L
    with dissolve
    show c front at S_R
    with dissolve

    c "Morning!"

    t "Morning."

    c "Robin, you haven't seen the company email we got, right?"

    r "Well, seeing as how I just got in, no. Lemme take a look..."

    "I have a seat at my desk and open up my email."

    r "\"This Monday, we will additionally be saying goodbye to one of our longtime employees.\""

    r "\"Chuck has been with us for years, and it is finally time for him to fulfill his true purpose in retirement.\""

    r "\"Please say thank you to Chuck if you see him in the halls.\""
    
    r "\"And feel free to join us in celebrating his time here on Monday.\""

    r "\"We will never fail to celebrate one of our esteemed employees leaving.\""

    r "\"Please look forward to when you or your coworkers finally leave.\""

    r "\"Mors tua, vita mea, nostra aeternitas.\""

    r "\"CEO.\""

    r "I see..."

    show t side

    t "Yeah, thanks for reading that out for us, Robin."

    r "Ah... yeah..."

    r "Well, did anyone here know Chuck or anything?"

    t "Nope."

    show c side

    c "Nah..."

    show c front

    c "He seemed to be a higher-up. Someone who would have no business with us."

    show c side

    c "Maybe Hori knew him?"

    r "I see... I'll try asking Boss about that later..."

    c "Anyways, best we get to work, yeah?"

    r "Yeah. Let's get to it."

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade

    r "Phew... finally lunchtime."

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
label dayFour_afternoon:
    #Talk about retirement with Taiga and Claire
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    "Alright... back from lunch!"

    show c front at S_C
    with dissolve
    show t front at S_R
    with dissolve

    c "Hey, Robin, Taiga?"

    r "What's up, Claire?"

    show c side

    c "I was curious, especially after that e-mail we got..."

    show c front

    c "Are you two thinking about retirement at all?"

    c "I'm honestly not thinking about it much, and sometimes I feel like I should."

    show t side 

    t "I'll retire when I die."

    r "Uh. I also haven't really thought about retirement."

    r "I know you're supposed to start early but... I dunno it's not something I wanna think about."

    c "Fair enough. It's a really scary thought."

    c "Whenever I see one of these retirement emails I just think \"Oh god. That's gonna be me someday.\"" 

    r "Right? It's such a scary thought."

    c "Well, that's an issue for future me to worry about. We should focus on our work."

    r "Too true, let's get to it!"

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade

    "Alright... All done!"

    "Maybe I should go ask Horace about Chuck..."

    stop music fadeout 1.0
    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/Grime (Boss).wav" fadein 1.0

    r "Hey, Boss?"

    show h front at S_C
    with dissolve

    h "Yes? What is it?"

    r "I was curious, did you personally know Chuck at all?"

    h "Yes. He's one of the higher-ups here. I work directly under his order."

    r "I see..."

    r "Are you going to miss him?"

    h "Not really."

    if h_count > 4:
        h "We talked about this."
    
    r "Y-Yeah. Right. Gotcha."

    h "Is that all you wanted to ask?"

    r "Yeah, pretty much..."

    r "I'll see you, Boss."

    stop audio fadeout 1.0
    scene bg home
    with pixellate
    play music "music/home (Night).wav" fadein 1.0

    r "Man, I'm finally home!"

    "I flop onto my bed."

    "It was great to get to learn more about [todayTalk] some more."

    "But outside of that... Today was all about retirement... Ugh. That bums me out..."

    "Best not to think about it..."

    "..."

    stop music fadeout 1.0
    scene black
    with fade

    jump dayFive_morning

label dayFive_morning:
    $ day = 5
    stop music fadeout 1.0
    scene bg home
    with fade
    play music "music/home (Morning).wav" fadein 1.0

    "..."

    r "..ugh"

    "I roll out of bed, falling onto the floor"

    "Upon impact, I hit my head in a way that..."
    
    "uh..."
    
    w "absolves you of your sins."

    "Right. I fell in a way that absolves me from my sins."

    r "{sc}ACK{/sc}"

    "I pull myself up and start to get ready for work."

    stop music fadeout 1.0
    scene bg officeoutside:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with pixellate
    play music "music/Sludge (Office outside morning).wav" fadein 1.0

    "Wow... I can't belive it's almost been a week since I started working here."

    "Time really flew by. I can barely remember working, but can vividly remember all the time I spent with the people I've met here."

    "No point in just standing here, time to get to work."

    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/Glop (Front Desk morning).wav" fadein 1.0

    show h front at S_C
    with dissolve

    h "Robin. Just the person I wanted to see."

    r "Oh! Hey Boss! What's up?"

    h "I had a meeting yesterday about our new hires."

    show h side

    h "We decided to give you the evening off."

    h "Feel free to head home after lunch."

    r "W-Wow really? Why so sudden?"

    show h front

    h "We all need a break, Robin. I've been working on this for almost 2 weeks."

    r "...Working on what?"

    show h side

    h "Never mind..."

    h "Try to get some work done this morning now."

    r "G-Got it!"

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/slime (Office Morning).wav" fadein 1.0

    "A-Alright! Time to knuckle down and work!"

    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade

    r "Phew... finally lunchtime."

    "This is my last chance to talk to someone before the weekend..."

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
label dayFive_afternoon:
    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    "A-Alright! All done! Time to head home!"

    r "Hey Claire! Taiga! Have a good weekend!"

    show c front at S_C
    with dissolve

    c "Oh! Heading out early?"

    r "Yep! Boss gave the new hires the afternoon off."

    c "Lucky lucky! Have fun!"

    if c_count > 5:
        c "I'll see you this weekend!"

    if t_count > 5:
        show t front at S_L
        with dissolve

        t "...I'll see you this weekend, Robin."

    r "See you!"

    scene bg hallway:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade

    show h front at S_C
    with dissolve

    r "Oh! Boss!"

    h "Hello Robin. Thank you for a good week of work."

    r "T-Thank you!"

    if h_count > 5:
        show h side

        h "I'll see you this weekend."
    
    r "See you!"

    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/Glop (Front Desk morning).wav" fadein 1.0

    show s front at S_C
    with dissolve

    r "Hey Shamir!"

    if not bShamir:
        s "Howdy Robin!"
    else:
        s "...Hey."

    r "I'll be seeing you! Thanks for a good first week!"

    if not bShamir:
        s "Absolutely! Thank you so much, Robin!"
    else:
        s "Yeah..."

    if s_count > 5:
        show s side
        if not bShamir:
            w "See you this weekend."
        else:
            s "See you this weekend."
        

    r "See you!"

    stop music fadeout 1.0
    scene bg officeoutside:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/Sludge (Office outside afternoon).wav" fadein 1.0

    "Alright... It's Friday..."
    
    "Time to head to the bar!"

    "I'll give Zeke a call in a little bit, I can tell him about my week! "

    stop music fadeout 1.0
    scene bg bar
    with pixellate
    play music "music/bar.wav" fadein 1.0

    show z front at DS_C
    with dissolve

    r "Hey Zeke!"

    z "Hey. You look much more chipper than last weekend."

    r "Yeah! Work wasn't as bad as I thought. I had a lotta fun."

    z "What did you do this week?"

    r "Uhh... A bunch of stuff! It's a little hard to remember the details though..."

    if c_count > 5:
        r "Though I did befriend someone named Claire!"
        r "We're gonna hang out tomorrow."
        z "That's nice."
        r "I don't wanna have a crazy hangover tomorrow cuz of that, so I'll be off early."
        z "Got it."
        r "Speaking of drinking..."
    elif s_count > 5:
        r "Though I did befriend someone named Shamir!"
        r "We're gonna hang out tomorrow."
        z "That's nice."
        r "I don't wanna have a crazy hangover tomorrow cuz of that, so I'll be off early."
        z "Got it."
        r "Speaking of drinking..."
    elif t_count > 5:
        r "Though I did befriend my fellow start Taiga!"
        r "We're gonna hang out tomorrow."
        z "That's nice."
        r "I don't wanna have a crazy hangover tomorrow cuz of that, so I'll be off early."
        z "Got it."
        r "Speaking of drinking..."
    elif h_count > 5:
        r "Though I did befriend someone named Horace!"
        r "We're gonna hang out tomorrow."
        z "That's nice."
        r "I don't wanna have a crazy hangover tomorrow cuz of that, so I'll be off early."
        z "Got it."
        r "Speaking of drinking..."
    else:
        r "I talked to a few people, hopefully, I can get to know them more."

        z "So do you have any weekend plans?"

        r "Nah, not really."

        z "I see... want to meet up then?"

        r "But I do have some movies I'm hoping to catch up on..."

        r "Ahh what the hell! Yeah, I'll turn up this weekend!"

        z "Fantastic."
        
        z "But anyways..."

    r "Wanna start drinking?"

    z "You know it!"

    stop music fadeout 1.0
    scene black
    with fade

    jump ending_morning

label ending_morning:
    stop music fadeout 1.0
    scene bg home
    with fade
    play music "music/home (Morning).wav" fadein 1.0

    "..."

    r "...Ugh"

    "I slowly rise up from bed"

    "instead of falling on the floor for the 5th time in a row."

    if t_count == 6:
        r "Ooh! I gotta get ready for today!"
        jump taigaEnding
    elif c_count == 6:
        r "Ooh! I gotta get ready for today!"
        jump claireEnding
    elif s_count == 6:
        r "Ooh! I gotta get ready for today!"
        if bShamir:
            jump shamirEndingA
        else:
            jump shamirEndingB
    elif h_count == 6:
        r "Ooh! I gotta get ready for today!"
        jump horaceEnding
    else:
        r "I don't really have anything this morning..."
        r "I'll watch some movies before going to the bar with Zeke..."
        jump zekeEnding
    

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
    else:
        python:
            renpy.error("Invalid taiga link!")
label horace:
    if h_count == 1:
        jump horace1
    elif h_count == 2:
        jump horace2
    elif h_count == 3:
        jump horace3
    elif h_count == 4:
        jump horace4
    elif h_count == 5:
        jump horace5
    else:
        python:
            renpy.error("Invalid horace link!")
label shamir:
    if s_count == 1:
        jump shamir1
    elif s_count == 2:
        jump shamir2
    elif s_count == 3:
        jump shamir3
    elif s_count == 4:
        jump shamir4
    elif s_count == 5:
        if bShamir:
            jump shamir5A
        else:
            jump shamir5B
    else:
        python:
            renpy.error("Invalid shamir link!")
label claire:
    if c_count == 1:
        jump claire1
    elif c_count == 2:
        jump claire2
    elif c_count == 3:
        jump claire3
    elif c_count == 4:
        jump claire4
    elif c_count == 5:
        jump claire5
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

    r "I went to Blighty U, and I had a great time there."

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
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    r "Hey Taiga, wanna go get lunch again?"

    show t side at S_C
    with dissolve

    r "To uh, bolster your status higher or whatever?"

    show t front

    t "Fine. Let's go."

    stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
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

    r "Wow, that sounds like a really sad life."

    t "If I wanted to know what a sad life was like, I'd ask you."

    r "Very funny, Taiga."

    t "I wasn't being funny."

    "...ah"

    r "So wait, what do you do once you get off of work?"

    t "I usually work out."

    r "Ah! See? That's something! You like working out!"

    show t side

    t "Working out isn't something I enjoy."

    t "It's something I do to stay in peak mental and physical fitness."

    show t front

    t "Same with my piano playing and cooking."

    t "I play the piano to exercise my mind."
    
    t "And I cook my own meals after workouts to maximize the benefits."

    show t side

    t "And speaking of cooking, if you wanna be more like me Robin..."

    r "Hm?"

    show t front

    t "You should lay off the fast food."

    "I sheepishly put down the burger I was about to shove into my mouth."

    r "Well... that's a very interesting way to lead your life."

    r "Do you derive joy from anything, Taiga"

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

    t "I'm going for a walk."

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
    with fade

    show t front at DS_C
    with dissolve

    t "Did you bring it?"

    r "Yeah, here's the painting."
    
    show t back

    t "..."

    r "Taiga? Mind telling me what's up?"

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

    t "\"Art doesn't make money,\" they said."

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
    with fade
    play music "music/Sludge (Office outside afternoon).wav" fadein 1.0

    show t side at DS_C
    with dissolve

    t "What do you want?"

    r "Here."

    show t front

    t "What's this?"

    r "Two tickets for an art gallery, this Saturday."

    t "{sc}WHAT?!?!?!{/sc}" 

    r "Woah! Calm down there Taiga."

    t "..."

    r "Taiga. You need to stop shelling yourself up like this."

    r "You aren't your parents. You have the right to do what you enjoy."

    r "Even if it's just off hours."

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
    stop music fadeout 1.0
    scene bg artstudio
    with fade
    play music "music/end1.wav" fadein 1.0

    "I took Taiga to an art gallery."

    "The tickets didn't come cheap, but looking at his face made it all worth it."

    show t back at DS_C
    with dissolve

    t "..."

    "I'm basically just tagging along. None of this art really means much to me..."

    t "Robin."

    r "Hm?"

    t "Thank you."

    r "O-Oh yeah! It's no problem."

    r "You can pay me back when you're one of the famous artists up here!"

    show t front

    t "{sc}!{/sc}"

    t "You... You really think I could be a famous artist one day?"

    r "What happened to the confidence?"
    
    r "If you could make it this far in your academic and work life, art should be easy for a guy like you!"

    show t side

    t "..."

    show t back 

    t "..."

    t "Alright. I'll try and get back into art..."

    r "I can't wait to see it, Taiga!"

    stop music fadeout 1.0

    scene black with dissolve

    show text "Ending:\nTaiga" with Pause(3)

    scene black with dissolve

    return

label claire1:
    #Getting help from Claire and talking about work

    stop music fadeout 1.0
    scene bg office:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
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
    with fade

    r "I see! Wow, thank you so much, Claire!"

    show c front at S_C 

    c "No problem, Robin!"

    c "It really is quite easy once it gets explained to you."

    r "It really is..."

    c "But I'm glad I could help, and you can call me anytime you need a hand."

    r "Thanks, Claire!"

    r "You're probably the nicest person here, hands down."

    "And probably the most normal..."

    c "Aww, thanks! I know how nice it is to get the help you need, so why not pay it forward?"

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
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    r "Hey, Claire, wanna go get lunch again today?"

    show c front at S_C
    with dissolve

    c "Sure! Let's head over!"

    stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/gloop (Cafe).wav" fadein 1.0

    show c front at DS_C
    with dissolve

    c "Alright, time to eat!"

    "We start to dig into our food."

    r "So Claire, when did you start working here?"

    c "Oh... about 6 or so years ago?"

    r "Congrats on 6 years, then!"

    r "Do you plan on staying here for a while longer?"

    c "Yeah... probably. I've got a lot of... ties here."

    r "I see... That does come with a lot of benefits!"

    r "You'll probably get a promotion if you haven't already."

    show c side

    c "Yeah... A promotion..."

    r "Is something the matter?"

    c "Nah, don't worry about it."

    show c front

    c "Actually, I have a question for you."

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

        "Hamburgers":
            r "Probably hamburgers can never beat a good smash burger."
            pass
        "Chilaquiles":
            r "Probably Chilaquiles, but only my dad's recipe, for sure."
            pass
        "Moules-Frites":
            r "Definitely Moules-Frites, an unexpectedly fantastic combo."
            pass
        "Maafe":
            r "A long-simmered Maafe with a pile of rice can't be beaten."
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

    r "I have a good college friend, his name is Zeke, and I remember how much my perception of him changed when he said his favorite food was mashed potatoes."

    show c front

    c "Right? Glad you see what I mean."

    show c side

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

    show h front at S_C
    with dissolve

    "Seemingly from the shadows, Horace steps in."

    h "Let me have a look."

    "..."

    show h back

    h "Done. I'll be going then."

    show c front

    c "Hori! Are you gonna stop by without saying hi, darling?"

    h "..."

    h "Why are you still clinging on, Claire?"

    show h front

    h "...Isn't it about time you let go?"

    c "H-Huh?" #sfx here maybe?

    show h side

    h "I'll be seeing you, Robin."

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
    with fade

    show c front at apron
    with dissolve

    r "So what did you want to vent about?"

    c "Alright, so..."

    show c side

    c "..ugh, for once I'm at a loss for words."

    show c front

    c "Let's just start at the beginning. Me and Horace started on the same day."

    c "We were desk to desk and obviously ended up talking a lot."

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

    c "I've heard that one enough from my mom."

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
    with fade
    play music "music/slime (Office Afternoon).wav" fadein 1.0

    show c front at S_C
    with dissolve

    c "Hey, Robin! Down for lunch again today?"

    r "Sure! Let's go!"

    stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/gloop (Cafe).wav" fadein 1.0

    show c front at DS_C
    with dissolve

    c "Y'know, I'm feeling a lot better after our talk last time."

    r "I'm glad to hear it, Claire!"

    c "By the way, would you wanna meet up sometime this weekend?"

    c "We could celebrate your first week of work!"

    "W-Wow, I forgot it's been a week..."

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
    stop music fadeout 1.0
    scene bg bar
    with fade
    play music "music/end1.wav" fadein 1.0

    show c front at DS_C
    with dissolve

    c "Hey! Robin! Over here!"

    r "Oh! Hey Claire!"

    "I have a seat, while Claire passes me a shot."

    r "How has your weekend been so far?"

    c "Great! It's especially picking up now that I've got a few drinks in me!"

    r "Ooh, I better catch up!"

    "I take my shot and push the glass back up the table."

    c "I do have some news..."

    r "Oh? What's that?"

    c "I think I might switch jobs."

    r "What? Why so sudden?"

    c "Well, talking to you kinda made me realize..."

    show c side

    c "I really have been clinging to the past."
    
    c "Smiling and bearing a job that I hate for someone who will never take me back."

    c "Horace will never take me back. I've been running away from that fact for so long now."

    c "It's time for me to move on, y'know?"

    r "I see. Well, even though we've worked together for such a short amount of time... I'll miss you!"

    c "If we make Birdley's a regular haunt together, you'll lose that feeling pretty fast. Trust me."

    r "Hah! Well, we'll see about that."

    r "But hey, cheers to a new life, yeah?"

    c "Yeah... Cheers!"

    stop music fadeout 1.0

    scene black with dissolve

    show text "Ending:\nClaire" with Pause(3)

    scene black with dissolve

    return


label horace1:
    #Talking in their office
    stop music fadeout 1.0
    scene bg officeboss:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/Grime (Boss).wav" fadein 1.0

    show h front at S_C
    with dissolve

    h "..."

    r "..."

    h "Why are you here?"

    r "Oh! I-It's lunch, and I wanted to talk to you."

    show h back

    h "Well, you talked to me. I'll be leaving now."

    r "{sc}W-WAIT!{/sc}"

    show h side

    h "What is it?"

    r "U-Uh, building a strong co-worker relationship is important to a strong company..?"

    h "..."

    show h front

    h "Do you have a source for that?"

    r "N-No but... Let's just try and talk, okay?"

    h "... Fine."

    r "How was your day?"

    show h side

    h "Efficient yet suffocatingly bland with a tinge of abject misery and horror."

    h "Just like the last 10,227 days of my agonizing existence."

    show h front

    h "...How about you..?"

    "..."

    "..."

    "I'm stunned... I can't... say anything..."

    show h side

    h "You're not very good at this talking thing. Hopefully, that isn't on your CV."

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
    with fade
    play music "music/gloop (Cafe).wav" fadein 1.0

    show h front at DS_C

    "..."

    "..."

    r "So... Boss... Are you gonna get any food? You just have a cup of coffee."

    h "No. I won't."

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

    h "Spending hours and hours of time outside of work to write a bunch of made-up characters just sounds like a waste of time."

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
            r "I was enraptured all the way through, excellent work."
            pass
        "It was okay":
            r "This was pretty alright, Boss."
            r "I think it could use a bit of... work..."
            r "But this is a great start!"
            pass
        "It was awful":
            r "I'm not gonna mince words with you, Boss."
            r "This was truly awful."
            r "You know you don't need to end every character dialogue with \"Sincerely, Horace\" right?"
            r "And why did everyone get fired at the end? None of them even worked at a company...??"
            r "You've got a long way to go."
            pass

    h "...I see. I will add this feedback to my report."

    show t front at S_C
    with dissolve

    c "Hey Boss. What's this?"

    "Horace slams the laptop shut"

    show h back

    h "This is a private business affair. Please leave, Taiga."

    show h front

    c "Ah. G-Got it, Boss."

    show t back

    c "See you..."

    hide t back

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

    h "I had befriended a majority of the office and had even started seeing someone."

    "...I honestly can't imagine that."

    show h side

    h "But my work suffered as a result. I was all play and no work."

    h "And one day. My Boss came to me with an ultimatum."

    h "Either focus on my work wholly and gain a large promotion"

    h "...or get laid off."

    h "He saw potential in me and knew that this potential would not be drawn out in my current state."

    show h front

    h "As you can see, I've made my choice."

    h "Additionally, I am currently caring for a lot of people."

    h "I am the \"breadwinner\" so to speak."

    r "So if you got laid off..."

    h "Yes. We would have starved."
    
    h "That is why I keep nobody close."

    show h side

    h "This is why I would also like to say one additional thing"
    
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

    r "I believe you need to have a better work-life balance."

    h "...What?"

    r "You need to learn to balance your life and work more!"

    r "Do stuff outside of work! Talk to your coworkers! Pick up a hobby!"

    h "...Robin, do you know what a work-life balance is?"

    r "{sc}n-no...{/sc} But that's beside the point!"

    r "Horace, I can tell, this is hurting you."

    h "..."

    r "You won't last much longer shutting yourself away like this."

    r "And if you wanna keep working, then you gotta do what's best for you."

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
    stop music fadeout 1.0
    scene bg bar
    with fade
    play music "music/end1.wav" fadein 1.0

    show h front at DS_C
    with dissolve

    h "Hello, Robin."

    r "Hey Horace!"

    r "How's it going?"

    show h side

    h "Ah... You know... The usual..."

    show h front

    h "Sorry. I'm not sure I'm used to this quite yet."

    r "Well, wanna get some drinks? Maybe that'll help loosen us both up."

    h "Well, alcohol being a \"Social Lubricant\" is a common myth."
    
    h "Many act anti-social when inebriated."

    r "So... No drinks?"

    h "I didn't say that. Let's get some beers, on me."

    show h back

    "We both order our beers of choice and are slid two glasses."

    show h front

    h "You've changed a lot in one week, Robin."

    r "I could say the same for you!"

    show h side

    h "Fair enough. I had really thought I surrendered being amicable with my coworkers forever."

    show h front

    h "But I forgot how nice this was."

    r "Here's to not pushing people away anymore, yeah?"

    h "Sure. Cheers."

    stop music fadeout 1.0

    scene black with dissolve

    show text "Ending:\nHorace" with Pause(3)

    scene black with dissolve

    return


label shamir1:
    #Talking to Shamir about day one incident
    stop music fadeout 1.0
    scene bg officefrontdesk:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
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

    s "Like if I was in front of you in a line, I might take a few steps away, you know?"

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
    with fade
    play music "music/Glop (Front Desk afternoon).wav" fadein 1.0

    r "Hey Shamir! Wanna go get lunch?"

    show s front at S_C
    with dissolve

    s "Sure. Again, I owe you after the last time."

    r "L-Let's just drop the \"I owe you\" stuff and get lunch, yeah?"

    s "Sure."

    stop music fadeout 1.0
    scene bg officecafe:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/gloop (Cafe).wav" fadein 1.0

    show s front at DS_C

    r "So Shamir, what do you do outside of work?"

    show s side

    if day > 3:
        s "Like I said earlier..."

    s "I do art, mostly."

    r "Do you sell any of your pieces?"

    show s front

    s "I try to, but it's really hard to sell my art here."

    r "Here? What do you mean?"

    show s side

    s "Ah, I don't think I've ever told you."

    show s front

    s "I'm an immigrant. I came here from overseas."

    r "I see, but what does that have to do with your art?"

    s "Well, my art is very telling of where I came from."

    s "And a lot of people here aren't quite used to that."

    s "Food is one thing, y'know? But are people as likely to buy an expensive painting?"

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
    with fade
    play music "music/Glop (Front Desk afternoon).wav" fadein 1.0

    show s front at S_C
    with dissolve

    r "Hey Shamir! Wanna go get lunch?"

    s "Sure, Robin. Just give me a moment, I need to wrap this up."

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
    with fade

    show s front at apron

    r "So Shamir, what is it you wanted to talk abo-"

    s "You feel it too, don't you?"

    s "Something is wrong here."

    r "..."

    s "I can see it in your eyes, Robin. You feel the same way."

    s "Everyone feels this... unsettling feeling when they first come here."

    s "But everyone slowly forgets."

    s "It's driving me insane."

    s "Every day, I dig into this company more and more."

    s "Yet I feel like I know less and less."

    s "That's why I reacted the way I did around Horace. I really don't trust them at all."

    s "We used to be friends, but one day they came into work dead behind the eyes."

    s "And that was the day Horace got a massive promotion. Their spot here was secured."

    s "Robin. Before you lose your way, get out of here. As soon as you can."

    r "S-Shamir..."

    s "Did you know this company exclusively snatches up college graduates?"

    s "And yet, they never seem to leave this place. They all get caught in its web."

    s "Our biggest department is IT, which is already an anomaly."

    s "And yet, none of our infrastructure is for our work, rather it's to store information about us."

    s "Don't you see it, Robin?"

    "..."

    "..."

    "..."

    s "...heh... I probably sound like a madwoman, don't I?"

    s "We have a few lunches together, and I act weird around a coworker..."

    s "And here I am throwing my conspiracy theories at you."

    s "And I called you a creep. Heh..."

    s "...Robin?"

    r "..?"

    menu:
        s "Do you believe me?"

        "I Do.":
            $ bShamir = True;
            r "I-I believe you, Shamir."

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

            show s front

            s "Robin?"

            r "Y-Yeah?"

            show s back

            s "I'm tired. I really don't know how much more I have left in me."

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

    s "Wanna check out that new art gallery? I have two tickets."

    r "Sounds good! I had been meaning to check that place out!"

    show s side

    s "Fantastic. I'll see you then."

    show s back
    s "For now, I've got something to attend to. We'll save today's chat for then."

    r "Oh! Shamir, before you go..."

    show s front at DS_C
    with dissolve

    s "Hm?"

    r "Never forget that I'm in your corner, okay?"

    show s back

    s "...I won't. Thank you, Robin."

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
    with fade

    show s front at S_C
    with dissolve

    r "So Shamir, how was your day?"

    s "{bt}Ahahahahahaha!{/bt}"

    s "Robin, you're a riot!"

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
    stop music fadeout 1.0
    scene bg artstudio
    with fade
    play music "music/end1.wav" fadein 1.0

    show s front at DS_C
    with dissolve

    s "Hello, Robin."

    r "Hey Shamir!"

    r "Wow... All of these pieces are really beautiful..."

    s "Mhm... I'm here to get some inspiration for my art."

    s "I'm gonna try and get back into selling art."

    s "Er... Well... I kinda have to. Since I quit my job."

    r "Wait, what? You quit?"

    s "Yeah."

    s "Yesterday, when I was leaving, I turned around and looked up at the tower that cast me in a deep shadow."

    s "And I realized... There really is nothing I could do to take down a company like this."

    s "I realized I would keep digging endlessly. While contributing to this place that I actively hate."

    r "I-I see..."

    s "I know I was talking big about finding the truth... But I would rather prioritize my own happiness."

    r "No. I understand! Spending all your time trying to find out what's going on does sound pretty maddening..."

    r "But anyways, want to start walking? We've just been standing at the start..."

    s "Yeah... Let's."

    stop music fadeout 1.0

    scene black with dissolve

    show text "Ending:\nShamir A" with Pause(3)

    scene black with dissolve

    return
label shamirEndingB:
    stop music fadeout 1.0
    scene bg badstudio:
        function WaveShader(period=1, amp=5.0, speed=1, direction='x', repeat="mirror")
    with fade
    play music "music/Lost Deer.mp3" fadein 1.0

    r "Ugh... Wh-What am I doing here..?"

    show z back at apron

    w "Robin?"

    r "Z-Zeke..?"

    w "Come along, Robin."

    w "It's time for us to go."

    r "Where's Shamir?"

    w "Come along, Robin."

    w "It's time for us to go."

    r "Oh..."

    r "Oh yeah..."

    r "It is time for us to go, isn't it?"

    w "Come along, Robin."

    r "Yeah... Alright..."

    show z side

    w "It's spreading quite nicely, isn't it?"

    r "Yeah..."

    "Yeah..."

    "..."
    stop music fadeout 1.0
    scene black with dissolve

    show text "Ending:\nShamir B" with Pause(3)

    scene black with dissolve

    return

label zekeEnding:
    stop music fadeout 1.0
    scene bg bar
    with fade
    play music "music/bar.wav" fadein 1.0

    r "Hey, Zeke!"

    show z front at DS_C
    with dissolve

    z "Hey, Robin."

    show z side

    z "Ready for a second taste of Dom P?"

    r "{sc}No way.{/sc}"

    r "My wallet still hasn't recovered from the first time."

    z "{bt}Ahaha...{/bt}"

    show z front

    z "All in good fun... Robin..."

    r "So... how are you? Anything new?"

    r "I feel like we've just been talking about my problems."

    r "Let's hear more about the wallet-busting Zeke"

    show z side

    z "Ahh... You know how it is. Same old same old."

    r "Don't you have to get a job soon?"

    r "Gotta pay rent and all that, right?"

    show z front

    z "Yeah, but in the meantime, I have my way of keeping my head above water."

    r "I see..."

    z "By the way... You didn't really find yourself getting close with any coworkers this week, right?"

    r "Oh! Yeah, I suppose so."

    show z side

    z "I see.., That's good..."

    r "That's good?"

    show z front

    z "Ah, yeah. Because I was scared I was losing my bill footing buddy!"

    r "Screw you, man."

    z "Heh, and speaking of the bill... Let's start making one, shall we?"

    r "Heh, sounds good."

    stop music fadeout 1.0

    scene black with dissolve

    show text "Ending:\nZeke / Neutral" with Pause(3)

    scene black with dissolve

    return