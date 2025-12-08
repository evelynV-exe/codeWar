def validate_hello(greetings):
    greeting = {'hallo', 'hello', 'ciao', 'salut', 'hola', 'ahoj', 'czesc'}
    return any(word in greetings.lower() for word in greeting)
