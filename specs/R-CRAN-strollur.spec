%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  strollur
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Store and Transfer Amplicon Sequence Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildRequires:    R-CRAN-rbiom >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-microseq 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-waldo 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcereal 
Requires:         R-CRAN-rbiom >= 3.1.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-cli 
Requires:         R-methods 
Requires:         R-CRAN-microseq 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-waldo 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-yaml 
Requires:         R-stats 
Requires:         R-utils 

%description
Stores the data associated with your amplicon sequence analysis. This
includes nucleotide sequences, abundance, sample and treatment
assignments, taxonomic classifications, asv, otu and phylotype clusters,
metadata, trees and various reports. It is designed to facilitate data
analysis across multiple R packages with utility functions to read / write
from 'mothur', 'qiime2', 'dada2', and 'phyloseq'.

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
