%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  trendseries
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extract Trends from Time Series

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dlm 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-hpfilter 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-mFilter 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tsbox 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dlm 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-hpfilter 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-mFilter 
Requires:         R-CRAN-RcppRoll 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tsbox 

%description
Extract trends from monthly and quarterly economic time series. Provides
two main functions: augment_trends() for pipe-friendly 'tibble' workflows
and extract_trends() for direct time series analysis. Includes key
econometric filters and modern parameter experimentation tools.

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
