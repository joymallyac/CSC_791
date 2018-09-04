import re, traceback


class O:
    y = n = 0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%" % (
            O.y, O.n, int(round(O.y * 100 / (O.y + O.n + 0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            print("\t")
            if f.__doc__:
                print("# " + re.sub(r'\n[ \t]*', "\n# ", f.__doc__))
            f()
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f



DATA1 ="""
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 ="""
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""


## --------- Implementation ---------------

def lines(src):

    """Return contents, one line at a time."""
    
    try:        
        src = src.replace(" ","").split('\n')
        i = 0
        while i < len(src):
            if(len(src[i]) == 0):
                src.pop(i)
            else:
                if ('#' in src[i]):
                    src[i] = src[i].split('#')[0]
                i = i + 1
    except:
        print(" Exception occurred in lines() function ")

    return src


def rows(src):

    """If line ends in ',' then join to next. Skip blank lines."""

    try:
        i = 0
        while i < len(src):
            if (src[i].endswith(',')):
                src[i] = src[i] + src[i+1]
                src.pop(i+1)
            else:
                i = i + 1
    except:
         print(" Exception occurred in rows() function ")
    return src


def cols(src):
    """If a column name on row1 contains '?',then skip over that column."""

    index = -1
    modified_list = []  

    try:
        i = 0        
        while i < len(src[0].split(',')):            
            if(src[0].split(',')[i].startswith('?')):
                index = i                
            i = i + 1

        for i, r in enumerate(src):
            new_row = r.split(',')
            if ( index >= 0):
                del new_row[index]
            modified_list.append(new_row)
    except:
        print(" Exception occurred in cols() function ")

    return modified_list


def prep(src):

    """If a column name on row1 contains '$', coerce strings in that column to a float."""

    index = -1

    try:
        i = 0        
        while i < len(src[0]):            
            if(src[0][i].startswith('$')):
                index = i                
            i = i + 1       
        
        for i in src[1:]:
            if ( index >= 0):
                i[index] = float(i[index])
    except:
        print(" Exception occurred in prep() function ")

    return src


# ----- Test Case ----------------------------

def ok0(s):
    
    for row in prep(cols(rows(lines(s)))):        
        print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)