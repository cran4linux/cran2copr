%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dynConfiR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Models for Confidence and Response Time Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-minqa 
Requires:         R-parallel 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Provides density functions for the joint distribution of choice, response
time and confidence for discrete confidence judgments as well as functions
for parameter fitting, prediction and simulation for various dynamical
models of decision confidence.  All models are explained in detail by
Hellmann et al.  (2023; Preprint available at <https://osf.io/9jfqr/>,
published version: <doi:10.1037/rev0000411>).  Implemented models are the
dynaViTE model, dynWEV model, the 2DSD model (Pleskac & Busemeyer, 2010,
<doi:10.1037/a0019737>), and various race models.  C++ code for dynWEV and
2DSD is based on the 'rtdists' package by Henrik Singmann.

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
