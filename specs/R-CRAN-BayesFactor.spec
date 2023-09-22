%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesFactor
%global packver   0.9.12-4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.12.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Bayes Factors for Common Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Matrix >= 1.1.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.2.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MatrixModels 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-hypergeo 
Requires:         R-CRAN-Matrix >= 1.1.1
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-coda 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-MatrixModels 
Requires:         R-methods 
Requires:         R-CRAN-hypergeo 

%description
A suite of functions for computing various Bayes factors for simple
designs, including contingency tables, one- and two-sample designs,
one-way designs, general ANOVA designs, and linear regression.

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
