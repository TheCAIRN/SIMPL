class SIMPL_Frontend:
    import TheActualOne as p
    parser = p.Parser()

    from pocketsphinx import LiveSpeech
    for phrase in LiveSpeech():
        p.input(phrase)

    def Pcode(s):
        print(s)

    def Scode(s):
        engine = speake3.Speake()  # Initialize the speak engine
        engine = speake3.Speak()
        engine.set('voice', 'en')
        engine.set('speed', '107')
        engine.set('pitch', '99')
        engine.say(s)  # String to be spoken
        engine.talkback()
