# <a name=top></a>Scripts for frequently done lab tasks:

* [GUI] (#abstracts_gui) [scripts] (#abstracts_scripts) [**Searching for and downloading NCBI PubMed abstracts**] (#abstracts)
* [GUI] (#gene_lists_gui) [scripts] (#gene_lists_scripts) [**Searching for and downloading NCBI Gene Lists**] (#gene_lists)
 


## Task: <a name=abstracts></a>[**Searching for and downloading NCBI PubMed abstracts**] (#top):

**1**. <a name=abstracts_gui></a>Original: Get PMIDs through the **GUI** at http://www.ncbi.nlm.nih.gov/pubmed:

  ![NCBI Pubmed](https://github.com/dklopfenstein/biocode/blob/master/doc/PyDkBio/asthma_pubmed_GUI.png)

**2**. <a name=abstracts_scripts></a>Faster: Get PMIDs through **scripts** accessing NCBI eutils using biopython:

This:
```
get_abstracts(
  'asthma_pubmed_ids.md',    # Markdown text File written and filled with PubMed Abstracts
  email  = 'myemail@gmail.com',
  query  = 'asthma[mesh] AND leukotrienes[mesh] AND "last 6 months" [DP]')
```

Writes the abstracts into the markdown text file, [asthma_pubmed_ids.md] (https://github.com/dklopfenstein/biocode/blob/master/doc/PyDkBio/asthma_pubmed_ids.md)

## Task: <a name=gene_lists></a>[**Searching for and downloading NCBI Gene Lists**] (#top):
1. <a name=gene_lists_gui></a>Original: Get PMIDs through the **GUI** at http://www.ncbi.nlm.nih.gov/pubmed:
2. <a name=gene_lists_scripts></a>Faster: Get PMIDs through **scripts** accessing NCBI eutils using biopython: