%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ConconiAnaerobicThresholdTest
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conconi Estimate of Anaerobic Threshold from a TCX File

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-trackeR 
BuildRequires:    R-CRAN-SiZer 
BuildRequires:    R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-trackeR 
Requires:         R-CRAN-SiZer 
Requires:         R-methods 

%description
Analyzes data from a Conconi et al. (1996) <doi:10.1055/s-2007-972887>
treadmill fitness test where speed is augmented by a constant amount every
set number of seconds to estimate the anaerobic (lactate) threshold speed
and heart rate. It reads a TCX file, allows optional removal observations
from before and after the actual test, fits a change-point linear model
where the change-point is the estimate of the lactate threshold, and plots
the data points and fit model. Details of administering the fitness test
are provided in the package vignette. Functions work by default for Garmin
Connect TCX exports but may require additional data preparation for heart
rate, time, and speed data from other sources.

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
