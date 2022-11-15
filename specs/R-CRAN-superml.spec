%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  superml
%global packver   0.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          Build Machine Learning Models Like Using Python's Scikit-Learn Library in R

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-R6 >= 2.2
BuildRequires:    R-CRAN-data.table >= 1.10
BuildRequires:    R-CRAN-Rcpp >= 1.0
BuildRequires:    R-CRAN-assertthat >= 0.2
BuildRequires:    R-CRAN-Metrics >= 0.1
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-R6 >= 2.2
Requires:         R-CRAN-data.table >= 1.10
Requires:         R-CRAN-Rcpp >= 1.0
Requires:         R-CRAN-assertthat >= 0.2
Requires:         R-CRAN-Metrics >= 0.1

%description
The idea is to provide a standard interface to users who use both R and
Python for building machine learning models. This package provides a
scikit-learn's fit, predict interface to train machine learning models in
R.

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
