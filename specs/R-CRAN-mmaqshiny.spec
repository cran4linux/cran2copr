%global packname  mmaqshiny
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Explore Air-Quality Mobile-Monitoring Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-plotly 

%description
Mobile-monitoring or "sensors on a mobile platform", is an increasingly
popular approach to measure high-resolution pollution data at the street
level. Coupled with location data, spatial visualisation of air-quality
parameters helps detect localized areas of high air-pollution, also called
hotspots. In this approach, portable sensors are mounted on a vehicle and
driven on predetermined routes to collect high frequency data (1 Hz).
'mmaqshiny' is for analysing, visualising and spatial mapping of
high-resolution air-quality data collected by specific devices installed
on a moving platform. 1 Hz data of PM2.5 (mass concentrations of
particulate matter with size less than 2.5 microns), Black carbon mass
concentrations (BC), ultra-fine particle number concentrations, carbon
dioxide along with GPS coordinates and relative humidity (RH) data
collected by popular portable instruments (TSI DustTrak-8530, Aethlabs
microAeth-AE51, TSI CPC3007, LICOR Li-830, Garmin GPSMAP 64s, Omega USB RH
probe respectively). It incorporates device specific cleaning and
correction algorithms. RH correction is applied to DustTrak PM2.5
following the Chakrabarti et al., (2004)
<doi:10.1016/j.atmosenv.2004.03.007>. Provision is given to add linear
regression coefficients for correcting the PM2.5 data (if required). BC
data will be cleaned for the vibration generated noise, by adopting the
statistical procedure as explained in Apte et al., (2011)
<doi:10.1016/j.atmosenv.2011.05.028>, followed by a loading correction as
suggested by Ban-Weiss et al., (2009) <doi:10.1021/es8021039>. For the
number concentration data, provision is given for dilution correction
factor (if a diluter is used with CPC3007; default value is 1). The
package joins the raw, cleaned and corrected data from the above said
instruments and outputs as a downloadable csv file.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
