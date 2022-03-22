%global __brp_check_rpaths %{nil}
%global packname  emstreeR
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Fast Computing and Plotting Euclidean Minimum Spanning Trees

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mlpack 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-mlpack 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-BBmisc 
Requires:         R-graphics 
Requires:         R-stats 

%description
Fast and easily computes an Euclidean Minimum Spanning Tree (EMST) from
data, relying on the R API for 'mlpack' - the C++ Machine Learning Library
(Curtin et. al., 2013). 'emstreeR' uses the Dual-Tree Boruvka (March, Ram,
Gray, 2010, <doi:10.1145/1835804.1835882>), which is theoretically and
empirically the fastest algorithm for computing an EMST. This package also
provides functions and an S3 method for readily plotting Minimum Spanning
Trees (MST) using either the style of the 'base', 'scatterplot3d', or
'ggplot2' libraries.

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
