%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AFR
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Toolkit for Regression Analysis of Kazakhstan Banking Sector Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-regclass 
BuildRequires:    R-CRAN-olsrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-mFilter 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-car 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-regclass 
Requires:         R-CRAN-olsrr 
Requires:         R-stats 
Requires:         R-CRAN-lmtest 
Requires:         R-graphics 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-gridExtra 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-mFilter 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-cli 

%description
Tool is created for regression, prediction and forecast analysis of
macroeconomic and credit data. The package includes functions from
existing R packages adapted for banking sector of Kazakhstan. The purpose
of the package is to optimize statistical functions for easier
interpretation for bank analysts and non-statisticians.

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
