%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MKendall
%global packver   1.5-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Matrix Kendall's Tau and Matrix Elliptical Factor Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Large-scale matrix-variate data have been widely observed nowadays in
various research areas such as finance, signal processing and medical
imaging. Modelling matrix-valued data by matrix-elliptical family not only
provides a flexible way to handle heavy-tail property and tail
dependencies, but also maintains the intrinsic row and column structure of
random matrices. We proposed a new tool named matrix Kendall's tau which
is efficient for analyzing random elliptical matrices. By applying this
new type of Kendell’s tau to the matrix elliptical factor model, we
propose a Matrix-type Robust Two-Step (MRTS) method to estimate the
loading and factor spaces. See the details in He at al. (2022)
<arXiv:2207.09633>. In this package, we provide the algorithms for
calculating sample matrix Kendall's tau, the MRTS method and the Matrix
Kendall's tau Eigenvalue-Ratio (MKER) method which is used for determining
the number of factors.

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
