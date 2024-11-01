%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BSTZINB
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Association Among Disease Counts and Socio-Environmental Factors

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-BayesLogit 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-gtsummary 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-BayesLogit 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-gtsummary 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-viridis 

%description
Estimation of association between disease or death counts (e.g. COVID-19)
and socio-environmental risk factors using a zero-inflated Bayesian
spatiotemporal model. Non-spatiotemporal models and/or models without
zero-inflation are also included for comparison. Functions to produce
corresponding maps are also included. See Chakraborty et al. (2022)
<doi:10.1007/s13253-022-00487-1> for more details on the method.

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
