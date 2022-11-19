import sys
from textwrap import wrap

STR_DEFINITION       = "DEFINITION"
END_POS_DEFINITION   = len(STR_DEFINITION)
POS_START_DEFINITION = END_POS_DEFINITION+2

STR_VERSION       = "VERSION"
END_POS_VERSION   = len(STR_VERSION)
POS_START_VERSION = END_POS_VERSION+2


STR_ORIGIN       = "ORIGIN"
END_POS_ORIGIN   = len(STR_ORIGIN)
POS_START_ORIGIN = END_POS_ORIGIN+2

def extract_aminoacids(line):
    first_space=line.find(" ")
    return line[first_space:].strip().replace(" ", "")

def convert_amino_lines(lines):
    aminoacid_lines=[extract_aminoacids(l) for l in lines]
    joined="".join(aminoacid_lines)
    joined=joined.upper()
    #We must now break the long aminoacid line in lines with
    #a width of 70 characters
    lines_70_col_width= wrap(joined, width=70)
    return "\n".join(lines_70_col_width)

def print_record(definition, gi, emb, lines):
    #print(definition,gi, emb)
    id="{0}{1}{2}".format(definition[0].upper(), definition[2].upper(), emb[:-2])
    line=">gi|{0}|emb|{1}|{2} {3}".format(gi[3:], emb, id, definition)
    print(line)
    print ( convert_amino_lines (lines))


def convert_from_genbank_to_fasta():
    definition = None
    version    = None
    lines      = None
    for line in sys.stdin:
        # Find definition
        if line[0:END_POS_DEFINITION] == STR_DEFINITION:
            definition=line[POS_START_DEFINITION:].strip()

        # Then find version
        if line[0:END_POS_VERSION] == STR_VERSION:
            version     = line[POS_START_VERSION:].strip()
            first_space = version.find(" ")
            emb         = version[0:first_space].strip()
            gi          = version[first_space+1:].strip()
            # print(">{0}<".format(emb))
            # print(">{0}<".format(gi))

        # And last, find origin
        if line[0:END_POS_ORIGIN] == STR_ORIGIN:
            # print("Found origin")
            lines=[]
            for line in sys.stdin:
                line=line.strip()
                if line=="//":
                    break
                lines.append(line)
        if definition!=None and version!=None and lines!=None:
            print_record(definition, gi, emb, lines)
            #2 blank lines between records
            print()
            print()
            print()
            
            definition = None
            version    = None
            lines      = None
            

if __name__=="__main__":
    convert_from_genbank_to_fasta()