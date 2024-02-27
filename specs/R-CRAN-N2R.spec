%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  N2R
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Scalable Approximate k-Nearest Neighbor Search Methods using 'N2' Library

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RcppSpdlog 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-Matrix 

%description
Implements methods to perform fast approximate K-nearest neighbor search
on input matrix. Algorithm based on the 'N2' implementation of an
approximate nearest neighbor search using hierarchical Navigable Small
World (NSW) graphs. The original algorithm is described in "Efficient and
Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable
Small World Graphs", Y. Malkov and D. Yashunin,
<doi:10.1109/TPAMI.2018.2889473>, <arXiv:1603.09320>.

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
