import sys
sys.path.append("C:/Users/vivek/AppData/Local/Programs/Python/Python39/Lib/site-packages")
#sys.path.append("C:/Users/vivek/anaconda3/Lib/site-packages")
#from sklearn.model_selection import GridSearchCV
#import shap
#import matplotlib.pyplot as plt
import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier
#from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import sys
import numpy
import warnings
warnings.filterwarnings("ignore")

#shap.initjs()

f = open("ml_results.txt","w")
temp = sys.argv[1]
arr = [temp.split(',')]
#arr = [[1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,1,1]]
temp1 = numpy.asarray(arr)
temp2 = xgb.DMatrix(temp1)

#df_XSS_vuln = pd.read_csv("C:/xampp/htdocs/Ransomware-VAPT-master/Third_Module/FYP_datasets/XSS_vuln_cases_attributes.csv")
#df_XSS_non_vuln = pd.read_csv("C:/xampp/htdocs/Ransomware-VAPT-master/Third_Module/FYP_datasets/XSS_non_vuln_cases_attributes.csv")
#df_FI_vuln = pd.read_csv("C:/xampp/htdocs/Ransomware-VAPT-master/Third_Module/FYP_datasets/FI_attribute_bad.csv")
#df_FI_non_vuln = pd.read_csv("C:/xampp/htdocs/Ransomware-VAPT-master/Third_Module/FYP_datasets/FI_attribute_good.csv")
#df_SQLI_vuln = pd.read_csv("C:/xampp/htdocs/Ransomware-VAPT-master/Third_Module/FYP_datasets/SQLi_Bad_attribute_file.csv")
#df_SQLI_non_vuln = pd.read_csv("C:/xampp/htdocs/Ransomware-VAPT-master/Third_Module/FYP_datasets/SQLi_Good_attribute_file.csv")


# XSS


#xss_saved = open("C:/xampp/htdocs/Ransomware-VAPT-master/Third_Module/FYP_datasets/xss_vuln_pred_model.sav","rb")
#model_xss = pickle.load(xss_saved)
#y_pred = model_xss.predict(arr)

bst_xss = xgb.Booster({'nthread': 4})  # init model
bst_xss.load_model('C:/xampp/htdocs/FYP2/Third_Module/FYP_datasets/xss_vuln_model_type2_3.model')
y_pred = bst_xss.predict(temp2)
f.write('Prediction for XSS :\t\t')
f.write(str(y_pred))
f.write('\n')


#SQLi
#sqli_saved = open("C:/xampp/htdocs/Ransomware-VAPT-master/Third_Module/FYP_datasets/sqli_vuln_pred_model.sav","rb")
#model_sqli = pickle.load(sqli_saved)
#y_sqli_pred = model_sqli.predict(arr)
#f.write(y_sqli_pred)

bst_sqli = xgb.Booster({'nthread': 4})  # init model
bst_sqli.load_model('C:/xampp/htdocs/FYP2/Third_Module/FYP_datasets/sqli_vuln_model_type_over_1.model')
y_pred = bst_sqli.predict(temp2)
f.write('Prediction for SQLi :\t\t')
f.write(str(y_pred))
f.write('\n')


#File Inclusion
#fi_saved = open("C:/xampp/htdocs/Ransomware-VAPT-master/Third_Module/FYP_datasets/fi_vuln_pred_model.sav","rb")
#model_fi = pickle.load(fi_saved)
#y_fi_pred = model_fi.predict(arr)
#f.write(y_fi_pred)

bst_fi = xgb.Booster({'nthread': 4})  # init model
bst_fi.load_model('C:/xampp/htdocs/FYP2/Third_Module/FYP_datasets/fi_vuln_model_type2_3.model')
f.write('Prediction for File Inclusion :\t')
y_pred = bst_fi.predict(temp2)
f.write(str(y_pred))
#print("End reached")
#xss_saved.close()
#fi_saved.close()
#sqli_saved.clos()
f.close()
#explainer = shap.TreeExplainer(bst_sqli)
#shap_values = explainer.shap_values(temp1)
#fig = shap.summary_plot(shap_values, train, show=False)
#temp1 = temp1.reshape(17,)
#fig = shap.force_plot(explainer.expected_value, shap_values, temp1,link='logit', show=False,matplotlib=True).savefig('sqli_shap.png',bbox_inches='tight')
#plt.savefig('sqli_shap.png',bbox_inches='tight')
#print(temp1.shape)
#print(shap_values[0].shape)
