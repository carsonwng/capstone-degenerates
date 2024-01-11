from GROOV.data_processing.extract_data import load_labels, parse_data

labels_path = "./AmazonCat-13K.raw/Yf.txt"
input_path = "./AmazonCat-13K.raw/trn.json"
output_path = "./AmazonCat-13K_train.json"

labels = load_labels(labels_path)
parsed = parse_data(input_path, output_path, labels, wiki_data=False)

# print(parsed[0])