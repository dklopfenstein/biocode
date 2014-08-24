#!/usr/bin/env python
"""This script downloads PubMed abstracts from NCBI's PubMed based on a user query.

   Requires the biopython package.
"""

import sys
import os
import datetime

from Bio import Entrez
from Bio import Medline

import PyDkBio.NCBI.ESearch_Action_Helpers as FT
import PyBiocode.NCBI.EUtils_Apps as EA


# -------------------------------------------------------
def run_example():
  email = "music_pupil@yahoo.com"
  query = "disease gene identification strategies for exome sequencing"
  query = "asthma[mesh] AND leukotrienes[mesh] AND 2009[pdat]"
  query = 'autism[TI] AND "last 14 days" [DP]'
  retmax = "100"
  EA.get_abstracts('medline.md', email, query, retmax)

def example2():
  EA.get_abstracts(
    'asthma_pubmed_ids.md',    # Markdown text File written and filled with PubMed Abstracts
    email  = 'myemail@gmail.com',
    query  = 'asthma[mesh] AND leukotrienes[mesh] AND "last 6 months" [DP]')
  

# -------------------------------------------------------
if __name__ == '__main__':
  #run_example()
  example2()