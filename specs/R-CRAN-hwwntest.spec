%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hwwntest
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tests of White Noise using Wavelets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-wavethresh 
Requires:         R-parallel 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-wavethresh 

%description
Provides methods to test whether time series is consistent with white
noise. Two new tests based on Haar wavelets and general wavelets described
by Nason and Savchev (2014) <doi:10.1002/sta4.69> are provided and, for
comparison purposes this package also implements the B test of Bartlett
(1967) <doi:10.2307/2333850>. Functionality is provided to compute an
approximation to the theoretical power of the general wavelet test in the
case of general ARMA alternatives.

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
