%global __brp_check_rpaths %{nil}
%global packname  drpop
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Doubly Robust Population Size Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ranger 
Requires:         R-stats 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-nnls 
Requires:         R-parallel 
Requires:         R-CRAN-ranger 

%description
Estimation of the total population size from capture-recapture data
efficiently and with low bias implementing the methods from Das M, Kennedy
EH, and Jewell NP (2021) <arXiv:2104.14091>. The estimator is doubly
robust against errors in the estimation of the intermediate nuisance
parameters. Users can choose from the flexible estimation models provided
in the package, or use any other preferred model.

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
