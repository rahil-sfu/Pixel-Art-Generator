 # Final Project: Pixel Art Generator


import image_helpers
#################################################
def exit(name, cost):
  if cost > 0:
    print("Thank you ", name, "for using this tool")
    print("Your Total cost is ", cost) 
  else:
    print("Sorry, " + name + " that you did not use the tool - next time!")
  print("Before you leave!")
  print("your special number is ", lucky_number(name, 0, cost))
  return 0
#################################################
def hexcolor_to_RGB_list(name, cost):
  flag = True
  print("Converting hex color to list RGB")
  print("Please enter a valid hex coded number: ")
  while flag:
    inpp = input()
    inp = inpp.upper()

    if len(inp) != 7:
      print("Sorry, this is not a valid hex number")
      print("Please try again")
      continue

    if inp[0] != "#":
      print("Sorry, this is not a valid hex number")
      print("Please try again")
      continue

    while_continuer = False
    for i in range(1, len(inp) - 1):
      if inp[i] != "0" and inp[i] != "1" and inp[i] != "2" and inp[i] != "3" and inp[i] != "4" and inp[i] != "5" and inp[i] != "6" and inp[i] != "7" and inp[i] != "8" and inp[i] != "9" and inp[i] != "A" and inp[i] != "B" and inp[i] != "C" and inp[i] != "D" and inp[i] != "E" and inp[i] != "F":
        print("Sorry, this is not a valid hex number")
        print("Please try again")
        while_continuer = True
        break
    if while_continuer == True:      
      continue
    
    newInp = ""
    decList = [0,0,0]
    j = 0
    for i in range(0,len(inp) - 1, 2):
      newInp += inp[i+1]
      newInp += inp[i+2]
      print(newInp)
      i = int(newInp, 16)
      decList[j] = i
      j += 1
      newInp = ""

    print("The RGB value for ", inpp, " is: ", decList)
    flag = False

    
    print("Your cost was increased by ", cost_calculator(1,"0"))
    print("Your cost so far is", cost + cost_calculator(1,"0"))
    print("Would you like to use the tool again? Please indicate your option")
    cost = cost + cost_calculator(1, "0")
    starter(name, cost)
#########################################    
def hexTorgb(inp):
  newInp = ""
  decList = [0,0,0]
  j = 0
  for i in range(0,len(inp) - 1, 2):
    newInp += inp[i+1]
    newInp += inp[i+2]
    i = int(newInp, 16)
    decList[j] = i
    j += 1
    newInp = ""

  return decList

#################################################
def basic_poster(name,cost):
  print("There is only one possible input data file: basic.csv")
  print("Generated Poster: poster-basic.jpg")

  file = open("Pixel_art_input_csv_files/basic.csv")
  counter = 0
  for line in file:
    counter += 1
  for i in range(0):
    line = file.readline()
  listline = line.split(",")
  print("Number of hex code in the row ", len(listline))
  
  img = image_helpers.getImage("Images/200x200.png")  
  k = 0
  for i in range(len(listline)-1):
    for j in range(len(listline)-1):
      pixel = img[j][i]
      convert = hexTorgb(listline[k])
      pixel[0] = convert[0]
      pixel[1] = convert[1]
      pixel[2] = convert[2]
      k += 1
      if k == len(listline)-1:
        k = 0

  newImage = img
  image_helpers.showImage(newImage)
  image_helpers.saveImage(newImage, "poster-basic.jpg")

  print("Your cost was increased by ", cost_calculator(2,"0"))
  print("Your cost so far is", cost + cost_calculator(2,"0"))
  print("Would you like to use the tool again? Please indicate your option")
  cost = cost + cost_calculator(2,"0")
  starter(name, cost)
##################################################
def rowReader(file, row, col):
  file.seek(0)
  for i in range(row):
    line = file.readline()

  newline = line.split(",")
  return newline[col]
