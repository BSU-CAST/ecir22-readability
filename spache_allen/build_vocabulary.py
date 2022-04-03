import openpyxl
from pathlib import Path


def extract_spache_easy_terms(spache_easy_path):
    with open(str(Path(spache_easy_path)), "r") as infile:
        lines = infile.readlines()
        stripped = [line.strip() for line in lines]

    print(f"{len(stripped)} extracted.")
    return stripped


def extract_aoa_terms(aoa_path):
    wb_obj = openpyxl.load_workbook(aoa_path)
    active_sheet = wb_obj.active
    words = [val[0].value for val in active_sheet.iter_rows(max_col=1)]

    print(f"{len(words)} extracted.")
    return words


def extract_sven_child_dict_terms(sven_child_dict_path):
    with open(str(sven_child_dict_path), "r") as infile:
        lines = infile.readlines()
        split_lines = [line.split("\t") for line in lines]
        terms = [sl[1] for sl in split_lines]

    print(f"{len(terms)} extracted.")
    return terms


if __name__ == "__main__":
    vocab_dir = Path(__file__).resolve().parent.joinpath("vocabulary")
    spache_easy = Path(vocab_dir).joinpath("spache_easy.txt")
    aoa = Path(vocab_dir).joinpath("AoA_ratings_Kuperman_et_al_BRM.xlsx")
    sven_child_dict = Path(vocab_dir).joinpath("ChildrenDict.tsv")
    sven_terms = extract_sven_child_dict_terms(sven_child_dict)
    aoa_terms = extract_aoa_terms(aoa)
    spache_easy_terms = extract_spache_easy_terms(spache_easy)

    spache_aoa_full = set(spache_easy_terms).union(set(aoa_terms))
    spache_allen_terms = spache_aoa_full.union(set(sven_terms))
    spache_allen_terms = list(filter(None, spache_allen_terms))
    spache_allen_terms = sorted(spache_allen_terms)

    with open(str(Path(vocab_dir).joinpath("spache_allen.txt")), "w") as outfile:
        for word in spache_allen_terms:
            outfile.write("{}\n".format(word))

    print(f"{len(spache_allen_terms)} written to /spache_allen/vocabulary/spache_allen.txt")
