import os
import pandas
import lexnlp.extract.en.amounts
import lexnlp.extract.en.acts
import lexnlp.extract.en.citations
import lexnlp.extract.en.courts
import lexnlp.extract.en.dict_entities
import lexnlp.extract.en.entities.nltk_re
import lexnlp.extract.en.conditions
import lexnlp.extract.en.constraints
import lexnlp.extract.en.copyright
import lexnlp.extract.en.cusip
import lexnlp.extract.en.dates
import lexnlp.extract.en.definitions
import lexnlp.extract.en.distances
import lexnlp.extract.en.durations
import lexnlp.extract.en.geoentities
import lexnlp.extract.en.money
import lexnlp.extract.en.percents
import lexnlp.extract.en.pii
import lexnlp.extract.en.ratios
import lexnlp.extract.en.regulations
import lexnlp.extract.en.trademarks
import lexnlp.extract.en.urls
import lexnlp.extract.en.entities.nltk_maxent
import lexnlp.extract.en.entities.stanford_ner
import lexnlp.extract.en.addresses.addresses
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')


# entity extraction
def entity_extractor(filepath):
    court_df = pandas.read_csv(
        "https://raw.githubusercontent.com/LexPredict/lexpredict-legal-dictionary/1.0.5/en/legal/us_courts.csv")
    court_config_data = []
    for _, row in court_df.iterrows():
        c = lexnlp.extract.en.dict_entities.entity_config(row["Court ID"], row["Court Name"], 0,
                                                          row["Alias"].split(";") if not pandas.isnull(
                                                              row["Alias"]) else [])
        court_config_data.append(c)
    for doc in os.listdir(filepath):
        print(doc)
        doc_path = os.path.join(filepath, doc)
        with open(doc_path, 'r') as f:
            lines = f.read().split('\n')
            for line in lines:
                # extract amount by using get_amount
                amounts = list(lexnlp.extract.en.amounts.get_amounts(line))
                # if len(amounts)>0:
                #   print(line)
                #   print (amounts)

                # extract acts by using get_act_list()
                acts = lexnlp.extract.en.acts.get_act_list(line)
                # if len(acts)>0:
                #   print(line)
                #   print(acts)

                # extract citations by using get_citations()
                # return: tuple or dict ---- (volume, reporter, reporter_full_name, page, page2, court, year[, source text])
                citations = list(lexnlp.extract.en.citations.get_citations(line))
                # if len(citations) > 0:
                #     print(citations)

                # extract courts by using get_courts()
                for entity, alias in lexnlp.extract.en.courts.get_courts(line, court_config_data):
                    print(line)
                    # print("entity=", entity)
                    # print("alias=", alias)

                # extract companies by using nltk_re.get_entities.nltk_re.get_companies()
                companies = list(lexnlp.extract.en.entities.nltk_re.get_companies(line))
                # if len(companies) > 0:
                #     print(companies)
                companies = list(lexnlp.extract.en.entities.nltk_re.get_parties_as(line))


                # extract conditions by using get_conditions()
                conditions = list(lexnlp.extract.en.conditions.get_conditions(line))

                # extract constraints by using get_constraints()
                constraints = list(lexnlp.extract.en.constraints.get_constraints(line))

                # extract copyright by using get_copyright()
                copyrights = list(lexnlp.extract.en.copyright.get_copyright(line))
                # if len(copyrights) > 0:
                #     print(copyrights)

                # extract cusip by using get_cusip()
                cusips = lexnlp.extract.en.cusip.get_cusip(line)

                # extract dates by using get_dates()
                dates = list(lexnlp.extract.en.dates.get_dates(line))

                # extract definitions by using get_definitions()
                definitions = list(lexnlp.extract.en.definitions.get_definitions(line))

                # extract distances by using get_distances()
                distances = list(lexnlp.extract.en.distances.get_distances(line))

                # extract durations by using get_durations()
                durations = list(lexnlp.extract.en.durations.get_durations(line))

                # extract geoentities by using get_geoentities()
                # geoentities = lexnlp.extract.en.geoentities.get_geoentities(line)

                # extract money by using get_money()
                moneys = list(lexnlp.extract.en.money.get_money(line))

                # extract percents by using .get_percents()
                percents = list(lexnlp.extract.en.percents.get_percents(line))

                # extract all the piis by using get_pii()
                piis = list(lexnlp.extract.en.pii.get_pii(line))

                # extract all the ratios by using get_ratios()
                ratios = list(lexnlp.extract.en.ratios.get_ratios(line))

                # extract all the regulations by using get_regulations()
                regulations = list(lexnlp.extract.en.regulations.get_regulations(line))

                # extract all the trademarks by using get_trademarks()
                trademarks = list(lexnlp.extract.en.trademarks.get_trademarks(line))

                # extract all the urls by using get_urls()
                urls = list(lexnlp.extract.en.urls.get_urls(line))

                # extract all the persons by using entities.nltk_maxent.get_persons()
                persons = list(lexnlp.extract.en.entities.nltk_maxent.get_persons(line))
                # if len(persons) > 0:
                #     print(line)
                #     print(persons)
                # persons = list(lexnlp.extract.en.entities.stanford_ner.get_persons(line))

                # extract all the geopolitical by using entities.nltk_maxent.get_geopolitical()
                geopolitical = list(lexnlp.extract.en.entities.nltk_maxent.get_geopolitical(line))

                # extract noun_phrases
                noun_phrases = list(lexnlp.extract.en.entities.nltk_maxent.get_noun_phrases(line))
                if len(noun_phrases) > 0:
                    print(line)
                    print(noun_phrases)

                # extract organizations
                # organizations = list(lexnlp.extract.en.entities.stanford_ner.get_organizations(line))

                # extract locations
                # locations = list(lexnlp.extract.en.entities.stanford_ner.get_locations(line))

                # extract address
                addresses = list(lexnlp.extract.en.addresses.addresses.get_addresses(line))

if __name__ == '__main__':
    filepath = '/home/iialab/Documents/Legal-kg/lexpredict-lexnlp-master/data_haihua/test_data'
    entity_extractor(filepath)