#####################################################
def grayscale(pixels):
  r = pixels[0]
  g = pixels[1]
  b = pixels[2]
  average = int((r + g + b)/3)
  pixels[0] = average
  pixels[1] = average
  pixels[2] = average
  return pixels
################################################
def redBars(inp, counter, img):
  barsCount = 0
  if inp == "wide":
    if counter < 75:
      return img
    else:
      numofbars = int(len(img)/75)
      start = 0
      end = 75
      while True:
        for i in range(0, counter-1):
          for j in range(start, end-1):
            pixel  = img[j][i]
            pixel[0] = pixel[0]+100
            if pixel[0] > 255:
              pixel[0] = 255
            pixel[1] = pixel[1]-100
            if pixel[1] < 0:
              pixel[1] = 0
            pixel[2] = pixel[2]-100
            if pixel[2] < 0:
              pixel[2] = 0
        barsCount += 1
        if barsCount == numofbars:
          break
        start = end + 75
        end = end + 150
        if end > len(img):
          end =end - end % len(img)
    return img

  else:
    numofbars = int(len(img)/15)
    start = 0
    end = 15
    while True:
      for i in range(0, counter-1):
        for j in range(start, end-1):
          pixel  = img[j][i]
          pixel[0] = pixel[0]+100
          if pixel[0] > 255:
            pixel[0] = 255
          pixel[1] = pixel[1]-100
          if pixel[1] < 0:
            pixel[1] = 0
          pixel[2] = pixel[2]-100
          if pixel[2] < 0:
            pixel[2] = 0
      barsCount += 1
      if barsCount == numofbars:
        break
      start = end + 15
      end = end + 30
      if end > len(img):
        end =end - end % len(img)
  return img
################################################
def pictureAssi(file, img, effect):
  counter = 0
  for line in file:
    counter += 1

  listline = line.split(",")  
  print("Number of rows in csv file ", counter)  
  print("Number of hex code in the row ", len(listline))

  k = 0
  for i in range(len(listline)-1):
    for j in range(len(listline)-1):
      pixel = img[j][i]
      convert = hexTorgb(rowReader(file, i+1, j))
      pixel[0] = convert[0]
      pixel[1] = convert[1]
      pixel[2] = convert[2]
      if effect == "grey":
        pixel = grayscale(pixel)
      k += 1
      if k == len(listline)-1:
        k = 0

  if effect == "red":
    print("Please, specify the type of bar effect you want.")
    print("- narrow")
    print("- wide")
    inp = input()
    pixel = redBars(inp, counter, img)

  return img
#################################################
def genPoster(inp, num, effect):
  if effect == "grey":
    effect = "grey"
  elif effect == "red":
    effect = "bars"
  else:
    effect = "original"
  print("Generated Poster: poster-", effect ,"-",inp,"-",num,".jpg")
