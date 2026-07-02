%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OUwie
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Evolutionary Rates in an OU Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-paleotree 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-phylolm 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-corHMM 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-paleotree 
Requires:         R-CRAN-phangorn 
Requires:         R-stats 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-interp 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-CRAN-phylolm 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-corHMM 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
Estimates rates for continuous character evolution under Brownian motion
and Ornstein-Uhlenbeck based Hansen models that allow both the strength of
the pull and stochastic motion to vary across selective regimes. Beaulieu
et al. (2012).

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
