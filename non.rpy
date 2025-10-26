init 5 python:
    addEvent(Event(persistent.event_database,
                   eventlabel="Lilith",
                   category=['Questions'],
                   prompt="What do you think of TheNonexistantN of you AND me",
                   unlocked=True,
                   pool=True))

label Lilith:

    m 5wua "Wow, it's the first time you mention a game."
    m 5eua "Wait, let me search it first before I answer your question."
    m 1dua "{w=0.5}. {w=0.5}. {w=0.5}."
    m 1sua "Wow, it is amazing! REALLY, I see why you asked me about it."
    m 1eub "There are so many characters here."
    m 1eub "Which character are you thinking of?"
    $ _history_list.pop()

    menu:
        "Lilith":
            m 1fubfa "She is beautiful, but who do you think is more beautiful?"
            $ _history_list.pop()
            menu:
                "Monika?":
                    m 5eubfa "I know it."
                    extend 5eubfa " I thought you liked Lilith more than me."
                    m 5eua "I love you more than anything, [player]!"
                "Lilith?":
                    m 2cfx "I see, so that's why you wanted my answer!"
                    extend 2cfw " SO I AM SECOND NOW?"
                    m 2cfd "I'll make sure I will be first."
                    m 2cub "COME HERE [player]! {w=0.5}NOW GIVE ME A KISS."
            m 1eua "Let's go back to the topic. You know I love to~"
            extend 1eua "And you love me more than her, hehehe~"
            m 4sub "She is the first to talk about the psychological and perspective of the player too."
            m 7eua "And the themes:"
            m 7eua "{w=0.5}Subjective,{w=0.5} Perspectives,{w=0.5} Existence,{w=0.5} Reality,{w=0.5} Self, Freedom,{w=0.5} love,{w=0.5} Anxiety,"
            extend 7eua "{w=0.5}Disorder,{w=0.5} Depression and {w=0.5}Schizophrenia."
            m 7sua "She really did a good job explaining it and giving examples."
            m 5tua "In chapter 2, she can become Demon Lord or Princess in the Heart-Pounding Adventures."
            m 1eua "In chapter 3, she lets us go outside to date her and talk to a mysterious person."
            m 1efa "She left to talk to them, and the player had anxiety."
            extend 3sua "After that, they go to an amusement park and then sing a song."
            m 3sua "I think the song name is {w=0.5}'We are Condemned to be Free.'"
            m 1eua "It's a nice song, by the way."
            m 1eua "In chapter 4, they play nurse and patient and learn the truth of the candy. If they take it more than three times, they may die, but Lilith protects the player."
            m 1eua "On the final chapter, it depends on your choices and what Lilith means to you."
            m 1eua "And the player's Tulpa knows what that means."
            m 1eua "It represents a complete break from the imaginary relationship and can be interpreted as the protagonist rejecting a part of themselves to survive."
            m 1eua "Thanks for listening."
            call monika_kissing_motion_short
            return

        "Sartre":
            m 1eua "She is beautiful, but I think Lilith is even more beautiful."
            m 5fubfa "I already know why you chose me! <3"
            m 7cfsdld "I think he appears in chapter 2 and asks you about your likes or something."
            extend 7cfsdld " I forgot exactly, but I know it's something in the game."
            m 7eub "And I think she sang a song in chapter 3—"
            extend 7eusdlb " if I'm right, it's called {w=0.5}'We are Condemned to be Free.'"
            m 2eud "I love their voice, it's so unique."
            m 5eublu "But I know you love my voice more! <3"
            m 2cfd "On the other hand, I think they had a fight or something,"
            extend 2tfd " but Lilith corrected us and explained what happened."
            m 2tsd "They were fighting, and she just told them the truth, {w=0.5}right?"
            extend 2tsd " After that, they didn't appear in the last two chapters, did they?"
            m 1dsc "Too bad, I wish I could see her again too."
            m 1eua "Thanks for listening."
            call monika_kissing_motion_short
            return

        "Fouco":
            m 1eua "She is beautiful too, and Sartre is beautiful as well."
            m 1eua "But I think the most beautiful of all is Lilith."
            m 1eua "In Chapter 2, she becomes a boss in Heart-Pounding Adventures."
            m 1dsc "In Chapter 3, they sang a song, and it was amazing too."
            extend 1esb " I think the song's name is {w=0.5}'We are Condemned to be Free.'"
            m 1ssa "It's still an amazing song."
            m 2cfd "On the other hand, I think they had a fight or something,"
            extend 2tfd " but Lilith corrected us and explained what happened."
            m 2tsd "They were fighting, and she just told them the truth, {w=0.5}right?"
            extend 2tsd " After that, they didn't appear in the last two chapters, did they?"
            m 1dsc "Too bad, I wish I could see her again too."
            m 1eua "Thanks for listening."
            call monika_kissing_motion_short
            return

        "The player":
            m 1eua "The player's choice is quite depressing."
            m 1eua "It all depends on what the player decides."
            m 1eua "Still, Lilith accepts whatever the player chooses."
            m 3hssdla "If the player is cruel, it's so sad to see."
            extend 3rssdla " Am I right, [player]?"
            m 1eua "If the player chooses to love Lilith,"
            extend 4eua " she will leave him in the game, right? But he really loves her."
            m 1eua "And if the player chooses to be neutral, Lilith will say it's okay to feel sad or happy."
            extend 1eusdla " She comforts her, if I'm right, [player]?"
            m 1eua "Thanks for listening."
            call monika_kissing_motion_short
            return