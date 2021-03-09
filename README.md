# A corpus for offensive language detection and sentiment analysis in Brazilian Portuguese
Mini-project for the Linguistic Corpus Annotation course at the University of Tübingen, Winter semester 2020/2021.

# Goals
- Create a corpus of tweets in Portuguese (non-standard language)
- Consider the current political and social context in Brazil (2020/2021)
- Contribute to the field of hate speech detection
- Analyze the linguistic differences between offensive and not offensive language
- Analyze the different ways offensive language is expressed

# Data
- 792 replies to news regarding the LGBTQIA+ community, politics, race, religion and women. 
  - Religion: 160
  - LGBTQ: 170 
  - Politics: 158
  - Race: 146
  - Women: 158
- Data acquired from the four biggest Brazilian news outlets: Estadão, Folha, G1 and O Globo.

# Annotations
- Polarity (positive, negative, neutral)
- Language (offensive, not offensive)
- POS tags
- Dependency relations

# Results
- Two different corpora for different purposes:
  - A CSV dataset with polarity and sentiment annotations
  - A WebAnno TSV dataset with POS, dependency relations and sentence-level polarity and sentiment annotations 

# Future work
- Expand corpus
- Equalize class distribution (the data is currently imbalanced)
- Add irony annotation
- Consider emojis
- Develop a more refined annotation scheme (offensive/hate speech)

