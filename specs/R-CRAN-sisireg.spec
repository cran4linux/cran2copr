%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sisireg
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sign-Simplicity-Regression-Solver

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-reticulate 

%description
Implementation of the SSR-Algorithm. The Sign-Simplicity-Regression model
is a nonparametric statistical model which is based on residual signs and
simplicity assumptions on the regression function. Goal is to calculate
the most parsimonious regression function satisfying the statistical
adequacy requirements. Theory and functions are specified in Metzner
(2020, ISBN: 979-8-68239-420-3, "Trendbasierte Prognostik") and Metzner
(2021, ISBN: 979-8-59347-027-0, "Adäquates Maschinelles Lernen").

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
