from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("cca3").getOrCreate()

# Obj 1.1
file_path = "hdfs://namenode:9000/ungeneral-debates.csv"

df = spark.read.csv(file_path, header=True, multiLine=True)
text_column = df.select(
    "text"
)  # extract every record of df with attribute "text", into "row" objects


def extract_text(row):
    return row[
        "text"
    ]  # Given an object "row", return the attribute value "text" of the row.


text_rdd = text_column.rdd.map(
    extract_text
)  # text_column.rdd will iterate every row object in text_column, with the function
# extract_text, it will extract "text" attribute value in every given object row,
# and map it to rdd
# 擷取出ungeneral-debates中的每一行records的text(text_rdd)

# Obj 1.2
all_verbs_rdd = spark.sparkContext.textFile("hdfs://namenode:9000/all_verbs.txt")


def is_not_empty(line):
    return line.strip() != ""


all_verbs_without_space_rdd = all_verbs_rdd.filter(
    is_not_empty
)  # deal space if all_verbs.txt has space elements

verb_dict_rdd = spark.sparkContext.textFile("hdfs://namenode:9000/verb_dict.txt")


# Obj 2.1
def is_not_empty(line):
    return line and line.strip() != ""


text_rdd_without_empty_lines = text_rdd.filter(is_not_empty)
# 為刪除ungeneral-debates rdd中的空行(text_rdd_without_empty_lines)

# Obj 2.2
import re


def remove_punctuation(line):
    return re.sub(r"[^\w\s]", "", line)


text_after_clean = text_rdd_without_empty_lines.map(remove_punctuation)
# 刪除text_rdd_without_empty_lines中的標點符號(text_after_clean)


# Obj 2.3
def to_lowercase(line):
    return line.lower()


lowercase_text_rdd = text_after_clean.map(to_lowercase)
# 將text_after_clean轉成小寫(lowercase_text_rdd)

# Obj 2.4
verb_list = set(all_verbs_without_space_rdd.collect())
sorted_verb_list = sorted(verb_list)
# 擷取all_verbs內的所有動詞並字母排序(sorted_verb_list)


def extract_verbs(line):
    every_setence = line.split()
    verbs_in_every_sentence = [
        every_word for every_word in every_setence if every_word in sorted_verb_list
    ]
    return verbs_in_every_sentence


existing_verbs_rdd = lowercase_text_rdd.map(extract_verbs)
# 擷取text中所有存在於all_verbs的動詞(existing_verbs_rdd)

# Obj 2.5
simple_present_tense_verbs_mapping = {}  # dictionary to store verbs mappings


def create_verb_mapping(line):
    every_verbs = line.split(",")
    base_verb = every_verbs[0]
    variations = every_verbs[1:]
    local_mapping = {}
    for v in variations:
        local_mapping[v] = base_verb
    return local_mapping


mappings_list = verb_dict_rdd.map(create_verb_mapping).collect()

# put every local mapping into a big global mapping dictionary
for mapping in mappings_list:
    simple_present_tense_verbs_mapping.update(mapping)


# Obj 3.1
def map_to_base_form(verb):
    return simple_present_tense_verbs_mapping.get(
        verb, verb
    )  # Function to map every verb to their simple present tense


base_form_verbs_rdd = existing_verbs_rdd.flatMap(
    lambda verbs: [map_to_base_form(verb) for verb in verbs]
)
# deploy function on every verb that used in text

verb_count_rdd = base_form_verbs_rdd.map(lambda verb: (verb, 1)).reduceByKey(
    lambda a, b: a + b
)
# Count frequency

top_10_verbs = verb_count_rdd.takeOrdered(10, key=lambda x: -x[1])
# Get 10 most frequent verbs

# Obj 3.2
for verb, count in top_10_verbs:
    print(f"{verb}, {count}")
