%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GNGTools
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Go/No-Go Decision-Making Framework

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plyr 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-reshape2 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-janitor 
Requires:         R-parallel 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-tictoc 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rlang 

%description
Go/No-Go Decision-making Framework based on Bayesian posterior
probabilities linked to the target product profile.

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
