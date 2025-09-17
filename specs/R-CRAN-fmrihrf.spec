%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fmrihrf
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hemodynamic Response Functions for fMRI Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-numDeriv 
Requires:         R-splines 
Requires:         R-CRAN-pracma 

%description
Creates, manipulates, and evaluates hemodynamic response functions and
event-related regressors for functional magnetic resonance imaging data
analysis. Supports multiple basis sets including Canonical, Gamma,
Gaussian, B-spline, and Fourier bases. Features decorators for
time-shifting and blocking, and efficient convolution algorithms for
regressor construction. Methods are based on standard fMRI analysis
techniques as described in Jezzard et al. (2001, ISBN:9780192630711).

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
