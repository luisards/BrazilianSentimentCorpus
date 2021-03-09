import spacy
from spacy import displacy
import json
import sys
import pandas
from csv import DictReader
from os import listdir

#if len(sys.argv) < 2:
#    sys.exit('Too few arguments, please speciify the input file')

#mypath = sys.argv[1]

nlp = spacy.load("pt_core_news_sm")

mypath = 'C:/Users/luisa/Desktop/LCA/MiniProject/data' 
#files = listdir(mypath)
#for f in files:
#    directory = mypath + '/' + f
#    with open(directory, encoding="utf-8") as tweet:
#        data = tweet.read()

with open('C:/Users/luisa/Desktop/LCA/MiniProject/BrazilianTweetsOut.csv', 'r', encoding='utf8') as read_obj:
    csv_dict_reader = DictReader(read_obj, delimiter='|')
    for row in csv_dict_reader:
        #Create title
        filename = row['Jornal']+'_'+row['Assunto']+'_'+str(row['Data'])+'_'+str(row['Tweet_ID'])
        #Check for polarity value
        if row['Polaridade']=='Negativa':
            polarity = 'Negativa'
        elif row['Polaridade']=='Positiva':
            polarity = 'Positiva'
        else:
            polarity='Neutra'
        #Check for language value
        if row['Linguagem']=='Ofensiva':
            offense='Ofensiva'
        else:
            offense='Não-ofensiva'
        #select tweet text    
        content = row['Tweet']
        #Create WebAnno TSV file
        with open(mypath+"/newdata/"+filename, 'w', encoding='utf8') as outfile:
            outfile.write("#FORMAT=WebAnno TSV 3.2\n#T_SP=de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS|coarseValue")
            outfile.write("\n#T_RL=de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency|DependencyType|BT_de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS")
            outfile.write("\n#T_SP=webanno.custom.Sentiment|Polarity")
            outfile.write("\n#T_SP=webanno.custom.Linguagem|Ofensa\n\n")
            
            doc = nlp(content)
            parent = list()
            sentence_list = list(doc.sents)
            doc_list = list(doc)
            word_count = 0
            doc_count = 0
            char_count = 0
            char_count_old = 0
            sent_count = 1
            
            for sent in doc.sents:
                word_list = list(sent)
                word_count = 0
                outfile.write("\n#Text=" + str(sent) + '\n')

                for token in sent:
                    if token.dep_ == "ROOT":            
                        parent = "_"
                        parent_index = word_count + 1
                    else:    
                        parent = token.head
                        parent_index = word_list.index(parent)+1
                    if  char_count != 0:
                        char_count = char_count + len(token.text) +1        
                    else:
                        char_count = char_count + len(token.text)
                    if token.dep_ == "punct":
                        char_count = char_count-1
                        char_count_old = char_count_old -1    
                    word_count += 1
                    doc_count +=1
                    line = str(sent_count)+"-" + str(word_count) + "\t"+ str(char_count_old)+ "-"+ str(char_count)+"\t" + token.text+ "\t" +token.pos_+"\t" + token.dep_ + "\t" + str(sent_count)+ '-' + str(parent_index) +'\t'+ polarity +'['+str(sent_count)+']'+'\t'+offense+'['+str(len(sentence_list)+sent_count)+']'+"\n"
                    char_count_old = char_count +1
                    outfile.write(line)

                sent_count +=1

        
