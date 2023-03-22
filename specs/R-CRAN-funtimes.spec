%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  funtimes
%global packver   9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Time Series Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-mlVAR 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-vars 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-mlVAR 
Requires:         R-parallel 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-vars 

%description
Nonparametric estimators and tests for time series analysis. The functions
use bootstrap techniques and robust nonparametric difference-based
estimators to test for the presence of possibly non-monotonic trends and
for synchronicity of trends in multiple time series.

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
