%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  conText
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'a la Carte' on Text (ConText) Embedding Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quanteda >= 3.0.0
BuildRequires:    R-CRAN-fastDummies >= 1.6.3
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-Matrix >= 1.3.2
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-text2vec >= 0.6
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-estimatr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-quanteda >= 3.0.0
Requires:         R-CRAN-fastDummies >= 1.6.3
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-Matrix >= 1.3.2
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-text2vec >= 0.6
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-estimatr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 

%description
A fast, flexible and transparent framework to estimate context-specific
word and short document embeddings using the 'a la carte' embeddings
approach developed by Khodak et al. (2018) <doi:10.48550/arXiv.1805.05388>
and evaluate hypotheses about covariate effects on embeddings using the
regression framework developed by Rodriguez et al.
(2021)<doi:10.1017/S0003055422001228>. New version of the package applies
a new estimator to measure the distance between word embeddings as
described in Green et al. (2025) <doi:10.1017/pan.2024.22>.

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
