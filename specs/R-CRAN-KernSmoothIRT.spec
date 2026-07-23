%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KernSmoothIRT
%global packver   6.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Item Response Theory

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-rgl 
Requires:         R-methods 

%description
Fits nonparametric item and option characteristic curves using kernel
smoothing. It allows for optimal selection of the smoothing bandwidth
using cross-validation and a variety of exploratory plotting tools. The
kernel smoothing is based on methods described in Silverman, B.W. (1986).
Density Estimation for Statistics and Data Analysis. Chapman & Hall,
London.

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
