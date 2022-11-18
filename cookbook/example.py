from pipetex2tex.convert import convert

tex = "There's \inp{|python -c 'print(int(24*60*60*365.25))'} seconds in a year."
print(tex)
print(convert(tex))

tex = "There's $\input { | ls -al ~ | wc -l }$ files/directories in your user directory."
print("\n"+tex)
print(convert(tex))
