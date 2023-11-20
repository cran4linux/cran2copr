%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PowerSDI
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Standardised Drought Indices Using NASA POWER Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lmom 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-nasapower 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-lmom 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-nasapower 
Requires:         R-stats 

%description
A set of functions designed to calculate the standardised precipitation
and standardised precipitation evapotranspiration indices using NASA POWER
data as described in Blain et al. (2023) <doi:10.2139/ssrn.4442843>.
These indices are calculated using a reference data source.  The functions
verify if the indices' estimates meet the assumption of normality and how
well NASA POWER estimates represent real-world data.  Indices are
calculated in a routine mode.  Potential evapotranspiration amounts and
the difference between rainfall and potential evapotranspiration are also
calculated.  The functions adopt a basic time scale that splits each month
into four periods.  Days 1 to 7, days 8 to 14, days 15 to 21, and days 22
to 28, 29, 30, or 31, where 'TS=4' corresponds to a 1-month length moving
window (calculated 4 times per month) and 'TS=48' corresponds to a
12-month length moving window (calculated 4 times per month).

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
