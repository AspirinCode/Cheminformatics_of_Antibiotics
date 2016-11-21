# Cheminformatics_of_Antibiotics
EPP622 Final Project - Sarah Cooper

I started to make a wiki but ran into some difficulty inserting images and formatting things the way I wanted.

The layout of this github page is as follows (ordered how it appears on the page not by order used for project):

1. analysis     

     Analysis contains the correlation results. The files _e.coli_12_descriptors.xlsx_ and _pae_12_descriptors.xlsx_ contain the initial test set of 12 molecules which was later expanded to 20 molecules (_e.coli_pae_correlated.xlsx_) and to all available molecules (_all_correlated.xlsx_). 

    Both _e.coli_12_descriptors.xlsx_ and _pae_2_descriptors.xlsx_ contain example scatterplots of some highly correlating data. This data was not included in the summary as these correlations changed when the dataset was increased to include 20 molecules which is more statistically significant. 

    **_e.coli_pae_correlated.xlsx_ is the main file to look at for my results. This file is color coded with a key on the right side of each correlation matrix. The correlation matrix is also color coded to make it easier to see highly correlating variables and easily observe trends. This spreadsheet is interactive and cells with a red triangle in the upper right corner have either more information about that particular descriptor or if it's part of the correlation matrix has the scatterplot of the data. To view this hover the mouse over the cell.
    
    Due to the lack of high correlations, _all_correlated.xlsx_ is color coded but does not have the individual scatterplots embedded in the worksheet.

2. raw_data     
  
  This folder contains the raw data for the correlations. _E.coli_pae_all_moe.xlsx_ contains all of the MOE descriptors. The MIC data is not provided but can be seen in _e.coli_pae_correlated.xlsx_. Also provided in raw_data is the structures of all of the molecules used. Molecules are present in PDB, XYZ, and MOL2 formats which we often use, each of which contains slightly differnet information/formatting. Structures are separated based on whether they were optimized with quantum mechanics or minimized using MOE.
   
3. refs   

  This folder contains references used in this project. These include papers that cover background information and experimental set up as well as information about how the descriptors are calculated and what they mean.

4. scripts

   This folder contains all of the scripts adapted and used for this work. Scripts are either in python or bash. Adapted scripts were originally written in csh and I translated this to python and am able to make changes for running simulations on new systems.  
   
    _1_qm_opt.py_   
      This script is used to generate Gaussian09 input files from a list of antibiotics. This file only requires the coordinates to be added and then it is ready for submission to Gaussian on Newton. Gaussian input files only require the header information that contains all of the instructions on how to run the simulation, a filename, charge and multiplicity of the molecule and the coordinates. To check for negative frequencies use the coordinates from the optimization output file and replace the word opt in the header lines with freq.

    _2_prep_md.py_    
    This script uses python to take a template file and iterating through a list in a separate file makes the necessary directories for the MD simulations and adds the appropriate files to run the simulations. This code was adapted from an earlier script to set up other MD simulations.

    _3_run_plumed.py_    
    This script uses python to copy over the necessary template files to a certain directory similar to (2) and run the program PLUMED. Note this cannot be run on Newton it was run on the clusters at ORNL where the program is installed. This code was adapted from an earlier script to set up other MD simulations.

    _download_pdb.py_    
    This script allows you to download PDB files to the current directory and requires only the PDB ID’s in the command line when executing the script. While I originally wrote this for the first project I proposed it'll be super helpful for other projects.

  _g09_freq.py_    
  This script is used to check for negative frequencies in geometry optimizations. Negative frequencies arise from structures that while considered optimized do not represent a real molecule. 
 
  _rename.sh_   
  This short bash script is used to batch rename files. 

  _replace.sh_   
  This short bash script is used to batch replace a string in files.
   
5. README.md   

   General overview and organization of the github page

6. epp622_presentation_cooper.pptx

   A copy of my presentation from class 11-21-16.

7. eppy22_project_summary_cooper.docx

   Here is the official summary/report. I have combined the "lab notebook" and summary into one as it helped to describe the methods. Code is not explicetly shown for the scripts since some are longer but the code can be viewed in the scripts folder.
