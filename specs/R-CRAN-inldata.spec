%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  inldata
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Datasets for the USGS-INL Monitoring Networks

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-terra 
Requires:         R-tools 
Requires:         R-utils 

%description
A collection of analysis-ready datasets for the U.S. Geological Survey -
Idaho National Laboratory (USGS-INL) groundwater and surface-water
monitoring networks, administered by the USGS-INL Project Office in
cooperation with the U.S. Department of Energy. The data collected from
wells and surface-water stations at the Idaho National Laboratory and
surrounding areas have been used to describe the effects of waste disposal
on water contained in the eastern Snake River Plain aquifer, located in
the southeastern part of Idaho, and the availability of water for
long-term consumptive and industrial use. The package includes long-term
monitoring records dating back to measurements from 1949. Geospatial data
describing the areas from which samples were collected or observations
were made are also included in the package. Bundling this data into a
single package significantly reduces the magnitude of data processing for
researchers and provides a way to distribute the data along with its
documentation in a standard format. Geospatial datasets are made available
in a common projection and datum, and geohydrologic data have been
structured to facilitate analysis.

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
