%global __brp_check_rpaths %{nil}
%global packname  modQR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple-Output Directional Quantile Regression

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve >= 5.6.1
BuildRequires:    R-CRAN-geometry >= 0.3.1
Requires:         R-CRAN-lpSolve >= 5.6.1
Requires:         R-CRAN-geometry >= 0.3.1

%description
Contains basic tools for performing multiple-output quantile regression
and computing regression quantile contours by means of directional
regression quantiles. In the location case, one can thus obtain halfspace
depth contours in two to six dimensions. Hallin, M., Paindaveine, D. and
Šiman, M. (2010) Multivariate quantiles and multiple-output regression
quantiles: from L1 optimization to halfspace depth. Annals of Statistics
38, 635-669 For more references about the method, see Help pages.

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
