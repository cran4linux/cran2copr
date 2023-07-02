%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dwp
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Density-Weighted Proportion

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-expint 
BuildRequires:    R-CRAN-GenEst 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-invgamma 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-expint 
Requires:         R-CRAN-GenEst 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-invgamma 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-VGAM 

%description
Fit a Poisson regression to carcass distance data and integrate over the
searched area at a wind farm to estimate the fraction of carcasses falling
in the searched area and format the output for use as the dwp parameter in
the 'GenEst' or 'eoa' package for estimating bird and bat mortality,
following Dalthorp, et al. (2022) <arXiv:2201.10064>.

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
