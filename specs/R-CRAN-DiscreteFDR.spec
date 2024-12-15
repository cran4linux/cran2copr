%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DiscreteFDR
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          FDR Based Multiple Testing Procedures with Adaptation for Discrete Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-DiscreteTests >= 0.2.1
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-DiscreteDatasets 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-DiscreteTests >= 0.2.1
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-DiscreteDatasets 

%description
Implementations of the multiple testing procedures for discrete tests
described in the paper Döhler, Durand and Roquain (2018) "New FDR bounds
for discrete and heterogeneous tests" <doi:10.1214/18-EJS1441>. The main
procedures of the paper (HSU and HSD), their adaptive counterparts (AHSU
and AHSD), and the HBR variant are available and are coded to take as
input the results of a test procedure from package 'DiscreteTests', or a
set of observed p-values and their discrete support under their nulls. A
shortcut function to obtain such p-values and supports is also provided,
along with a wrapper allowing to apply discrete procedures directly to
data.

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
