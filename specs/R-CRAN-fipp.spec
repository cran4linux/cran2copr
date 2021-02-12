%global packname  fipp
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Induced Priors in Bayesian Mixture Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-matrixStats 

%description
Computes implicitly induced quantities from prior/hyperparameter
specifications of three Mixtures of Finite Mixtures models: Dirichlet
Process Mixtures (DPMs; Escobar and West (1995)
<doi:10.1080/01621459.1995.10476550>), Static Mixtures of Finite Mixtures
(Static MFMs; Miller and Harrison (2018)
<doi:10.1080/01621459.2016.1255636>), and Dynamic Mixtures of Finite
Mixtures (Dynamic MFMs; Frühwirth-Schnatter, Malsiner-Walli and Grün
(2020) <arXiv:2005.09918>). For methodological details, please refer to
Greve, Grün, Malsiner-Walli and Frühwirth-Schnatter (2020)
<arXiv:2012.12337>) as well as the package vignette.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
