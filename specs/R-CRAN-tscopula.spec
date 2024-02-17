%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tscopula
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Copula Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-FKF 
BuildRequires:    R-CRAN-ltsa 
BuildRequires:    R-CRAN-rvinecopulib 
BuildRequires:    R-CRAN-arfima 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-kdensity 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats4 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-FKF 
Requires:         R-CRAN-ltsa 
Requires:         R-CRAN-rvinecopulib 
Requires:         R-CRAN-arfima 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-kdensity 

%description
Functions for the analysis of time series using copula models. The package
is based on methodology described in the following references. McNeil,
A.J. (2021) <doi:10.3390/risks9010014>, Bladt, M., & McNeil, A.J. (2021)
<doi:10.1016/j.ecosta.2021.07.004>, Bladt, M., & McNeil, A.J. (2022)
<doi:10.1515/demo-2022-0105>.

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