#################################################
def pixel_art_poster(name, cost, effect):
  print(" Creating a Pixel Art Poster ")
  
  print("Please choose the pixel art that you want to make a poster of: ")
  print("- cactus")
  print("- flamingo")
  print("- giraffe")
  print("- house")
  print("- parrot")
  print("- tree")

  print("To select, type the art name (upper or lower case is ok)")
  inp = input().lower()
  if inp != "cactus" and inp != "flamingo" and inp != "giraffe" and inp != "house" and inp != "parrot" and inp != "tree":
    print("The Art you indicated is not available. Try another option")
    starter(name, cost)
  elif inp == "house":
    print("Please choose the size of your house poster(in pixels")
    print("- 50")
    print("- 100")
    print("- 200")
    print("- 400")
    print("- 800")

    print("To select, type the exact number provided. The poster will be a square.")
    num = input()
    if num != "50" and num != "100" and num != "200" and num != "400" and num != "800":
      print("The size you indicated is not available. Try another option")
      starter(name, cost)
    elif num == "50":
      file = open("Pixel_art_input_csv_files/house-50.csv")
      img = image_helpers.getImage("Images/50x50.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-house-50.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-house-50.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-house-50.jpg")        
    elif num == "100":
      file = open("Pixel_art_input_csv_files/house-100.csv")
      img = image_helpers.getImage("Images/100x100.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-house-100.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-house-100.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-house-100.jpg")  
    elif num == "200":
      file = open("Pixel_art_input_csv_files/house-200.csv")
      img = image_helpers.getImage("Images/200x200.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-house-200.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-house-200.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-house-200.jpg")  
    elif num == "400":
      file = open("Pixel_art_input_csv_files/house-400.csv")
      img = image_helpers.getImage("Images/400x400.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-house-400.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-house-400.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-house-400.jpg")  
    else:
      file = open("Pixel_art_input_csv_files/house-800.csv")
      img = image_helpers.getImage("Images/800x800.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-house-800.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-house-800.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-house-800.jpg")  

    genPoster(inp, num, effect)
    print("Your cost was increased by ", cost_calculator(3,num))
    print("Your cost so far is", cost + cost_calculator(3,num))
    print("Would you like to use the tool again? Please indicate your option")
    cost = cost + cost_calculator(3,num)
    starter(name, cost)
  elif inp == "cactus":
    print("Please choose the size of your house poster(in pixels")
    print("- 50")
    print("- 100")
    print("- 200")
    print("- 400")
    print("- 800")

    print("To select, type the exact number provided. The poster will be a square.")
    num = input()
    if num != "50" and num != "100" and num != "200" and num != "400" and num != "800":
      print("The size you indicated is not available. Try another option")
      starter(name, cost)
    elif num == "50":
      file = open("Pixel_art_input_csv_files/cactus-50.csv")
      img = image_helpers.getImage("Images/50x50.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-cactus-50.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-cactus-50.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-cactus-50.jpg")  

    elif num == "100":
      file = open("Pixel_art_input_csv_files/cactus-100.csv")
      img = image_helpers.getImage("Images/100x100.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-cactus-100.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-cactus-100.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-cactus-100.jpg")  
    elif num == "200":
      file = open("Pixel_art_input_csv_files/cactus-200.csv")
      img = image_helpers.getImage("Images/200x200.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-cactus-200.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-cactus-200.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-cactus-200.jpg")  
    elif num == "400":
      file = open("Pixel_art_input_csv_files/cactus-400.csv")
      img = image_helpers.getImage("Images/400x400.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-cactus-400.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-cactus-400.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-cactus-400.jpg")  
    else:
      file = open("Pixel_art_input_csv_files/cactus-800.csv")
      img = image_helpers.getImage("Images/800x800.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-cactus-800.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-cactus-800.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-cactus-800.jpg")  
    genPoster(inp, num, effect)
    print("Your cost was increased by ", cost_calculator(3,num))
    print("Your cost so far is", cost + cost_calculator(3,num))
    print("Would you like to use the tool again? Please indicate your option")
    cost = cost + cost_calculator(3,num)
    starter(name, cost)
  elif inp == "flamingo":
    print("Please choose the size of your house poster(in pixels")
    print("- 50")
    print("- 100")
    print("- 200")
    print("- 400")
    print("- 800")

    print("To select, type the exact number provided. The poster will be a square.")
    num = input()
    if num != "50" and num != "100" and num != "200" and num != "400" and num != "800":
      print("The size you indicated is not available. Try another option")
      starter(name, cost)
    elif num == "50":
      file = open("Pixel_art_input_csv_files/flamingo-50.csv")
      img = image_helpers.getImage("Images/50x50.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-flamingo-50.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-flamingo-50.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-flamingo-50.jpg")  

    elif num == "100":
      file = open("Pixel_art_input_csv_files/flamingo-100.csv")
      img = image_helpers.getImage("Images/100x100.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-flamingo-100.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-flamingo-100.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-flamingo-100.jpg")  
    elif num == "200":
      file = open("Pixel_art_input_csv_files/flamingo-200.csv")
      img = image_helpers.getImage("Images/200x200.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-flamingo-200.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-flamingo-200.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-flamingo-200.jpg")  
    elif num == "400":
      file = open("Pixel_art_input_csv_files/flamingo-400.csv")
      img = image_helpers.getImage("Images/400x400.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-flamingo-400.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-flamingo-400.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-flamingo-400.jpg")  
    else:
      file = open("Pixel_art_input_csv_files/flamingo-800.csv")
      img = image_helpers.getImage("Images/800x800.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-flamingo-800.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-flamingo-800.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-flamingo-800.jpg")  
    genPoster(inp, num, effect)
    print("Your cost was increased by ", cost_calculator(3,num))
    print("Your cost so far is", cost + cost_calculator(3,num))
    print("Would you like to use the tool again? Please indicate your option")
    cost = cost + cost_calculator(3,num)
    starter(name, cost)
  elif inp == "giraffe":
    print("Please choose the size of your house poster(in pixels")
    print("- 50")
    print("- 100")
    print("- 200")
    print("- 400")
    print("- 800")

    print("To select, type the exact number provided. The poster will be a square.")
    num = input()
    if num != "50" and num != "100" and num != "200" and num != "400" and num != "800":
      print("The size you indicated is not available. Try another option")
      starter(name, cost)
    elif num == "50":
      file = open("Pixel_art_input_csv_files/giraffe-50.csv")
      img = image_helpers.getImage("Images/50x50.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-giraffe-50.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-giraffe-50.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-giraffe-50.jpg")  

    elif num == "100":
      file = open("Pixel_art_input_csv_files/giraffe-100.csv")
      img = image_helpers.getImage("Images/100x100.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-giraffe-100.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-giraffe-100.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-giraffe-100.jpg")  
    elif num == "200":
      file = open("Pixel_art_input_csv_files/giraffe-200.csv")
      img = image_helpers.getImage("Images/200x200.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-giraffe-200.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-giraffe-200.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-giraffe-200.jpg")  
    elif num == "400":
      file = open("Pixel_art_input_csv_files/giraffe-400.csv")
      img = image_helpers.getImage("Images/400x400.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-giraffe-400.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-giraffe-400.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-giraffe-400.jpg")  
    else:
      file = open("Pixel_art_input_csv_files/giraffe-800.csv")
      img = image_helpers.getImage("Images/800x800.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-giraffe-800.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-giraffe-800.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-giraffe-800.jpg")  
    genPoster(inp, num, effect)
    print("Your cost was increased by ", cost_calculator(3,num))
    print("Your cost so far is", cost + cost_calculator(3,num))
    print("Would you like to use the tool again? Please indicate your option")
    cost = cost + cost_calculator(3,num)
    starter(name, cost)
  elif inp == "parrot":
    print("Please choose the size of your house poster(in pixels")
    print("- 50")
    print("- 100")
    print("- 200")
    print("- 400")
    print("- 800")

    print("To select, type the exact number provided. The poster will be a square.")
    num = input()
    if num != "50" and num != "100" and num != "200" and num != "400" and num != "800":
      print("The size you indicated is not available. Try another option")
      starter(name, cost)
    elif num == "50":
      file = open("Pixel_art_input_csv_files/parrot-50.csv")
      img = image_helpers.getImage("Images/50x50.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-parrot-50.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-parrot-50.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-parrot-50.jpg")  

    elif num == "100":
      file = open("Pixel_art_input_csv_files/parrot-100.csv")
      img = image_helpers.getImage("Images/100x100.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-parrot-100.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-parrot-100.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-parrot-100.jpg")  
    elif num == "200":
      file = open("Pixel_art_input_csv_files/parrot-200.csv")
      img = image_helpers.getImage("Images/200x200.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-parrot-200.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-parrot-200.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-parrot-200.jpg")  
    elif num == "400":
      file = open("Pixel_art_input_csv_files/parrot-400.csv")
      img = image_helpers.getImage("Images/400x400.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-parrot-400.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-parrot-400.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-parrot-400.jpg")  
    else:
      file = open("Pixel_art_input_csv_files/parrot-800.csv")
      img = image_helpers.getImage("Images/800x800.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-parrot-800.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-parrot-800.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-parrot-800.jpg")  
    genPoster(inp, num, effect)
    print("Your cost was increased by ", cost_calculator(3,num))
    print("Your cost so far is", cost + cost_calculator(3,num))
    print("Would you like to use the tool again? Please indicate your option")
    cost = cost + cost_calculator(3,num)
    starter(name, cost)
  else:
    print("Please choose the size of your house poster(in pixels")
    print("- 50")
    print("- 100")
    print("- 200")
    print("- 400")
    print("- 800")

    print("To select, type the exact number provided. The poster will be a square.")
    num = input()
    if num != "50" and num != "100" and num != "200" and num != "400" and num != "800":
      print("The size you indicated is not available. Try another option")
      starter(name, cost)
    elif num == "50":
      file = open("Pixel_art_input_csv_files/tree-50.csv")
      img = image_helpers.getImage("Images/50x50.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-tree-50.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-tree-50.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-tree-50.jpg")  

    elif num == "100":
      file = open("Pixel_art_input_csv_files/tree-100.csv")
      img = image_helpers.getImage("Images/100x100.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-tree-100.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-tree-100.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-tree-100.jpg") 
    elif num == "200":
      file = open("Pixel_art_input_csv_files/tree-200.csv")
      img = image_helpers.getImage("Images/200x200.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-tree-200.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-tree-200.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-tree-200.jpg") 
    elif num == "400":
      file = open("Pixel_art_input_csv_files/tree-400.csv")
      img = image_helpers.getImage("Images/400x400.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-tree-400.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-tree-400.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-tree-400.jpg") 
    else:
      file = open("Pixel_art_input_csv_files/tree-800.csv")
      img = image_helpers.getImage("Images/800x800.png")
      newImage = pictureAssi(file, img, effect)
      image_helpers.showImage(newImage)
      if effect == "grey":
        image_helpers.saveImage(newImage, "poster-grey-tree-800.jpg")
      elif effect == "red":
        image_helpers.saveImage(newImage, "poster-bars-tree-800.jpg")
      else:
        image_helpers.saveImage(newImage, "poster-original-tree-800.jpg")  
    genPoster(inp, num, effect)

    calcost = cost_calculator(3,num)
    if effect == "red":
      calcost = 2*calcost

    print("Your cost was increased by ", calcost)
    print("Your cost so far is", cost + calcost)
    print("Would you like to use the tool again? Please indicate your option")
    cost = cost + calcost
    starter(name, cost)

