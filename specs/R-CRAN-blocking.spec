%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blocking
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Various Blocking Methods for Entity Resolution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-text2vec 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-RcppHNSW 
BuildRequires:    R-CRAN-RcppAnnoy 
BuildRequires:    R-CRAN-mlpack 
BuildRequires:    R-CRAN-rnndescent 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppAlgos 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-text2vec 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-RcppHNSW 
Requires:         R-CRAN-RcppAnnoy 
Requires:         R-CRAN-mlpack 
Requires:         R-CRAN-rnndescent 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RcppAlgos 
Requires:         R-methods 
Requires:         R-CRAN-readr 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 

%description
The goal of 'blocking' is to provide blocking methods for record linkage
and deduplication using approximate nearest neighbour (ANN) algorithms and
graph techniques. It supports multiple ANN implementations via
'rnndescent', 'RcppHNSW', 'RcppAnnoy', and 'mlpack' packages, and provides
integration with the 'reclin2' package. The package generates shingles
from character strings and similarity vectors for record comparison, and
includes evaluation metrics for assessing blocking performance including
false positive rate (FPR) and false negative rate (FNR) estimates. For
details see: Papadakis et al. (2020) <doi:10.1145/3377455>, Steorts et al.
(2014) <doi:10.1007/978-3-319-11257-2_20>, Dasylva and Goussanou (2021)
<https://www150.statcan.gc.ca/n1/en/catalogue/12-001-X202100200002>,
Dasylva and Goussanou (2022) <doi:10.1007/s42081-022-00153-3>.

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
