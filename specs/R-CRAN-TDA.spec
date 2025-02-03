%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TDA
%global packver   1.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for Topological Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-BH >= 1.87.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-CRAN-scales 

%description
Tools for Topological Data Analysis. The package focuses on statistical
analysis of persistent homology and density clustering. For that, this
package provides an R interface for the efficient algorithms of the C++
libraries 'GUDHI' <https://project.inria.fr/gudhi/software/>, 'Dionysus'
<https://www.mrzv.org/software/dionysus/>, and 'PHAT'
<https://bitbucket.org/phat-code/phat/>. This package also implements
methods from Fasy et al. (2014) <doi:10.1214/14-AOS1252> and Chazal et al.
(2015) <doi:10.20382/jocg.v6i2a8> for analyzing the statistical
significance of persistent homology features.

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
