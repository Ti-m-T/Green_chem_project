from chempy.chemistry import balance_stoichiometry
from rdkit.Chem import Descriptors
from rdkit import Chem
from rdkit.Chem.rdMolDescriptors import CalcMolFormula

dictionary_input_smiles: dict[str, list[str]] = {
    "reactants": ["[H][H]", "O=O"],
    "products": ["O"],
}


def split_input(
    dictionary_input_smiles: dict[str, list[str]],
) -> tuple[list[str], list[str]]:
    reactants: list[str] = dictionary_input_smiles.get("reactants", [])
    products: list[str] = dictionary_input_smiles.get("products", [])
    return (reactants, products)


# Split en deux classes le dictionnaire d'input


def smiles_to_brute(
    dictionary_input_smiles: dict[str, list[str]],
) -> dict[str, list[str]]:

    dictionary_input_brute: dict[str, list[str]] = {}

    for key, liste_smiles in dictionary_input_smiles.items():
        dictionary_input_brute[key] = []

        for smiles in liste_smiles:
            molecule = Chem.MolFromSmiles(smiles)
            formule_brute = CalcMolFormula(molecule)
            dictionary_input_brute[key].append(formule_brute)

    return dictionary_input_brute


# print(smiles_to_brute(dictionary_input_smiles))
# Fonction qui passe de smiles a formule brute et retourne un dictionnarie de listes de formules brutes


def calcul_coef_stoechio(
    dictionary_input_smiles: dict[str, list[str]],
) -> dict[dict[str, int]]:
    dict_coef_stoechio: dict[dict[str, int]] = {"reactants": {}, "products": {}}
    dict_input_brute = smiles_to_brute(dictionary_input_smiles)
    reactant, product = split_input(dict_input_brute)
    coef_stoi_reac, coef_stoi_prod = balance_stoichiometry(reactant, product)

    # Calcul des coefficients stoechiométriques à partir des formules brutes des réactifs et des produits

    liste_smiles_tot: list[str] = []
    for key in dictionary_input_smiles["reactants"]:
        liste_smiles_tot.append(key)

    liste_smiles_prod: list[str] = []
    for key in dictionary_input_smiles["products"]:
        liste_smiles_tot.append(key)

    # Creation des liste des smiles des réactifs et des produits

    liste_brute_tot: list[str] = []
    for key in coef_stoi_reac.keys():
        liste_brute_tot.append(key)

    for key in coef_stoi_prod.keys():
        liste_brute_tot.append(key)

        # Creation des listes de formules brutes associées

        for key, coef_stoi in coef_stoi_reac.items():
            Loc = liste_brute_tot.index(key)
            smiles_associé_au_brute = liste_smiles_tot[Loc]
            dict_coef_stoechio["reactants"][smiles_associé_au_brute] = coef_stoi

        for key, coef_stoi in coef_stoi_prod.items():
            Loc = liste_brute_tot.index(key)
            smiles_associé_au_brute = liste_smiles_tot[Loc]
            dict_coef_stoechio["products"][smiles_associé_au_brute] = coef_stoi

    # On relie la formule brute au smile par emplacement dans la liste

    return dict_coef_stoechio


# print(calcul_coef_stoechio(dictionary_input_smiles))
# Fonction qui calcule les coefficients stoechiométriques d'une réaction chimique donnée sous forme de dictionnaire de listes de réactifs et de produits, retourant les coefficients stochiométriques sous forme de dictionaires.


def coef_stoechio_reactants(dictionary_input_smiles: dict[str, list[str]]) -> list[int]:
    list_coef_reactants: list[int] = []
    for key in calcul_coef_stoechio(dictionary_input_smiles)[0]:
        list_coef_reactants.append(
            calcul_coef_stoechio(dictionary_input_smiles)[0][key]
        )
    return list_coef_reactants


# Fonction qui calcule les coefficients stoechiométriques des réactifs d'une réaction chimique donnée sous forme de dictionnaire de listes de réactifs et de produits, retourant les coefficients stochiométriques des réactifs sous forme de liste d'entiers.

print(dictionary_input_smiles(*balance_stoichiometry(["H2", "O2"], ["H2O"])).string())
# Fonction qui calcule les coefficients stoechiométriques d'une réaction chimique donnée sous forme de listes de réactifs et de produits, retournant l'equation chimique équilibrée sous forme de string.


def calculate_molecular_weight(
    dictionary_input_smiles: dict[str, list[str]],
) -> dict[str, dict[str, float]]:
    mol_weights_dict: dict[str, dict[str, float]] = {"reactants": {}, "products": {}}
    for key in ["reactants", "products"]:
        for individual_smiles in dictionary_input_smiles.get(key, []):
            molecule = Chem.MolFromSmiles(individual_smiles)
            mol_weight = Descriptors.MolWt(molecule)
            mol_weights_dict[key][individual_smiles] = mol_weight
    return mol_weights_dict


# print(calculate_molecular_weight(dictionary_input_smiles))
# Fonction qui calcule le poids moléculaire de chaque réactif et produit d'une réaction chimique apartir d'un dictionnaire contenant les listes de SMILES des réactifs et des produits, retournant un dictionnaire contenant les poids moléculaires correspondants.


def calcul_eco_atom_reactants(dictionary_input_smiles: dict[str, list[str]]) -> float:
    dict_coef_stoic = calcul_coef_stoechio(dictionary_input_smiles)
    dict_coef_stoic_reactants = dict_coef_stoic.get("reactants", [])
    print(dict_coef_stoic_reactants)
    mol_weight_dict = calculate_molecular_weight(dictionary_input_smiles)
    mol_weight_reactants = mol_weight_dict.get("reactants", {})
    print(mol_weight_reactants)
    eco_atom_reactants: float = 0.0
    # for key_reac, coef in dict_coef_stoic_reactants.items():
    # co_atom_reactants += coef * mol_weight_reactants.get(key_reac, ())
    return eco_atom_reactants


# print(calcul_eco_atom_reactants(dictionary_input_smiles))
# print (calcul_eco_atom_reactants(dictionary_input_smiles))
# need of the smiles / brute conversion

# def calculate_eco_atm(smiles_of_reaction: dict[str,list[str]]) -> tuple[dict[str, float], dict[str, float]]:
#    reac,prod = calcul_coef_stoechio(smiles_of_reaction.get("reactants", []), smiles_of_reaction.get("products", []))
#    mol_weights_dict = calculate_molecular_weight(smiles_of_reaction)
# for i in range(len(smiles_of_reaction.get("reactants",[]))):


# test:list[str]= ["ea", "eb", "ec", "ed", "ee"]
# print(test.index("ec"))
