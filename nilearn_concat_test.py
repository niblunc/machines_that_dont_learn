# -*- coding: utf-8 -*-
#"""
#Created on Tue Jun 27 10:40:10 2017

#@author:nibl
#"""

#this imports all the commands needed for the script to work#
import os
import numpy as np
import nilearn
import matplotlib
import glob
import nibabel as nib
from nilearn.image import concat_imgs, index_img


################################################
#Concatinate mutplie fxnl files into one for decoding

################################################
#set basepath
basepath=os.path.join('/Users','nibl','github','nilearn_concat')

################################################
#from neurostars: 

#before this we need to change the affine of both images to make them the same -GES
output = concat_imgs([os.path.join(basepath,'csimag_set1.nii.gz'),
                      os.path.join(basepath,'csimag_set2.nii.gz')],
                     memory_level=0, auto_resample=False, verbose=0)

outfile=os.path.join(basepath,'test_7_5.nii.gz')
nib.save(output, outfile) 


#load the indivdual fxnl data
#create list via glob, wildcards etc....
#if no wildcards, use brackets for list like
    #allthebrains=concat_imgs(['dataset/subject1.nii', 'dataset/subject2.nii']) 
listofiles=glob.glob(os.path.join(basepath, 'cs_imagine_set*.nii.gz'))

#actaully concatinate the files, all options below
output=concat_imgs(listofiles, auto_resample=True)
print(output)

#Save the concatinated file
outfile=os.path.join(basepath,'testies.nii.gz')
nib.save(output, outfile)                                 


#nilearn.image.concat_imgs(niimgs, dtype=<type ‘numpy.float32’>, 
                            #ensure_ndim=None, memory=Memory(cachedir=None), 
                            #memory_level=0, auto_resample=False, verbose=0)

#Parameters:	
#niimgs: iterable of Niimg-like objects or glob pattern

#dtype: numpy dtype, optional
    #the dtype of the returned image

#ensure_ndim: integer, optional
    #Indicate the dimensionality of the expected niimg. 
    #An error is raised if the niimg is of another dimensionality.

#auto_resample: boolean
    #Converts all images to the space of the first one.

#verbose: int
    #Controls the amount of verbosity (0 means no messages).

#memory : instance of joblib.Memory or string
    #Used to cache the resampling process. By default, no caching is done. 
    #If a string is given, it is the path to the caching directory.

#memory_level : integer, optional
    #Rough estimator of the amount of memory used by caching. 
    #Higher value means more memory for caching.
                