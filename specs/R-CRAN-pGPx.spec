%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pGPx
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Pseudo-Realizations for Gaussian Process Excursions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-KrigInv 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-KrigInv 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-pracma 
Requires:         R-grDevices 

%description
Computes pseudo-realizations from the posterior distribution of a Gaussian
Process (GP) with the method described in Azzimonti et al. (2016)
<doi:10.1137/141000749>. The realizations are obtained from simulations of
the field at few well chosen points that minimize the expected distance in
measure between the true excursion set of the field and the approximate
one. Also implements a R interface for (the main function of) Distance
Transform of sampled Functions
(<https://cs.brown.edu/people/pfelzens/dt/index.html>).

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
