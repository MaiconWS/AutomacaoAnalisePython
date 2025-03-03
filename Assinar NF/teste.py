import pyscreeze

localizar = pyscreeze.locateOnScreen('img/logo.png', grayscale=True, confidence=0.8)
print(localizar)
