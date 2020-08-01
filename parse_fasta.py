import sys
import re
import json
import requests

unce_file = './unce_file.json'

if(len(sys.argv) == 1):
    exit("Specify path")

file_name = sys.argv[1]

urls = [
    ["mouse", "https://ccg.epfl.ch/UCNEbase/data/download/ucnes/mm10_UCNE_orthologs.txt"],
    ["armadillo", "https://ccg.epfl.ch/UCNEbase/data/download/ucnes/dasNov1_UCNE_orthologs.txt"],
    ["opossum","https://ccg.epfl.ch/UCNEbase/data/download/ucnes/monDom5_UCNE_orthologs.txt",],
    ["platypus","https://ccg.epfl.ch/UCNEbase/data/download/ucnes/ornAna1_UCNE_orthologs.txt",],
    ["xenopus","https://ccg.epfl.ch/UCNEbase/data/download/ucnes/xenTro3_UCNE_orthologs.txt",],
    ["painted_turtle","https://ccg.epfl.ch/UCNEbase/data/download/ucnes/chrPic1_UCNE_orthologs.txt",],
    ["lizard","https://ccg.epfl.ch/UCNEbase/data/download/ucnes/anoCar2_UCNE_orthologs.txt",],
    ["zebra_finch","https://ccg.epfl.ch/UCNEbase/data/download/ucnes/taeGut1_UCNE_orthologs.txt",],
    ["fugu","https://ccg.epfl.ch/UCNEbase/data/download/ucnes/fr2_UCNE_orthologs.txt",],
    ["stickleback","https://ccg.epfl.ch/UCNEbase/data/download/ucnes/gasAcu1_UCNE_orthologs.txt",],
    ["tetraodon","https://ccg.epfl.ch/UCNEbase/data/download/ucnes/tetNig2_UCNE_orthologs.txt",],
    ["zebrafish","https://ccg.epfl.ch/UCNEbase/data/download/ucnes/taeGut1_UCNE_orthologs.txt"]
]

# Tracks id's -> species
unce_id_map = {}

for url in urls:
    species = url[0]
    print("Querying: " + url[1])
    r = requests.get(url[1])
    content = r.content
    lines = content.split("\n")

    header = re.split('[,\s]', lines[0])
    header = list(filter(lambda a: a != '', header))
    id_idx = header.index("UCNE_ID")

    if(id_idx < 0):
        sys.exit("Couldn't find index for columns")

    for line in lines[1:]:
        values = re.split('[,\s]', line)
        values = list(filter(lambda a: a != '', values))
        if(len(values) > 1):
            unce_id = int(values[id_idx], 10)
            if unce_id in unce_id_map:
                unce_id_map[unce_id].add(species)
            else:
                unce_id_map[unce_id] = {species}

def is_header(line):
    return line[0] == ">"

def parse_header(header_line):
    """
    >SALL3_Abdullah id=17975 pos=chr18:77010255-77010679
        unce_name: SALL3_Abdullah
        unce_id: 17975
        chr: chr18
        start: 77010255
        end: 77010679
    """
    header_line = header_line.strip(">")
    parts = header_line.split()
    if(len(parts) == 3):
        unce_name = parts[0]
        unce_id = int(parts[1].split("=")[1], 10)
        pos_part = parts[2].split("=")[1]
        chr_pos = pos_part.split(":")
        chr = chr_pos[0]
        start_end = chr_pos[1].split("-")
        start = int(start_end[0], 10)
        end = int(start_end[1], 10)
        return {
            "unce_name": unce_name,
            "unce_id": unce_id,
            "chr": chr,
            "start": start,
            "end": end,
            "seq": "",
            "species": [] if unce_id not in unce_id_map else list(unce_id_map[unce_id])
        }
    print("invalid line: " + header_line)
    return {}

f = open(file_name, "r")
line = f.readline()
entries = []

entry = "Finished Parsing"
while(line):
    if(is_header(line)):
        # >SALL3_Abdullah id=17975 pos=chr18:77010255-77010679
        entries.append(entry)
        entry = parse_header(line)
    elif(re.match("[AGCT]", line)):
        # TGCAGGGGAAAGTGTGAGGTGGTGGTTATGCATTTTGCAAGACAGTGATT
        entry["seq"] += line.strip()
    line = f.readline()

print(entries.pop(0))

contents = {
    'entries': entries
}

f = open(unce_file, "w")
json.dump(contents, f)
f.close()

