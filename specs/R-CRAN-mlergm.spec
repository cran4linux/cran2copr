%global __brp_check_rpaths %{nil}
%global packname  mlergm
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Multilevel Exponential-Family Random Graph Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ergm >= 3.10.1
BuildRequires:    R-CRAN-sna >= 2.4
BuildRequires:    R-CRAN-network >= 1.15
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-ergm >= 3.10.1
Requires:         R-CRAN-sna >= 2.4
Requires:         R-CRAN-network >= 1.15
Requires:         R-parallel 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-lpSolve 

%description
Estimates exponential-family random graph models for multilevel network
data, assuming the multilevel structure is observed. The scope, at
present, covers multilevel models where the set of nodes is nested within
known blocks. The estimation method uses Monte-Carlo maximum likelihood
estimation (MCMLE) methods to estimate a variety of canonical or curved
exponential family models for binary random graphs. MCMLE methods for
curved exponential-family random graph models can be found in Hunter and
Handcock (2006) <DOI: 10.1198/106186006X133069>. The package supports
parallel computing, and provides methods for assessing goodness-of-fit of
models and visualization of networks.

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
