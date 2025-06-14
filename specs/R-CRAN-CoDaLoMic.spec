%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CoDaLoMic
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Compositional Models to Longitudinal Microbiome Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-ggbiplot 
BuildRequires:    R-CRAN-zCompositions 
BuildRequires:    R-utils 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-compositions 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-ggbiplot 
Requires:         R-CRAN-zCompositions 
Requires:         R-utils 

%description
Implementation of models to analyse compositional microbiome time series
taking into account the interaction between groups of bacteria. The models
implemented are described in Creus-Martí et al (2018,
ISBN:978-84-09-07541-6), Creus-Martí et al (2021)
<doi:10.1155/2021/9951817> and Creus-Martí et al (2022)
<doi:10.1155/2022/4907527>.

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
