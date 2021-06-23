%global __brp_check_rpaths %{nil}
%global packname  emstreeR
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Fast Computing and Plotting Euclidean Minimum Spanning Trees

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-RcppMLPACK 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-BBmisc 

%description
Fast and easily computes an Euclidean Minimum Spanning Tree (EMST) from
data. This package relies on 'RcppMLPACK' to provide an R interface to the
Dual-Tree Boruvka algorithm (March, Ram, Gray, 2010,
<doi:10.1145/1835804.1835882>) implemented in 'mlpack', the C++ Machine
Learning Library (Curtin et. al., 2013). The Dual-Tree Boruvka is
theoretically and empirically the fastest algorithm for computing an EMST.
This package also provides functions and an S3 method for readily plotting
Minimum Spanning Trees (MST) using either the style of the 'base',
'scatterplot3d', or 'ggplot2' libraries.

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
