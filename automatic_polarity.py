import re
import pandas
import snorkel
from snorkel.labeling import labeling_function
from snorkel.labeling import PandasLFApplier

df = pandas.read_csv('BrazilianTweetsDataset.csv', sep='\t')

@labeling_function()
def maravilhosa(x):
    return Positiva if re.search(r"maravil.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def respeito(x):
    return Positiva if re.search(r"respeit.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def parabens(x):
    return Positiva if "parabéns" in x.text.lower() else ABSTAIN

@labeling_function()
def otimo(x):
    return Positiva if re.search(r"ótim.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def perfeito(x):
    return Positiva if re.search(r"perfeit.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def bonito(x):
    return Positiva if re.search(r"bonit.", x.text, flags=re.I) else ABSTAIN                                 

@labeling_function()
def amo(x):
    return Positiva if re.search(r"amo.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def haha(x):
    return Positiva if re.search(r"haha.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def kk(x):
    return Positiva if re.search(r"kk.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def beijo(x):
    return Positiva if re.search(r"beij.", x.text, flags=re.I) else ABSTAIN                                    

@labeling_function()
def normal(x):
    return Neutra if re.search(r"norm.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def laico(x):
    return Neutra if "laico" in x.text.lower() else ABSTAIN 
                               
@labeling_function()
def homicidio(x):
    return Negativa if "homicídio" in x.text.lower() else ABSTAIN

@labeling_function()
def pqp(x):
    return Negativa if "pqp" in x.text.lower() else ABSTAIN

@labeling_function()
def crime(x):
    return Negativa if re.search(r"crim.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def demente(x):
    return Negativa if "demente" in x.text.lower() else ABSTAIN

@labeling_function()
def burro(x):
    return Negativa if re.search(r"burr.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def imbecil(x):
    return Negativa if re.search(r"imbec.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def merda(x):
    return Negativa if re.search(r"merd.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def canalha(x):
    return Negativa if re.search(r"canalha.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def vtnc(x):
    return Negativa if "vtnc" in x.text.lower() else ABSTAIN                                 

@labeling_function()
def facista(x):
    return Negativa if re.search(r"facis.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def estupido(x):
    return Negativa if re.search(r"estupid.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def vagabundo(x):
    return Negativa if re.search(r"vagabund.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def escroto(x):
    return Negativa if re.search(r"escrot.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def podre(x):
    return Negativa if "podre" in x.text.lower() else ABSTAIN

@labeling_function()
def odeio(x):
    return Negativa if re.search(r"odei.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def gayzada(x):
    return Negativa if "gayzada" in x.text.lower() else ABSTAIN

@labeling_function()
def desgraça(x):
    return Negativa if re.search(r"desgraç.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def prostituta(x):
    return Negativa if re.search(r"prostitu.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def idiota(x):
    return Negativa if re.search(r"idiota.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def puta(x):
    return Negativa if re.search(r"puta.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def mimimi(x):
    return Negativa if re.search(r"mimi.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def porra(x):
    return Negativa if "porra" in x.text.lower() else ABSTAIN

@labeling_function()
def hipocrita(x):
    return Negativa if re.search(r"hipócrit.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def odio(x):
    return Negativa if "ódio" in x.text.lower() else ABSTAIN

@labeling_function()
def intolerante(x):
    return Negativa if re.search(r"intoleran.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def cu(x):
    return Negativa if re.search(r"cu.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def transfobia(x):
    return Negativa if re.search(r"transfob.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def ridiculo(x):
    return Negativa if re.search(r"ridícul.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def caralho(x):
    return Negativa if "caralho" in x.text.lower() else ABSTAIN

@labeling_function()
def genocida(x):
    return Negativa if "genocida" in x.text.lower() else ABSTAIN

@labeling_function()
def traveco(x):
    return Negativa if "traveco" in x.text.lower() else ABSTAIN

@labeling_function()
def triste(x):
    return Negativa if "triste" in x.text.lower() else ABSTAIN

@labeling_function()
def covarde(x):
    return Negativa if "covarde" in x.text.lower() else ABSTAIN

@labeling_function()
def assassino(x):
    return Negativa if re.search(r"assassin.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def espancar(x):
    return Negativa if re.search(r"espanc.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def fanatico(x):
    return Negativa if re.search(r"fanátic.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def racismo(x):
    return Negativa if re.search(r"racis.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def xenofobia(x):
    return Negativa if re.search(r"xenof.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def homofobia(x):
    return Negativa if re.search(r"homof.", x.text, flags=re.I) else ABSTAIN

@labeling_function()
def lixo(x):
    return Negativa if "lixo" in x.text.lower() else ABSTAIN

lfs = [maravilhosa, respeito, parabens, otimo, perfeito, bonito, amo, haha, kk, beijo, normal, laico, homicidio, pqp, crime, demente, burro, imbecil, merda, canalha, vtnc, facista, estupido, vagabundo, escroto, podre, odeio, gayzada, desgraça, prostituta, idiota, puta, mimimi, porra, hipocrita, odio, intolerante, cu, transfobia, ridiculo, caralho, genocida, traveco, triste, covarde, assassino, espancar, fanatico, racismo, xenofobia, homofobia, lixo]                                 

applier = PandasLFApplier(lfs=lfs)
L_train = applier.apply(df=df)

label_model = LabelModel(cardinality=3, verbose=True)
label_model.fit(L_train, n_epochs=500, log_freq=50)
df["label"] = label_model.predict(L=L_train, tie_break_policy="abstain")
