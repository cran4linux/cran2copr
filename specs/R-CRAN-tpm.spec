%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tpm
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          FHWA TPM Score Calculation Functions

License:          Mozilla Public License Version 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.13
BuildRequires:    R-CRAN-fasttime 
Requires:         R-CRAN-data.table >= 1.13
Requires:         R-CRAN-fasttime 

%description
Contains functions for calculating the Federal Highway Administration
(FHWA) Transportation Performance Management (TPM) performance measures.
Currently, the package provides methods for the System Reliability and
Freight (PM3) performance measures calculated from travel time data
provided by The National Performance Management Research Data Set
(NPMRDS), including Level of Travel Time Reliability (LOTTR), Truck Travel
Time Reliability (TTTR), and Peak Hour Excessive Delay (PHED) metric
scores for calculating statewide reliability performance measures.
Implements <https://www.fhwa.dot.gov/tpm/guidance/pm3_hpms.pdf>.

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