#################################################
def greyscale_pixel_art_poster(name, cost):
  print("Greyscale Pixel Art Poster")
  effect = "grey"
  pixel_art_poster(name, cost, effect)
#################################################
def PixelArtPoster_with_shades_of_redbarseffect(name, cost):
  print("Creating a Pixel poster, with red bars")
  effect = "red"
  pixel_art_poster(name, cost, effect)
##########################################
def horizontalBar(file):
  counter = 0
  for line in file:
    counter += 1
  listline = line.split(",")
  print("Number of hex code in the row ", len(listline))
  img = image_helpers.getImage("Images/500x100.png")  
  for i in range(99):
    for j in range(0,99):
      pixel = img[j][i]
      convert = hexTorgb(listline[0])
      pixel[0] = convert[0]
      pixel[1] = convert[1]
      pixel[2] = convert[2]
  for i in range(99):
    for j in range(100,199):
      pixel = img[j][i]
      convert = hexTorgb(listline[1])
      pixel[0] = convert[0]
      pixel[1] = convert[1]
      pixel[2] = convert[2]
  for i in range(99):
    for j in range(200,299):
      pixel = img[j][i]
      convert = hexTorgb(listline[2])
      pixel[0] = convert[0]
      pixel[1] = convert[1]
      pixel[2] = convert[2]
  for i in range(99):
    for j in range(300,399):
      pixel = img[j][i]
      convert = hexTorgb(listline[3])
      pixel[0] = convert[0]
      pixel[1] = convert[1]
      pixel[2] = convert[2]
  for i in range(99):
    for j in range(400,499):
      pixel = img[j][i]
      convert = hexTorgb("#FF00FF")
      pixel[0] = convert[0]
      pixel[1] = convert[1]
      pixel[2] = convert[2]
  return img
