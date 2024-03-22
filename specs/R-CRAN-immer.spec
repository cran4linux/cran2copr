%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  immer
%global packver   1.5-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.13
Release:          1%{?dist}%{?buildtag}
Summary:          Item Response Models for Multiple Ratings

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-CDM 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-psychotools 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TAM 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CDM 
Requires:         R-CRAN-coda 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-psychotools 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-sirt 
Requires:         R-stats 
Requires:         R-CRAN-TAM 

%description
Implements some item response models for multiple ratings, including the
hierarchical rater model, conditional maximum likelihood estimation of
linear logistic partial credit model and a wrapper function to the
commercial FACETS program. See Robitzsch and Steinfeld (2018) for a
description of the functionality of the package. See Wang, Su and Qiu
(2014; <doi:10.1111/jedm.12045>) for an overview of modeling alternatives.

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
