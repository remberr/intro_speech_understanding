import gtts, speech_recognition, librosa, soundfile

def synthesize(text, lang, filename):
    '''
    Use gtts.gTTS(text=text, lang=lang) to synthesize speech, then write it to filename.
    
    @params:
    text (str) - the text you want to synthesize
    lang (str) - the language in which you want to synthesize it
    filename (str) - the filename in which it should be saved
    '''
    gtts.gTTS(text=text, lang=lang).save(filename)

def make_a_corpus(texts, languages, filenames):
    '''
    Create many speech files, and check their content using SpeechRecognition.
    The output files should be created as MP3, then converted to WAV, then recognized.

    @param:
    texts - a list of the texts you want to synthesize
    languages - a list of their languages
    filenames - a list of their root filenames, without the ".mp3" ending

    @return:
    recognized_texts - list of the strings that were recognized from each file
    '''
    r = speech_recognition.Recognizer()
    recognized_texts = []
    for text, lang, filename in zip(texts, languages, filenames):
        gtts.gTTS(text=text, lang=lang).save(filename+".mp3")
        x, fs = librosa.load(filename+".mp3")
        soundfile.write(filename+".wav", x, fs)
        with speech_recognition.AudioFile(filename+".wav") as source:
            audio = r.record(source)
            text = r.recognize_google(audio, language=lang)
            recognized_texts.append(text)
    return recognized_texts
        