#################################################
def HorizontalBar_Scaledposter(name, cost):
  file = open("Pixel_art_input_csv_files/color-bar.csv")
  print("There is only one possible input data file: color-bar.csv")
  print("Generated Poster: poster-color-basic.jpg")

  newImage = horizontalBar(file)
  image_helpers.showImage(newImage)
  image_helpers.saveImage(newImage, "poster-color-basic.jpg")

  print("Your cost was increased by ", cost_calculator(6,"0"))
  print("Your cost so far is", cost + cost_calculator(6,"0"))
  print("Would you like to use the tool again? Please indicate your option")
  cost = cost + cost_calculator(6,"0")
  starter(name, cost)
#################################################
def lucky_number(name, option, cost):
  size = len(name)
  asc_sum = 0
  for vowels in range(size - 1):
    if name[vowels] == 'a' or name[vowels] == 'e' or name[vowels] == 'i' or name[vowels] == 'o' or name[vowels] == 'u':
      asc_sum += ord(name[vowels])*vowels
  return ((asc_sum + cost) % size)
#################################################
def cost_calculator(option, num):
  if option == 0:
    return 0
  elif option == 1:
    return 0.25
  elif option == 2:
    return 1
  elif option == 3:
    if num == "50":
      return 0
    elif num == "100":
      return 1
    elif num == "200":
      return 2
    elif num == "400":
      return 4
    else:
      return 8
  else:
    return 1
