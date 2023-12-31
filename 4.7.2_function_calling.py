def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "/")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

    # It could be called like this:
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir",
           shopkeeper="Michale Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
    