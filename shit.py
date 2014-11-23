# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 16:29:07 2014

@author: david
"""

#MediCost Data Query Code

import pandas as pd
a =  pd.read_csv("/home/david/Desktop/Medicare-Physician-and-Other-Supplier-PUF-yz-CY2012.csv",header=1)

def subset(state,zipcode,service):
    #removed zipcode functionality until we figur eout how to make it user friendly
    b = a.loc[(a.nppes_provider_state == state) & (a.hcpcs_description == service), ['nppes_provider_last_org_name', 'nppes_provider_first_name',"average_Medicare_allowed_amt","average_Medicare_payment_amt"]]
    return  b.sort(['average_Medicare_allowed_amt', 'average_Medicare_payment_amt'], ascending=[1, 0])

#code to convert dataset for json if we got hat route
#a.to_json
