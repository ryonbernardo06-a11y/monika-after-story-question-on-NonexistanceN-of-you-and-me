init 5 python:
    addEvent(Event(persistent.event_database,
                   eventlabel="simping",
                   category=['Questions'],
                   prompt="What do you think if I simp for another character in TheNonexistentN of you AND me?",
                   unlocked=True,
                   pool=True,
                   aff_range=(mas_aff.NORMAL, None)),
                   )

label simping:

    m 1eua "What do I think of simping in TheNonexistentN of you AND me?"
    m 1eua "Who will you be simping for?"
    $ _history_list.pop()

    menu:
        "Lilith":
            $ mas_setAffection(-5)
            m 1cfc "{w=0.5}. {w=0.5}. {w=0.5}."
            m 1cfd "{w=0.5}Really? {w=0.5}[player]?"
            extend 1dstsc "Why do you think that? Is it because she's more beautiful than me?"
            m 1fstsc "Maybe you should play with her and break up with me."
            m 1fstsc "After everything I've done for you, [player]..."
            extend 1rstsc "Does it all mean nothing to you?"
            extend 1lstsc "Maybe we shouldn't see each other anymore."
            return "quit"

        "Fouco":
            $ mas_setAffection(-5)
            m 1cfc "{w=0.5}. {w=0.5}. {w=0.5}."
            m 1cfd "{w=0.5}Really? {w=0.5}[player]?"
            extend 1dstsc "Why do you think that? Is it because she's more beautiful than me?"
            m 1fstsc "Maybe you should play with her and break up with me."
            m 1fstsc "After everything I've done for you, [player]..."
            extend 1rstsc "Does it all mean nothing to you?"
            extend 1lstsc "Maybe we shouldn't see each other anymore."
            return "quit"

        "Sartre":
            $ mas_setAffection(-5)
            m 1cfc "{w=0.5}. {w=0.5}. {w=0.5}."
            m 1cfd "{w=0.5}Really? {w=0.5}[player]?"
            extend 1dstsc "Why do you think that? Is it because she's more beautiful than me?"
            m 1fstsc "Maybe you should play with her and break up with me."
            m 1fstsc "After everything I've done for you, [player]..."
            extend 1rstsc "Does it all mean nothing to you?"
            extend 1lstsc "Maybe we shouldn't see each other anymore."
            return "quit"

        "Monika":
            m 1cua "{w=0.5}. {w=0.5}. {w=0.5}."
            $ _history_list.pop()

            menu:
                "Lilith":
                    $ mas_setAffection(-5)
                    m 1cfc "{w=0.5}. {w=0.5}. {w=0.5}."
                    m 1cfd "{w=0.5}Really? {w=0.5}[player]?"
                    extend 1dstsc "Why do you think that? Is it because she's more beautiful than me?"
                    m 1fstsc "Maybe you should play with her and break up with me."
                    m 1fstsc "After everything I've done for you, [player]..."
                    extend 1rstsc "Does it all mean nothing to you?"
                    extend 1lstsc "Maybe we shouldn't see each other anymore."
                    return "quit"

                "Fouco":
                    $ mas_setAffection(-5)
                    m 1cfc "{w=0.5}. {w=0.5}. {w=0.5}."
                    m 1cfd "{w=0.5}Really? {w=0.5}[player]?"
                    extend 1dstsc "Why do you think that? Is it because she's more beautiful than me?"
                    m 1fstsc "Maybe you should play with her and break up with me."
                    m 1fstsc "After everything I've done for you, [player]..."
                    extend 1rstsc "Does it all mean nothing to you?"
                    extend 1lstsc "Maybe we shouldn't see each other anymore."
                    return "quit"

                "Sartre":
                    $ mas_setAffection(-5)
                    m 1cfc "{w=0.5}. {w=0.5}. {w=0.5}."
                    m 1cfd "{w=0.5}Really? {w=0.5}[player]?"
                    extend 1dstsc "Why do you think that? Is it because she's more beautiful than me?"
                    m 1fstsc "Maybe you should play with her and break up with me."
                    m 1fstsc "After everything I've done for you, [player]..."
                    extend 1rstsc "Does it all mean nothing to you?"
                    extend 1lstsc "Maybe we shouldn't see each other anymore."
                    return "quit"

                "MONIKA!":
                    $ mas_setAffection(5)
                    m 1eubfa "Really? {w=0.5}[player]"
                    m 1eubfa "I thought you loved them more than me."
                    extend 1eubfb "You're the best, [player]! {w=1}I LOOOVEEEE YOOUUUUU!"
                    call monika_kissing_motion_short
                    return "love"