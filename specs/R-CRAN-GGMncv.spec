%global packname  GGMncv
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Graphical Models with Nonconvex Regularization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-MASS >= 7.3.51.5
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-CRAN-mathjaxr >= 1.0.1
BuildRequires:    R-CRAN-glassoFast >= 1.0
BuildRequires:    R-CRAN-Rdpack >= 0.11
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS >= 7.3.51.5
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-numDeriv >= 2016.8.1.1
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-CRAN-mathjaxr >= 1.0.1
Requires:         R-CRAN-glassoFast >= 1.0
Requires:         R-CRAN-Rdpack >= 0.11
Requires:         R-CRAN-reshape 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimate Gaussian graphical models with nonconvex penalties
<doi:10.31234/osf.io/ad57p>, including the atan Wang and Zhu (2016)
<doi:10.1155/2016/6495417>, seamless L0 Dicker, Huang, and Lin (2013)
<doi:10.5705/ss.2011.074>, exponential Wang, Fan, and Zhu
<doi:10.1007/s10463-016-0588-3>, smooth integration of counting and
absolute deviation Lv and Fan (2009) <doi:10.1214/09-AOS683>, logarithm
Mazumder, Friedman, and Hastie (2011) <doi:10.1198/jasa.2011.tm09738>, Lq,
smoothly clipped absolute deviation Fan and Li (2001)
<doi:10.1198/016214501753382273>, and minimax concave penalty Zhang (2010)
<doi:10.1214/09-AOS729>. There are also extensions for computing variable
inclusion probabilities, multiple regression coefficients, and statistical
inference <doi:10.1214/15-EJS1031>.

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
