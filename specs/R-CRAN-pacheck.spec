%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pacheck
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Analysis Check Package

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-randomForestSRC 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-simsurv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-randomForestSRC 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-simsurv 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-survival 

%description
Investigate (analytically or visually) the inputs and outputs of
probabilistic analyses of health economic models using standard health
economic visualisation and metamodelling methods.

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
