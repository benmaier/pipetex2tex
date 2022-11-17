import re
from subprocess import Popen, PIPE

def _extract_command_from_within_brackets(text):

    prefixes = [' ','|','{',r'\input',r'\inp']
    while True:
        done = True
        for c in prefixes:
            if text.startswith(c):
                text = text[len(c):]
                done = False
        if done:
            break

    suffixes = [' ','}']
    while True:
        done = True
        for c in suffixes:
            if text.endswith(c):
                text = text[:-len(c)]
                done = False
        if done:
            break

    return text

def run_command(cmd):
    proc = Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
    out, err = proc.communicate()
    if proc.wait() != 0:
        output = "Command \"" + cmd+"\" raised errors:\n"+err.decode('utf-8')
        success = False
    else:
        output = out.decode('utf-8')
        success = True

    if output.endswith('\n'):
        output = output[:-1]
    return output, success

def convert(tex):
    """
    For explanation of regexp expression, check
    https://regexr.com/72k51
    """
    input_regexp = r"(\\inp|\\input)?\s*{\s*\|.*}"
    pattern = re.compile(input_regexp)
    pos = 0
    overall_success = True
    newtex = str(tex)

    found_matches = set()
    while True:
        m = pattern.search(tex, pos=pos)
        if m is None:
            break
        if m not in found_matches:
            span = m.span()
            this_match = m.group()
            command = _extract_command_from_within_brackets(this_match)
            output, success = run_command(command)
            overall_success = overall_success and success
            if not success:
                print("====================================")
                print("An error occured for input command "+this_match+" at position "+str(span[0])+".")
                print("Context:")
                print("   ..."+tex[max(0,span[0]-20):span[1]+20]+"...")
                print("this is the error message:")
                print(output)
                print("====================================\n")
            else:
                newtex = newtex.replace(this_match, output)

            found_matches.add(this_match)

            pos = span[1]

    if not overall_success:
        raise ValueError("There have been errors in the commands, see above.")

    return newtex



if __name__ == "__main__":

    tex = r"""
        This is a {\bf test}.

        I'll try converting this \input{|python -c "print('hi(input)')"}

        I'll try converting this \inp{|python -c "print('hi(inp)')"}
        I'll try converting this \inp  {  |    python -c "print('hi(inp)')"}
    """

    tex2 = r"""
        This is a {\bf test}.

        I'll try converting this \input{|python -c "print('hi(input)')"}

        I'll try converting this \inp{|python -c "print('hi(inp)')"}
        I'll try converting this \inp{|python "print('hi(inp)')"}
        I'll try converting this \inp  { |  python   "print('hi(inp)')"   }
    """



    result = convert(tex)
    print(result)
    convert(tex2)
    

