"""
This code a slight modification of perplexity by hugging face
https://huggingface.co/docs/transformers/perplexity

Both this code and the orignal code are published under the MIT license.

by Burhan Ul tayyab and Nicholas Chua
"""

from model_korean import GPT2PPLV2 as GPT2PPL
import pandas as pd
from tqdm import tqdm
import pandas as pd
from sklearn.metrics import roc_curve, precision_recall_curve, auc, f1_score,  precision_score, recall_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import classification_report
# # initialize the model
model = GPT2PPL()

df = pd.read_csv('/home/kang/DetectGPT/data_kol/gen_concat_cate_f.csv', encoding='utf-8-sig')
cnt=0
result = []

for i in tqdm(range(len(df))):
    try:
        sentence = df['gen_text'][i]
        f = model(sentence, 20, "v1.1") #100
        cnt+=1
        print(cnt)
        prob = f[0]['prob'].split('%')[0]
        label = 'OR' if f[0]['label'] == 1 else 'CG'
        answer = df['label'][i]
        result.append([sentence, prob , label, answer])
        #result.append([sentence, label, answer])
        fin = pd.DataFrame(result, columns =['sentence', 'prob', 'pred_label', 'answer'])
        fin.to_csv('/home/kang/DetectGPT/result/detect_1113_v5.csv', encoding='utf-8-sig', index=False)
    except:
        pass

target_names = ['OR', 'CG']
print(classification_report(fin['answer'], fin['pred_label'], target_names=target_names))