%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPTCM
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Promotion Time Cure Model with Bayesian Shrinkage Priors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-riskRegression 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-miCoPTCM 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-riskRegression 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-miCoPTCM 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 

%description
Generalized promotion time cure model (GPTCM) via Bayesian hierarchical
modeling for multiscale data integration (Zhao et al. (2025)
<doi:10.48550/arXiv.2509.01001>). The Bayesian GPTCMs are applicable for
both low- and high-dimensional data.

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
