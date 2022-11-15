%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtfs2emis
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Public Transport Emissions from General Transit Feed Specification (GTFS) Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 0.9.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-gtfs2gps 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-sf >= 0.9.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-gtfs2gps 
Requires:         R-methods 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-units 

%description
A bottom up model to estimate the emission levels of public transport
systems based on General Transit Feed Specification (GTFS) data. The
package requires two main inputs: i) Public transport data in the GTFS
standard format; and ii) Some basic information on fleet characteristics
such as fleet age, technology, fuel and Euro stage. As it stands, the
package estimates several pollutants at high spatial and temporal
resolutions. Pollution levels can be calculated for specific transport
routes, trips, time of the day or for the transport system as a whole. The
output with emission estimates can be extracted in different formats,
supporting analysis on how emission levels vary across space, time and by
fleet characteristics. A full description of the methods used in the
'gtfs2emis' model is presented in Vieira, J. P. B.; Pereira, R. H. M.;
Andrade, P. R. (2022) <doi:10.31219/osf.io/8m2cy>.

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