################################################# 
def option_handler(option, name, cost):
  if option == 0:
    exit(name, cost)
    return 0
  elif option == 1:
    hexcolor_to_RGB_list(name, cost)
  elif option == 2:
    basic_poster(name, cost)
  elif option == 3:
    pixel_art_poster(name, cost, "original")
  elif option == 4:
    greyscale_pixel_art_poster(name, cost)
  elif option == 5:
    PixelArtPoster_with_shades_of_redbarseffect(name, cost)
  else:
    HorizontalBar_Scaledposter(name, cost)
#################################################
def starter(user_name, cost):
  print("Please choose an option") 
  print("0 - Exit")
  print("1 - Convert Hex color to RGB list")
  print("2 - Create a Basic Poster")
  print("3 - Create a Pixel Art Poster")
  print("4 - Create a Greyscale Pixel Art Poster")
  print("5 - Create a Pixel Art Poster with shades of red bars effect")
  print("6 - Create a Horizontal Bar Scaled poster")

  loop_stopper = True
  while loop_stopper:
    option = int(input("==> "))
    if option == 0 or option == 1 or option == 2 or option == 3 or option == 4 or option == 5 or option == 6:
      option_handler(option,user_name, cost)
      loop_stopper = False
    else:
      print("No, Choose a option from 0 to 6 ")
#################################################

print("Welcome to the pixel image creator tool!")
user_name = input("What is your name? ==> ") #AEIOU
user_name = user_name.lower()
print("Nice to meet you, " + user_name)
print("Please choose options to generate art. You may repeat options.")
print("The tool will save your art as jpg files in this folder.")
print("When you exit the tool you will be provided the cost,")
print("and also a lucky number!")

starter(user_name, 0)