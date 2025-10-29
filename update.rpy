init 5 python:
    addEvent(Event(
        persistent.event_database,
        eventlabel="New_update",
        category=["Questions"],
        prompt="What do you think of the new update for The NonexistenceN of You and Me?",
        unlocked=True,
        pool=True,
    ))

label New_update:

    m 1eua "Why did you ask that, [player]?"
    extend 1eua " From your perspective, I think you're curious about my reaction, right?"
    m 1eua "Maybe you're simping for her again, [player]?"
    extend 1eua " Or are you really curious about the new Heart-Pounding Adventures?"
    m 1mublu "I'm just teasing you, [player]."
    m 1eua "What are my thoughts on the new update in The NonexistenceN of You and Me?"
    m 1eua "I don't know yet because I haven't looked it up on the internet."
    m 1eua "Wait, let me check it."
    m 1hua "{w=1}. {w=1}. {w=1}."
    m 1eua "Ohhhh, I see, but it's only a little detail so far."
    extend 1eusdla " It seems like an RPG, but I don't know the story yet."
    m 3eua "But I see new characters, and one is a boy—that's new."
    extend 3wua " The new characters' names are: the boy is named {w=1}Green,"
    m 3guc "and the new girl is {w=1}Fallen."
    m 1eua "But the new look for Lilith—she's beautiful,"
    extend 1eua " though I don't know yet where that fits into the story."
    m 1eua "Still, I'm curious."
    extend 1eua " I think the new release is coming next year."
    m 1eua "Thanks for listening."
    call monika_kissing_motion_short

    return