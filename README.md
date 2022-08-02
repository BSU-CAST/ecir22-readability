# ecir22-readability

This repository contains a notebook to reproduce the experiments conducted in our paper, *Supercalifragilisticexpialidocious: 
Why Using the "Right" Readability Formula in Children's Web Search Matters*. Also included is an implementation of the 
Spache-Allen readability formula.


## Using This Repository

In order to utilize the code contained in this repository, there are some requirements that must be fulfilled.

### Package Requirements

| Code Section | Package Requirements |
| --- | --- |
| Experiment Notebook | pandas, numpy, nltk, textstat, tqdm |
| Spache-Allen | nltk, openpyxl |

### Experiments

This notebook (`experiment_two_scenarios.ipynb`) utilizes prior published models which we exclude the code for due to
copyright reasons. For reproducibility needs, the citations of the necessary papers are provided below. The notebook 
makes a set of assumptions due to these factors. These assumptions are as follows:

 - **Scenario 1**
   - You will need to load a file that contains the queries for which you wish to assess the readability.
 - **Scenario 2**
   - We do not include the code for running ReQuik which is used for this scenario. Please reference the paper *“Looking 
   for the Movie Seven or Sven from the Movie Frozen?: A Multi-perspective Strategy for Recommending Queries for Children”* 
   for detail on the algorithm.
   - Our code assumes that you are loading in files of the results for each combination of formulas we describe in the 
   paper. The file should contain a column with the original query and the generated query suggestions.
 - **Scenario 3**
   - Similar to Scenario 1, you need to load a file that contains the snippets for which you wish to assess the 
   readability.
 - **Scenario 4**
   - Similar to Scenario 2, we do not include the code for running KORSCE. Please refer to the paper *“A Ranking Strategy 
   to Promote Resources Supporting the Classroom Environment"* for detail on the algorithm.
   - Our code assumes that you are loading one file with the re-ranked results from KORSCE for all data and readabilities 
   you wish to assess. The file must contain the query used to generate an entry, a column for each readabilities ranking 
   score, and a column with the original entries rank.

### Spache-Allen

The Spache-Allen readability formula extends the vocabulary of the original Spache formula. The terms used for this 
extension source from existing datasets, and are therefore not included in this repository for copyright reasons. In
order to use the formula we provide, you will need to complete the following steps, after cloning:

 1. Download and extract the [Age of Acquisition Dataset](http://crr.ugent.be/papers/AoA_ratings_Kuperman_et_al_BRM.zip)
 2. Download and extract the [ChildrenDict.tsv](https://scholarworks.boisestate.edu/context/cs_scripts/article/1004/type/native/viewcontent)
file of vocabulary terms from *“Looking for the Movie Seven or Sven from the Movie Frozen?: A Multi-perspective Strategy for 
Recommending Queries for Children”*
 3. Place both files in the `/spache_allen/vocabulary` directory
 4. Execute the `build_vocabulary.py` script, which can be found in `/spache_allen`
 5. Use the Spache-Allen formula in your project

## Citations

Please cite the following works if you use this repository for your research.

```
@inproceedings{allen2022supercalifragilisticexpialidocious,
  title={Supercalifragilisticexpialidocious: Why Using the “Right” Readability Formula in Children’s Web Search Matters},
  author={Allen, Garrett and Milton, Ashlee and Wright, Katherine Landau and Fails, Jerry Alan and Kennington, Casey and Pera, Maria Soledad},
  booktitle={European Conference on Information Retrieval},
  pages={3--18},
  year={2022},
  organization={Springer}
}

@inproceedings{madrazo2018looking,
  title={Looking for the Movie Seven or Sven from the Movie Frozen? A Multi-perspective Strategy for Recommending Queries for Children},
  author={Madrazo Azpiazu, Ion and Dragovic, Nevena and Anuyah, Oghenemaro and Pera, Maria Soledad},
  booktitle={Proceedings of the 2018 Conference on Human Information Interaction \& Retrieval},
  pages={92--101},
  year={2018}
}

@article{kuperman2012age,
  title={Age-of-acquisition ratings for 30,000 English words},
  author={Kuperman, Victor and Stadthagen-Gonzalez, Hans and Brysbaert, Marc},
  journal={Behavior research methods},
  volume={44},
  number={4},
  pages={978--990},
  year={2012},
  publisher={Springer}
}

@inproceedings{milton2020ranking,
  title={A Ranking Strategy to Promote Resources Supporting the Classroom Environment},
  author={Milton, Ashlee and Anuya, Oghenemaro and Spear, Lawrence and Wright, Katherine Landau and Pera, Maria Soledad},
  booktitle={2020 IEEE/WIC/ACM International Joint Conference on Web Intelligence and Intelligent Agent Technology (WI-IAT)},
  pages={121--128},
  year={2020},
  organization={IEEE}
}
```
