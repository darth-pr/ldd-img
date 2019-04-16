# Welcome to the Imaging Local Data Dictionary (LDD)

The Imaging contains high level classes and attributes ...

This is a development repository for the Imaging LDD. The official releases of the Imaging LDD 
are available at <https://pds.jpl.nasa.gov/datastandards/schema/released>. Development releases are available at <https://github.com/nasa-pds-data-dictionaries/ldd-img/releases>. 

# Imaging LDD

## Dicationary Attributes

The following attributes are being used for ***development*** purposes: 

- Information Model Version: 1.11.0.0 
- Dictionary Version: 1.6.0.0


## Namespace Attributes

- Namespace Id: img
- XML Schema Namespace: http://pds.nasa.gov/pds4/img/v1
- XML Namespace Prefix: img
- Governance Level: Discipline
- Registration Authority: 0001_NASA_PDS_1
- Registration Date: 3-Apr-2012
- Registrar: S. LaVoie

## Stewardship

- Steward Name: Imaging
- Steward Id: img
- Steward Lead: PDS IMG Node

### Current Stewards

| Name | Affiliation | Role |
| ---- | ----------- | ----- |
| Cristina De Cesare | PDS IMG | lead steward |
| Jordan Padams | PDS EN | committer |
| Paul Ramirez | PDS IMG | committer |
| Trent Hare | PDS IMG | committer |
| Ron Joyner | PDS EN | release manager |

TODO: Insert reference to governance document that describes how to manage LDDs and the roles above. 
***

# Getting Started

## Useful Resources

- [*Installing and Configuring LDDTool*](http://sbndev.astro.umd.edu/wiki/Installing_and_Configuring_LDDTool)
- [*PDS Namespace Registry*](https://pds.jpl.nasa.gov/datastandards/schema/pds-namespace-registry.pdf)
- [*PDS4 Released Schemas*](https://pds.jpl.nasa.gov/datastandards/schema/released/)
- [*Documents Describing Planetary Data System version 4 (PDS4)*](https://pds.jpl.nasa.gov/datastandards/documents/)

## Building the Imaging 

Building the dictionary requires that you have installed the [LDD Tool](https://pds.nasa.gov/tools/about/ldd/). 

```
git clone https://github.com/nasa-pds-data-dictionaries/ldd-img.git
cd ldd-img
python setup.py lddtool
```

The outputs from running LDDTool are placed 'build' directory.

## Contributing


### Stewards

Stewards of the Imaging can commit directly to the dictionary repository but should generally follow the same process as the community. They also determine when, how, or whether a community patch gets merged back into the [canonical dictionary repository](https://github.com/nasa-pds-data-dictionaries/ldd-img). In order to commit to this repository one needs to be part of the [PDS Dictionary Stewards](https://github.com/orgs/nasa-pds-data-dictionaries/teams/pds-dictionary-stewards) and listed in the [Current Stewards](#Current-Stewards).


### Community

Contributions from the community are welcomed! These contributions will not be a part of an official releases until they pass PDS4 Data Dictionary Release Process. Before official release any community contirbution may be reverted. At the discretion of the steward(s) the requested changes will be merged, altered, or rejected into the the development version of the LDD. Please submit a patch or file an issue following the process described below.


### Submitting a Patch

To contribute a patch, follow these instructions.

1. File a GitHub issue at https://github.com/nasa-pds-data-dictionaries/ldd-img/issues/new. This will create an issue with an assigned issue ID .

2. [Fork the repo](http://help.github.com/fork-a-repo) on which you're working, clone your forked repo to your local computer, and set up the upstream remote:
    ```
    git clone https://github.com/<YourGitHubUserName>/ldd-img.git
    git remote add upstream https://github.com/nasa-pds-data-dictionaries/ldd-img.git
    ```
3. Go into ldd-img directory
    ```
    cd ldd-img
    ```
4. Checkout out a new local branch based on your master and update it to the latest. The convention is to name the branch after the current GitHub issue, e.g. LDD-IMG-xxx where xxx is the issue ID.
    ```
    git checkout -b LDD-IMG-xxx
    ```
5. Do the changes to the relavant files and keep your code clean. If you find another bug, you want to fix while being in a new branch, please fix it in a separated branch instead.

6. Add relevant files to the staging  area.
    ```
    git add <files>
    ```
7. For every commit please write a short (max 72 characters) summary of the change. Use markdown syntax for simple styling. Please include any GitHub issue numbers in your summary.
    ```
    git commit -m “[LDD-IMG-xxx] Put change summary here ”
    ```
    **NEVER leave the commit message blank!** Provide a detailed, clear, and complete description of your commit!

8. Before submitting a pull request, update your branch to the latest code.
    ```
    git checkout master
    git pull --rebase upstream master
    git checkout LDD-IMG-xxx
    git rebase -i master
    ```
9. Push the code to your forked repository
    ```
    git push origin ldd-img-xxx
    ```
10. In order to make a pull request,
  * Navigate to the ldd-img repository you just pushed to (e.g. https://github.com/<YourGitHubUserName>/ldd-img)
  * Click "Pull Request".
  * Write your branch name in the branch field (this is filled with "master" by default)
  * Click "Update Commit Range".
  * Ensure the changesets you introduced are included in the "Commits" tab.
  * Ensure that the "Files Changed" incorporate all of your changes.
  * Fill in some details about your potential patch including a meaningful title.
  * Click "Send pull request".

### Filing an Issue

If you encounter errors in ldd-img or want to suggest an improvement or a new
feature, please visit the ldd-img issue tracker 
https://github.com/nasa-pds-data-dictionaries/ldd-img/issues.  There you can also find the
latest information on known issues and recent bug fixes and enhancements.

***

# Imaging Dictionary Releases

The official releases of the Imaging LDD are available at <https://pds.jpl.nasa.gov/datastandards/schema/released>

## Latest Release:

- Release Date: December 6, 2018 
- Information Model Version: 1.10.1.0
- Dictionary Version: 1.5.1.0
- Dictionary: [PDS4_IMG_1A10_1510.JSON](https://pds.jpl.nasa.gov/datastandards/schema/released/img/v1/PDS4_IMG_1A10_1510.JSON)
- Schema: [PDS4_IMG_1A10_1510.xsd](https://pds.jpl.nasa.gov/datastandards/schema/released/img/v1/PDS4_IMG_1A10_1510.xsd)
- Schematron: [PDS4_IMG_1A10_1510.sch](https://pds.jpl.nasa.gov/datastandards/schema/released/img/v1/PDS4_IMG_1A10_1510.sch)
- Dictionary Label: [PDS4_IMG_1A10_1510.xml](https://pds.jpl.nasa.gov/datastandards/schema/released/img/v1/PDS4_IMG_1A10_1510.xml)

## Previous Releases:

| Namespace | Information Model Version | Dictionary Version | Release Artifacts |
| --------- | ------------------------- | ------------------ | ----------------- |

 
