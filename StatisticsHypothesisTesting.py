
# Hypothesis Testing performed on a simple random input data, and another uploaded csv data for null hypothesis is are amount of carbohydrates in hot and cold cereal related
# 
# The following were calculated:
# 
# 1) interval estimate
# 2) point estimate
# 3) hypothesis testing
# 	a) z testing
# 	b) t testing



import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # data visualizationh
import matplotlib.pyplot as plt #more data visualization
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore') # ignore warnings
from scipy.stats import ttest_ind # for the t-test we'll be doing
from subprocess import check_output 
#print(check_output(["ls", "../input"]).decode("utf8"))
import math
import scipy.stats as st
from statsmodels.stats import weightstats as stests

# legend
# flag=1 just point estimate
# flag=2 just interval estimate
# flag=3 do all above
# flag=4 do all above
# flag_tail=1 1 tailed test
# flag_tail=2 2 tailed test
# csv_file=0 no csv upload
# csv_file=1 csv upload
#alpha='0.05z','0.025z','0.05t','0.025t' first 2 key value pair is for z table.
# last 2 values above for t table with 9 degree of freedom.So sample has to be taken 10 for t test.

cereal=pd.read_csv("cereal.csv")
        # cereal.head() check data 
        # cereal.shape check shape note row coloumns 
        # Store indexnames of carbohydrates in negative values
        # Problem statement are the amount of carbohydrates in hot and cold cerealas related?
        # Null hypothesis is calories in both types is related
        # Alternative hypothesis is it it is not related
siz=cereal.shape[0]

def stats_calc(population_mean,alpha, flag,flag_tail,csv_file,sample_mean=0, popstd_deviation=0,sampstd_deviation=0,sample_size=0):
#     sample_mean=float(input("Enter Sample Mean:"))
#     popstd_deviation=float(input("Enter Population Standard deviation:"))
#     sampstd_deviation=float(input("Enter Sample Standard deviation:"))
#     sample_size=float(input("Enter sample size:"))
    a='NA'
    b1='NA'
    b2='NA'
    z='NA'
    t='NA'
    ztest='NA'
    testvalue='NA'
    alphadic={'0.05z':1.645,'0.025z':1.96,'0.05t':1.83,'0.025t':2.26} # first 2 key value pair is for z table.
