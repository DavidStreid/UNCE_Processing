# UNCE's Ultraconserved Element Processing
Downloads [UNCE](https://ccg.epfl.ch/UCNEbase/)'s ultraconserved elements and saves to JSON

## Upload
* If already downloaded, run
```
$ python3 mongo_upload.py
0: SALL3_Abdullah
1: CASZ1_Benjamin
2: CASZ1_Cameron
3: CASZ1_Eden
...
```

## Download
```
./download.sh
python parse_fasta
``` 

### Output
FASTA & JSON
```
{
   "entries":[
      {
         "end":77010679,
         "seq":"TGCAGGGGAAAGTGTGAGGTGGTGGTTATGCATTTTGCAAGACAGTGATTCTTTATTTTATTACAAAAAAAGACCAACTCTGGAAGGCCAGATTAAATCATTCCTTTCACTTTTTAATGGGATTTGGATGAATAGAGTAAAATATGCACTTTGCATTCATTGATAGCATCTTTAGGTTGAGGTAATTGAGTCTTTTTTCCCTGAGTGAATGAATAATGACTTCATCTGATCCTCAGTGAGGCCTGAAACTTAGACCGCCTTTGTCACAGCAAAAGGATCTGGGCTTTGAAACATGCTCTACTTCCCTGGCTTAATTTTTCTTCATTTTAATCCAAAAACCTATTTTTCTCAATAATTCAAGCATAAACTATGTAGTAGTTGAAGTAGCGGAAATTGCACGATATTTGTCCTGGTTGTGCTGCTTT",
         "unce_name":"SALL3_Abdullah",
         "start":77010255,
         "chr":"chr18",
         "unce_id":17975,
         "species":[
            "zebra_finch",
            "xenopus",
            "fugu",
            "platypus",
            "lizard",
            "painted_turtle",
            "opossum",
            "armadillo",
            "zebrafish",
            "mouse",
            "stickleback"
         ]
      },
      ...
   ]
}
```
