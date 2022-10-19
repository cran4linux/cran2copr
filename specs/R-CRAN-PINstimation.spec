%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PINstimation
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of the Probability of Informed Trading

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-skellam 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-knitr 
Requires:         R-methods 
Requires:         R-CRAN-skellam 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-coda 

%description
A comprehensive bundle of utilities for the estimation of probability of
informed trading models: original PIN in Easley and O'Hara (1992) and
Easley et al. (1996); Multilayer PIN (MPIN) in Ersan (2016); Adjusted PIN
(AdjPIN) in Duarte and Young (2009); and volume-synchronized PIN (VPIN) in
Easley et al. (2011, 2012). Implementations of various estimation methods
suggested in the literature are included. Additional compelling features
comprise posterior probabilities, an implementation of an
expectation-maximization (EM) algorithm, and PIN decomposition into
layers, and into bad/good components. Versatile data simulation tools, and
trade classification algorithms are among the supplementary utilities. The
package provides fast, compact, and precise utilities to tackle the
sophisticated, error-prone, and time-consuming estimation procedure of
informed trading, and this solely using the raw trade-level data.

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
