%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WINS
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          The R WINS Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-viridis 

%description
Calculate the win statistics (win ratio, net benefit and win odds) for
prioritized multiple endpoints, plot the win statistics and win
proportions over study time if at least one time-to-event endpoint is
analyzed, and simulate datasets with dependent endpoints. The package can
handle any type of outcomes (continuous, ordinal, binary, time-to-event)
and allow users to perform stratified analysis, inverse probability of
censoring weighting (IPCW) and inverse probability of treatment weighting
(IPTW) analysis.

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
