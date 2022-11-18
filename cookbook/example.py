import pipetex2tex as p2t

tex = "There's \inp{|python -c 'print(int(24*60*60*365.25))'} seconds in a year."
print("source:", tex)
print("out   :", p2t.convert(tex), '\n')

tex = "There's $\input { | ls -al ~ | wc -l }$ files/directories in your user directory."
print("source:", tex)
print("out   :", p2t.convert(tex))
