from openie import StanfordOpenIE

with StanfordOpenIE() as client:
    # text = 'Barack Obama was born in Hawaii. Richard Manning wrote this sentence.'
    # text = 'A growing crop has such an existence as to be the subject-matter of a mortgage or other contract which passes an interest to vest in possession, either immediately or at a future time.'
    text = 'Texas has a city named Dallas'
    print('Text: %s.' % text)
    for triple in client.annotate(text):
        print('|-', triple)

    graph_image = '/home/iialab/Documents/Legal-kg/lexpredict-lexnlp-master/results_haihua/graph.png'
    client.generate_graphviz_graph(text, graph_image)
    print('Graph generated: %s.' % graph_image)

    # with open('/home/iialab/Documents/Legal-kg/lexpredict-lexnlp-master/data_haihua/test_data/01-05-1  Adams v Tanner.txt', 'r', encoding='utf8') as r:
    #     corpus = r.read().replace('\n', ' ').replace('\r', '')
    #
    # triples_corpus = client.annotate(corpus[0:50000])
    # print('Corpus: %s [...].' % corpus[0:80])
    # print('Found %s triples in the corpus.' % len(triples_corpus))
    # for triple in triples_corpus[:3]:
    #     print('|-', triple)