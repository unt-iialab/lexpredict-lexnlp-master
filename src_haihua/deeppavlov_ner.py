from deeppavlov import configs, build_model

ner_model = build_model(configs.ner.ner_ontonotes_bert, download=True)
ner_model(['Bob Ross lived in Florida'])
