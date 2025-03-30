%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SPREDA
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Package for Reliability Data Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nlme 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nlme 

%description
The Statistical Package for REliability Data Analysis (SPREDA) implements
recently-developed statistical methods for the analysis of reliability
data. Modern technological developments, such as sensors and smart chips,
allow us to dynamically track product/system usage as well as other
environmental variables, such as temperature and humidity. We refer to
these variables as dynamic covariates. The package contains functions for
the analysis of time-to-event data with dynamic covariates and degradation
data with dynamic covariates. The package also contains functions that can
be used for analyzing time-to-event data with right censoring, and with
left truncation and right censoring. Financial support from NSF and DuPont
are acknowledged.

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
