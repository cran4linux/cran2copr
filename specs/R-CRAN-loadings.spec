%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  loadings
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Loadings for Principal Component Analysis and Partial Least Squares

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-geigen 
Requires:         R-CRAN-geigen 

%description
Computing statistical hypothesis testing for principal component (PC)
loading (Yamamoto, H. et al. (2014)), orthogonal smoothed PC (OS-PC)
loading (Yamamoto, H. et al. (2021) <doi:10.3390/metabo11030149>),
one-sided kernel PC loading (Yamamoto, H. (2023) <doi:10.51094/jxiv.262>)
, partial least squares (PLS) loading (Yamamoto, H. (2017)
<doi:10.1002/cem.2883>), PLS with rank order of groups (PLS-ROG) loading
(Yamamoto, H. (2017), multiset PLS and PLS-ROG loading (Yamamoto, H.
(2022) <doi:10.1101/2022.08.30.505949>).

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
