# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 10:23:46 2014

@author: david
"""
def server_call(procedures, state):
    largeframe =  pd.read_csv("/home/david/Desktop/Medicare-Physician-and-Other-Supplier-PUF-yz-CY2012.csv",header=1)
    results = largeframe.loc[(largeframe.nppes_provider_state == state) & (largeframe.hcpcs_description == procedures), ['nppes_provider_last_org_name', 'nppes_provider_first_name',"average_Medicare_allowed_amt","average_Medicare_payment_amt"]]
    results = results.sort(['average_Medicare_allowed_amt', 'average_Medicare_payment_amt'], ascending=[1, 0])
    return results.to_json()
