%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mpactr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Correction of Preprocessed MS Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-treemapify 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-treemapify 
Requires:         R-CRAN-viridis 

%description
An 'R' implementation of the 'python' program Metabolomics Peak Analysis
Computational Tool ('MPACT') (Robert M. Samples, Sara P. Puckett, and
Marcy J. Balunas (2023) <doi:10.1021/acs.analchem.2c04632>). Filters in
the package serve to address common errors in tandem mass spectrometry
preprocessing, including: (1) isotopic patterns that are incorrectly split
during preprocessing, (2) features present in solvent blanks due to
carryover between samples, (3) features whose abundance is greater than
user-defined abundance threshold in a specific group of samples, for
example media blanks, (4) ions that are inconsistent between technical
replicates, and (5) in-source fragment ions created during ionization
before fragmentation in the tandem mass spectrometry workflow.

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
