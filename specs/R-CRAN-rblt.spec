%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rblt
%global packver   0.2.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bio-Logging Toolbox

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-hdf5r >= 1.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-methods 
BuildRequires:    R-tools 
Requires:         R-CRAN-hdf5r >= 1.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-shiny 
Requires:         R-methods 
Requires:         R-tools 

%description
An R-shiny application to plot datalogger time series at a microsecond
precision as Acceleration, Temperature, Pressure, Light intensity from
CATS, AXY-TREK LUL and WACU bio-loggers. It is possible to link behavioral
labels extracted from 'BORIS' software <http://www.boris.unito.it> or
manually written in a csv file. CATS bio-logger are manufactured by
<https://cats.is/>, AXY-TREK are manufactured by
<https://www.technosmart.eu> and LUL and WACU are manufactured by
<https://www.iphc.cnrs.fr/-MIBE-.html>.

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
