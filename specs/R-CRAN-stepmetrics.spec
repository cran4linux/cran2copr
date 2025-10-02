%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stepmetrics
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Step and Cadence Metrics from Wearable Data

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PhysicalActivity 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-PhysicalActivity 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides functions to calculate step- and cadence-based metrics from
timestamped accelerometer and wearable device data. Supports CSV and AGD
files from 'ActiGraph' devices, CSV files from 'Fitbit' devices, and step
counts derived with R package 'GGIR' <https://github.com/wadpac/GGIR>,
with automatic handling of epoch lengths from 1 to 60 seconds. Metrics
include total steps, cadence peaks, minutes and steps in predefined
cadence bands, and time and steps in moderate-to-vigorous physical
activity (MVPA). Methods and thresholds are informed by the literature,
e.g., Tudor-Locke and Rowe (2012) <doi:10.2165/11599170-000000000-00000>,
Barreira et al. (2012) <doi:10.1249/MSS.0b013e318254f2a3>, and Tudor-Locke
et al. (2018) <doi:10.1136/bjsports-2017-097628>. The package record is
also available on Zenodo (2023) <doi:10.5281/zenodo.7858094>.

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
