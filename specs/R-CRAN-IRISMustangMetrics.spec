%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IRISMustangMetrics
%global packver   2.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.7
Release:          1%{?dist}%{?buildtag}
Summary:          Statistics and Metrics for Seismic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-IRISSeismic >= 1.3.0
BuildRequires:    R-CRAN-seismicRoll >= 1.1.4
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-IRISSeismic >= 1.3.0
Requires:         R-CRAN-seismicRoll >= 1.1.4
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-methods 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-XML 
Requires:         R-stats 
Requires:         R-CRAN-pracma 

%description
Classes and functions for metrics calculation as part of the 'EarthScope
MUSTANG' project. The functionality in this package builds upon the base
classes of the 'IRISSeismic' package. Metrics include basic statistics as
well as higher level 'health' metrics that can help identify problematic
seismometers.

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
