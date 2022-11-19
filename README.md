# genbank2fasta
A sample script to convert from Genbank files to FASTA format.

Just print a Genbank file and pipe the result to the script to obtain a FASTA file in the standard output.

For example::

    cat ls_orchid.gbk | python3 genbank2fasta.py

If you want to keep the result in a file redirect the result by using something like this::

    cat ls_orchid.gbk | python3 genbank2fasta.py > ls_orchid.fasta