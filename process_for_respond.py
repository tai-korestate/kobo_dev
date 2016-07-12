
def process(speech_act):
    if "furniture" in speech_act:
        return "We have a great selection of furniture at korestate dot com"

    elif "hello" in speech_act:
        return "Hello to you too!"

    else:
        return "You said %s" % speech_act


