n=int("4")
for i in ["00000000", 
          "00000000",
          "00111100", 
          "01100110",
          "11000010", 
          "11000000", 
          "11000000", 
          "11011110",
          "11000110", 
          "11000110",
          "01100110", 
          "00111010",
          "00000000", 
          "00000000",
          "00000000", 
          "00000000"]:
    print(((""+""+''.join(j*n for j in i)+""+',\n')*n)[:-1])