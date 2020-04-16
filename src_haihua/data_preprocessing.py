import lexnlp.nlp.en.segments.sentences
import nltk
import os

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
import re

# Split the documents into sentences
def sentenceSegment(original_path, save_path):
    for doc in os.listdir(original_path):
        print(doc)
        doc_path = os.path.join(original_path, doc)
        with open(doc_path, 'r') as file:
            content = file.read()
            # print(content)
            sent = lexnlp.nlp.en.segments.sentences.get_sentence_list(content)
            # print(sent)
            with open(save_path + '/' + doc, 'w') as outfile:
                for listitem in sent:
                    outfile.write('%s\n' % listitem)

# remove some noise by defining a set of patterns
def clean_sentence(pre_process_path,clean_filepath):
    for doc in os.listdir(pre_process_path):
        print(doc)
        doc_path = os.path.join(pre_process_path, doc)
        with open(doc_path, 'r') as f:
            lines = f.read().split('\n')
            for i, line in enumerate(lines):
                # print(i,line)
                if line.startswith('v.'):
                    lines[i - 1] = lines[i - 1] + lines[i]
                    lines.pop(i)
                    for j, l in enumerate(lines):
                        # print(j,l)
                        if l.endswith('v.'):
                            lines[j] = lines[j] + lines[j + 1]
                            lines.pop(j + 1)
                        else:
                            pass

                elif line.endswith('v.'):
                    lines[i] = lines[i] + lines[i + 1]
                    lines.pop(i + 1)

                if line[:3].isdigit():
                    lines[i - 1] = lines[i - 1] + lines[i]
                    # print(line)
                    lines.pop(i)

                    for j, l in enumerate(lines):
                        if l[:3].isdigit():
                            # print(l)
                            lines[j - 1] = lines[j - 1] + lines[j]
                            lines.pop(j)
                        else:
                            pass

                if line.endswith(':'):
                    # print(line)
                    lines[i] = lines[i] + lines[i + 1]
                    lines.pop(i + 1)

        with open(clean_filepath + '/' + doc, 'w') as outf:
            for items in lines:
                outf.write('%s\n' % items)


if __name__ == '__main__':
    original_path = '/home/iialab/Documents/Legal-kg/lexpredict-lexnlp-master/data_haihua/sample_case'
    save_path = '/home/iialab/Documents/Legal-kg/lexpredict-lexnlp-master/data_haihua/pre_process_data'
    clean_path = '/home/iialab/Documents/Legal-kg/lexpredict-lexnlp-master/data_haihua/clean_sentence'
    sentenceSegment(original_path, save_path)
    clean_sentence(save_path, clean_path)