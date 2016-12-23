class WordMath():

  def __init__ (self):
    self.units = self.getUnits()
    self.tens = self.getTens()
    self.scales = self.getScales()

  def textToInteger(self, textnum, numwords={}):
    if not numwords:
      self.units
      self.tens
      self.scales

    numwords["and"] = (1, 0)

    for idx, word in enumerate(self.units):
      numwords[word] = (1, idx)

    for idx, word in enumerate(self.tens):
      numwords[word] = (1, idx * 10)

    for idx, word in enumerate(self.scales):
      numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0

    for word in textnum.split():
      if word not in numwords:
        raise Exception("Illegal word: " + word)

      scale, increment = numwords[word]
      current = current * scale + increment
      if scale > 100:
        result += current
        current = 0

    return result + current

  def getUnits(self):
    return [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

  def getTens(self):
    return [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
        "eighty", "ninety"
      ]

  def getScales(self):
    return [
        "hundred", "thousand", "million", "billion", "trillion"
      ]