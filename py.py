def func1(word):
    info = "welcome to python training in telugu"
    if word in info.split():
        print(f'{word} exists in the string')
    else:
        print(f'{word} DOnt Exists')

func1("to")
func1("python")