%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gctsc
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling Count Time Series Data via Gaussian Copula Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-TruncatedNormal 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-TruncatedNormal 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-car 
Requires:         R-CRAN-truncnorm 

%description
Gaussian copula models for count time series. Includes simulation
utilities, likelihood approximation, maximum-likelihood estimation,
residual diagnostics, and predictive inference. Implements the Time Series
Minimax Exponential Tilting (TMET) method, an adaptation of Minimax
Exponential Tilting (Botev, 2017) <doi:10.1111/rssb.12162> and the
Vecchia-based tilting framework of Cao and Katzfuss (2025)
<doi:10.1080/01621459.2025.2546586>. Also provides a linear-cost
implementation of the Geweke–Hajivassiliou–Keane (GHK) simulator inspired
by Masarotto and Varin (2012) <doi:10.1214/12-EJS721>, and the Continuous
Extension (CE) approximation of Nguyen and De Oliveira (2025)
<doi:10.1080/02664763.2025.2498502>. The package follows the S3 structure
of 'gcmr', but all code in 'gctsc' was developed independently.

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
