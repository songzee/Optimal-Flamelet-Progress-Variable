# -*- coding:utf-8 -*- 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import readdata
from scipy.optimize import minimize

def optimal(XX,YY,ZZ):

	mzlib=1000
	mzprimlib=50
	mxlib=49
	ns=9
	CC=np.zeros((mxlib-1,mzlib))
	Czst=np.zeros((mxlib-1))	
	ZST=1.0/(1.0+8.0*1/0.245)
	Q=0
	A=0



	# for i in range(mzprimlib-1) :
	for j in range (mxlib-1) :
		for k in range (mzlib) :
			CC[j,k]= XX[0]*YY[0,j,k,0]+XX[1]*YY[2,j,k,0]+XX[2]*YY[6,j,k,0]
	XX[3]=np.amin(CC)
	XX[4]=np.amax(CC)


	
	# for i in range(mzprimlib-1) :
	
	for k in range (mzlib) :
    		for j in range (mxlib-2) :
    			 for i in range (j+1,mxlib-2) :
        			if CC[j,k]>CC[i,k]:
        				A=CC[j,k]
        				CC[j,k]=CC[i,k]
        				CC[i,k]=A



	# for i in range(mzprimlib-1) :
	for j in range (mxlib-1) :
		for k in range (mzlib-1) :
			if ZST>ZZ[k] and ZST<ZZ[k+1]:
				Czst[j]=CC[j,k]+(ZST-ZZ[k])/(ZZ[k+1]-ZZ[k])*(CC[j,k+1]-CC[j,k])



	# for i in range(mzprimlib-1) :
	for k in range (1,mzlib-1) :
        	for j in range (mxlib-2) :
        		if (CC[j+1,k]-CC[j,k])/(Czst[j+1]-Czst[j])<0:
        			Q=Q+CC[j,k]*0.5*(ZZ[k+1]-ZZ[k-1])*0.5*(Czst[j+1]-Czst[j-1]) 
    
	return Q



mzlib=1000
mzprimlib=50
mxlib=49
ns=9
ZST=1.0/(1.0+8.0*1/0.245)
QQ=0

XX=[0 for i in range(5)]
XX[0]=1
XX[1]=1
XX[2]=1
print XX

YY=np.zeros((ns-1,mxlib-1,mzlib,mzprimlib-1))		
WW=np.zeros((mxlib-1,mzlib,mzprimlib-1))
ZZ=np.zeros(1000)
[YY,ZZ,WW]=readdata.readdata(mzlib,mzprimlib,mxlib,ns)
res = minimize(optimal,XX,args=(YY,ZZ),bounds=((-1,1),(-1,1),(-1,1),(0,1),(0.98,1)),method='TNC', tol=1e-6)
print res.x 
print res