#   #  last 2 for t table with 9 degree of freedom.So sample has to be taken 10 for t test.
    if csv_file==0:
        if flag==1: # just point estimate
            a=sample_mean #point estimate
        if flag==2: # just interval estimate
            if sample_size>30:
                z=(sample_mean-population_mean)/(popstd_deviation/math.sqrt(sample_size)) # z score
                b1=sample_mean+(z*popstd_deviation/math.sqrt(sample_size))
                b2=sample_mean-(z*popstd_deviation/math.sqrt(sample_size))
                # interval estimate with z 
            elif sample_size<=30 and sample_size>0:
                t=(sample_mean-population_mean)/(sampstd_deviation/math.sqrt(sample_size)) # t score
                b1=sample_mean+(t*sampstd_deviation/math.sqrt(sample_size)) # interval estimate with t
                b2=sample_mean-(t*sampstd_deviation/math.sqrt(sample_size)) 
        if flag ==3: # just hypothesis testing
             
           
            if sample_size>30: #Null hypothesis with z test
                z=(sample_mean-population_mean)/(popstd_deviation/math.sqrt(sample_size)) # z score
               
                if flag_tail==1:
                     #Now null hypothesis be that population_mean value<5
                    #alternate is all the others
                    #right tail test
                    if population_mean<5:
                        if z<alphadic[alpha]:
                            print(f"This is Z distributiom and Accept null Hypothesis{z}<{alphadic[alpha]}")
                        if z>=alphadic[alpha]:
                            print(f"This is Z distributiom and Reject Null Hypothesis{z}>={alphadic[alpha]}")
                        
                     #Now null hypothesis be that population_mean value>5
                    #alternate is all the others
                    #left tail test
                    if population_mean>5:
                        if z>alphadic[alpha]:
                            print(f"This is Z distributiom and Accept null Hypothesis as {z}>{alphadic[alpha]}")
                        if z<=alphadic[alpha]:
                            print(f"This is Z distributiom and Reject Null Hypothesis{z}<={alphadic[alpha]}")
                        
                
                if flag_tail==2:
                    #Now null hypothesis be that population_mean value=5
                    #alternate hypohes is is all the others
                    #two tail test
                    # here take alpha 0.05 so alpha/2 0.025 for two tailed test
                    if z<alphadic[alpha] and z>-alphadic[alpha]:
                        print(f"This is Z distributiom and Accept null Hypothesis as {z}>{alphadic[alpha]} and z>-{alphadic[alpha]}")
                    else:
                        print(f"This is Z distributiom and Reject Null Hypothesis as {z} is in rejection region")
            elif sample_size<=30 and sample_size>0: #Null hypothesis with t test
                # Note take sample size as 10 to use t test as di cotains only t values for dof 9
                t=(sample_mean-population_mean)/(sampstd_deviation/math.sqrt(sample_size)) # t score
                
                if flag_tail==1:
                     #Now null hypothesis be that population_mean value<5
                    #alternate is all the others
                    #right tail test
                    if population_mean<5:
                        if t<alphadic[alpha]:
                            print(f"This is T distributiom and Accept null Hypothesis as {t}<{alphadic[alpha]}")
                        if t>=alphadic[alpha]:
                            print(f"This is T distributiom and Reject Null Hypothesis as {t}>={alphadic[alpha]}")
                        
                     #Now null hypothesis be that population_mean value>5
                    #alternate is all the others
                    #left tail test
                    if population_mean>5:
                        if t>alphadic[alpha]:
                            print(f"This is T distributiom and Accept null Hypothesis as {t}>{alphadic[alpha]}")
                        if t<=alphadic[alpha]:
                            print(f"This is T distributiom and Reject Null Hypothesis as {t}<={alphadic[alpha]}")
                
                if flag_tail==2:
                    #Now null hypothesis be that population_mean value=5
                    #alternate is all the others
                    #two tail test
                    # here take alpha 0.05 so alpha/2 0.025 for two tailed test
                    if t<alphadic[alpha] and t>-alphadic[alpha]:
                        print(f"This is T distributiom and Accept null Hypothesis as {t}<{alphadic[alpha]} and {t}>-{alphadic[alpha]}")
                    else:
                        print(f"This is T distributiom and Reject Null Hypothesis as {t} is in rejection region")                      
        if flag ==4: # point,interval and hypothesis testing
             
            a=sample_mean #point estimate
            if sample_size>30: #Null hypothesis with z test
                z=(sample_mean-population_mean)/(popstd_deviation/math.sqrt(sample_size)) # z score
                b1=sample_mean+(z*popstd_deviation/math.sqrt(sample_size)) # interval estimate with z
                b2=sample_mean-(z*popstd_deviation/math.sqrt(sample_size))
                if flag_tail==1:
                     #Now null hypothesis be that population_mean value<5
                    #alternate is all the others
                    #right tail test
                    if population_mean<5:
                        if z<alphadic[alpha]:
                            print(f"This is Z distributiom and Accept null Hypothesis{z}<{alphadic[alpha]}")
                        if z>=alphadic[alpha]:
                            print(f"This is Z distributiom and Reject Null Hypothesis{z}>={alphadic[alpha]}")
                        
                     #Now null hypothesis be that population_mean value>5
                    #alternate is all the others
                    #left tail test
                    if population_mean>5:
                        if z>alphadic[alpha]:
                            print(f"This is Z distributiom and Accept null Hypothesis as {z}>{alphadic[alpha]}")
                        if z<=alphadic[alpha]:
                            print(f"This is Z distributiom and Reject Null Hypothesis{z}<={alphadic[alpha]}")
                        
                
                if flag_tail==2:
                    #Now null hypothesis be that population_mean value=5
                    #alternate hypohes is is all the others
                    #two tail test
                    # here take alpha 0.05 so alpha/2 0.025 for two tailed test
                    if z<alphadic[alpha] and z>-alphadic[alpha]:
                        print(f"This is Z distributiom and Accept null Hypothesis as {z}<{alphadic[alpha]} and {z}>-{alphadic[alpha]}")
                    else:
                        print(f"This is Z distributiom and Reject Null Hypothesis as {z} is in rejection region")
            elif sample_size<=30 and sample_size>0: #Null hypothesis with t test
                # Note take sample size as 10 to use t test as di cotains only t values for dof 9
                t=(sample_mean-population_mean)/(sampstd_deviation/math.sqrt(sample_size)) # z score
                b1=sample_mean+(t*sampstd_deviation/math.sqrt(sample_size)) # interval estimate with t
                b2=sample_mean-(t*sampstd_deviation/math.sqrt(sample_size))
                if flag_tail==1:
                     #Now null hypothesis be that population_mean value<5
                    #alternate is all the others
                    #right tail test
                    if population_mean<5:
                        if t<alphadic[alpha]:
                            print(f"This is T distributiom and Accept null Hypothesis as {t}<{alphadic[alpha]}")
                        if t>=alphadic[alpha]:
                            print(f"This is T distributiom and Reject Null Hypothesis as {t}>={alphadic[alpha]}")
                        
                     #Now null hypothesis be that population_mean value>5
                    #alternate is all the others
                    #left tail test
                    if population_mean>5:
                        if t>alphadic[alpha]:
                            print(f"This is T distributiom and Accept null Hypothesis as {t}>{alphadic[alpha]}")
                        if t<=alphadic[alpha]:
                            print(f"This is T distributiom andReject Null Hypothesis as {t}<={alphadic[alpha]}")
                
                if flag_tail==2:
                    #Now null hypothesis be that population_mean value=5
                    #alternate is all the others
                    #two tail test
                    # here take alpha 0.05 so alpha/2 0.025 for two tailed test
                    if t<alphadic[alpha] and t>-alphadic[alpha]:
                        print(f"This is T distributiom and Accept null Hypothesis as {t}<{alphadic[alpha]} and {t}>-{alphadic[alpha]}")
                    else:
                        print(f"This is T distributiom and Reject Null Hypothesis as {t} is in rejection region")
        print(f"Point estimate is {a}")
        print(f"Interval Estimate is  ({b2},{b1})")
        return a,b2,b1,z,t
    
    
    
    elif csv_file==1:
       
        
        indexNames = cereal[ cereal['carbo']<0 ].index
        # Delete these row indexes from dataFrame
        cereal.drop(indexNames , inplace=True)
        hot_cereal = cereal.loc[cereal['type'] == 'H', :] # define a hot_cereal 
        cold_cereal = cereal.loc[cereal['type'] == 'C', :] # definte a cold_cereal
        a=np.mean(cereal['carbo']) #point estimate of carbohyrates in cereal
        a1=np.mean(hot_cereal['carbo']) #point estimate of carbohyrates in hot cereal
        a2=np.mean(cold_cereal['carbo']) #point estimate of carbohyrates in cold cereal
         
        #Let's Visualize
        ax = plt.subplots(figsize=(18,8)) # make our plot larger
        # plot the cold cereal sugar distribution
        sns.distplot(cold_cereal['carbo'], bins = 10, hist = True,  label = 'cold')
        # plot the hot cereal sugar distribution
        sns.distplot(hot_cereal['carbo'], bins = 10, hist = True, label = 'hot') 
        plt.legend() #show legend
        #confidence interval of hot creal carbohydrate content
        b1=st.t.interval(alpha=0.95, df=len(hot_cereal['carbo'])-1, loc=np.mean(hot_cereal['carbo']), scale=st.sem(hot_cereal['carbo'])) 
        #confidence interval of cold cereal carbohydrate content
        b2=st.t.interval(alpha=0.95, df=len(hot_cereal['carbo'])-1, loc=np.mean(cold_cereal['carbo']), scale=st.sem(cold_cereal['carbo']))
        
        # null hypothesis is are amount of carbohydrates in hot and cold cereal related
        # alternate hypothesis is are amount of carbohydrates in hot and cold cereal not related
        
        if sample_size<=30:# T Test
            testvalue=ttest_ind(cold_cereal['carbo'], hot_cereal['carbo'], equal_var = False)
            print(f"The T score is {testvalue}")
            if testvalue[0]>=alphadic[alpha] or testvalue[0]<=-alphadic[alpha]:
                print("This is T test and we reject Null hypotheis")
            if testvalue[0]<alphadic[alpha] and testvalue[0]>-alphadic[alpha]:
                print("This is T test and we accept Null hypotheis") 
        elif sample_size>30:# Z Test
            ztest ,pval1 = stests.ztest(hot_cereal['carbo'], x2=cold_cereal['carbo'], alternative='two-sided')
            print(f"The Z Test value is {ztest} and pvalue is {pval1}")
            if ztest>=alphadic[alpha] or ztest<=-alphadic[alpha]:
                print("This is Z test and we reject Null hypotheis")
            if ztest<alphadic[alpha] and ztest>-alphadic[alpha]:
                print("This is Z test and accept Null hypotheis")
        print(f"Point estimate is {a}")
        print(f"Interval Estimate for cold cereal carbohydrates is {b2} and for hot cereal carbohydrates is {b1}")
        return a,b1,b2,ztest,testvalue[0]
    
# def stats_calc(population_mean,alpha, flag,flag_tail,csv_file,sample_mean=0, popstd_deviation=0,sampstd_deviation=0,sample_size=0)
                                
stats_calc(6.35,'0.025z',4,2,0,7.4, 2.6,2.9,20)                    
                   