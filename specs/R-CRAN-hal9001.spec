%global __brp_check_rpaths %{nil}
%global packname  hal9001
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          The Scalable Highly Adaptive Lasso

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-origami >= 1.0.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-origami >= 1.0.3
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-data.table 

%description
A scalable implementation of the highly adaptive lasso algorithm,
including routines for constructing sparse matrices of basis functions of
the observed data, as well as a custom implementation of Lasso regression
tailored to enhance efficiency when the matrix of predictors is composed
exclusively of indicator functions. For ease of use and increased
flexibility, the Lasso fitting routines invoke code from the 'glmnet'
package by default. The highly adaptive lasso was first formulated and
described by MJ van der Laan (2017) <doi:10.1515/ijb-2015-0097>, with
practical demonstrations of its performance given by Benkeser and van der
Laan (2016) <doi:10.1109/DSAA.2016.93>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
