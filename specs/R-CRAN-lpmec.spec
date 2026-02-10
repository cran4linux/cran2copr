%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lpmec
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Measurement Error Analysis and Correction Under Identification Restrictions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sensemakr 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-emIRT 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-reticulate 
Requires:         R-stats 
Requires:         R-CRAN-sensemakr 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-emIRT 
Requires:         R-CRAN-gtools 

%description
Implements methods for analyzing latent variable models with measurement
error correction, including Item Response Theory (IRT) models. Provides
tools for various correction methods such as Bayesian Markov Chain Monte
Carlo (MCMC), over-imputation, bootstrapping for robust standard errors,
Ordinary Least Squares (OLS), and Instrumental Variables (IV) based
approaches. Supports flexible specification of observable indicators and
groupings for latent variable analyses in social sciences and other
fields. Methods are described in a working paper (2025)
<doi:10.48550/arXiv.2507.22218>.

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
