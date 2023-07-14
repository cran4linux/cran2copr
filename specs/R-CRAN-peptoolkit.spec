%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  peptoolkit
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolkit for Using Peptide Sequences in Machine Learning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Peptides 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-Peptides 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-caret 

%description
This toolkit is designed for manipulation and analysis of peptides. It
provides functionalities to assist researchers in peptide engineering and
proteomics. Users can manipulate peptides by adding amino acids at every
position, count occurrences of each amino acid at each position, and
transform amino acid counts based on probabilities. The package offers
functionalities to select the best versus the worst peptides and analyze
these peptides, which includes counting specific residues, reducing
peptide sequences, extracting features through One Hot Encoding (OHE), and
utilizing Quantitative Structure-Activity Relationship (QSAR) properties
(based in the package 'Peptides' by Osorio et al. (2015)
<doi:10.32614/RJ-2015-001>). This package is intended for both researchers
and bioinformatics enthusiasts working on peptide-based projects,
especially for their use with machine learning.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
