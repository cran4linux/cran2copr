%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dSTEM
%global packver   2.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Testing of Local Extrema for Detection of Change Points

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Simultaneously detect the number and locations of change points in
piecewise linear models under stationary Gaussian noise allowing
autocorrelated random noise. The core idea is to transform the problem of
detecting change points into the detection of local extrema (local maxima
and local minima)through kernel smoothing and differentiation of the data
sequence, see Cheng et al. (2020) <doi:10.1214/20-EJS1751>. A
low-computational and fast algorithm call 'dSTEM' is introduced to detect
change points based on the 'STEM' algorithm in D. Cheng and A. Schwartzman
(2017) <doi:10.1214/16-AOS1458>.

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
