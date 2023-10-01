def write_multiple_items(file, seperator, *args):
    file.write(seperator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)
concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")
