%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BTtest
%global packver   0.10.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate the Number of Factors in Large Nonstationary Datasets

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 

%description
Large panel data sets are often subject to common trends. However, it can
be difficult to determine the exact number of these common factors and
analyse their properties. The package implements the Barigozzi and Trapani
(2022) <doi:10.1080/07350015.2021.1901719> test, which not only provides
an efficient way of estimating the number of common factors in large
nonstationary panel data sets, but also gives further insights on factor
classes. The routine identifies the existence of (i) a factor subject to a
linear trend, (ii) the number of zero-mean I(1) and (iii) zero-mean I(0)
factors. Furthermore, the package includes the Integrated Panel Criteria
by Bai (2004) <doi:10.1016/j.jeconom.2003.10.022> that provide a
complementary measure for the number of factors.

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
