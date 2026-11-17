%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spDBL
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Bayesian Learning for Spatiotemporal Mechanistic Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-matrixsampling 
BuildRequires:    R-CRAN-mniw 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-matrixsampling 
Requires:         R-CRAN-mniw 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-readr 

%description
Emulates the output of spatiotemporal mechanistic simulators, a field on a
spatial grid at each time step, with a matrix-variate dynamic linear model
whose posterior is available in closed form, processing large grids as
sequences of spatial blocks, and predicts the output at untried inputs.
Calibrates simulator parameters to noisy field data without further
simulator runs: a design Gaussian process supplies the emulator's
autoregressive inputs, and 'Stan' (through the suggested package 'rstan')
samples the parameters conditionally on emulator posterior draws, with the
emulator field and a dynamic spatial discrepancy integrated out. Follows
Banerjee, Chen, Frankenburg and Zhou (2025)
<https://jmlr.org/papers/v26/22-0896.html>.

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
