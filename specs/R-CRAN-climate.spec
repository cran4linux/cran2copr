%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  climate
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to Download Meteorological (and Hydrological) Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringi 

%description
Automatize downloading of meteorological and hydrological data from
publicly available repositories: OGIMET
(<http://ogimet.com/index.phtml.en>), University of Wyoming - atmospheric
vertical profiling data (<http://weather.uwyo.edu/upperair/>), Polish
Institute of Meteorology and Water Management - National Research
Institute (<https://danepubliczne.imgw.pl>), and National Oceanic &
Atmospheric Administration (NOAA). This package also allows for searching
geographical coordinates for each observation and calculate distances to
the nearest stations.

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
