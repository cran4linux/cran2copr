%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cpop
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Detection of Multiple Changes in Slope in Univariate Time-Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-crops 
BuildRequires:    R-CRAN-pacman 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-crops 
Requires:         R-CRAN-pacman 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-pracma 
Requires:         R-methods 

%description
Detects multiple changes in slope using the CPOP dynamic programming
approach of Fearnhead, Maidstone, and Letchford (2019)
<doi:10.1080/10618600.2018.1512868>. This method finds the best continuous
piecewise linear fit to data under a criterion that measures fit to data
using the residual sum of squares, but penalizes complexity based on an L0
penalty on changes in slope.

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
