%global __brp_check_rpaths %{nil}
%global packname  AgroTech
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Analysis of Pesticide Application Technology

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-ggrepel 
Requires:         R-stats 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-crayon 
Requires:         R-utils 

%description
In total it has 7 functions, three for calculating machine calibration,
which determine application rate (L/ha), nozzle flow (L/min) and amount of
product (L or kg) to be added. to the tank with each sprayer filling. Two
functions for graphs of the flow distribution of the nozzles (L/min) in
the application bar and, of the temporal variability of the meteorological
conditions (air temperature, relative humidity of the air and wind speed).
Two functions to determine the spray deposit (uL/cm2), through the
methodology called spectrophotometry, with the aid of bright blue
(Palladini, L.A., Raetano, C.G., Velini, E.D. (2005),
<doi:10.1590/S0103-90162005000500005>) or metallic markers (Chaim, A.,
Castro, V.L.S.S., Correles, F.M., Galvão, J.A.H., Cabral, O.M.R.,
Nicolella, G. (1999), <doi:10.1590/S0100-204X1999000500003>). The package
supports the analysis and representation of information, using a single
free software that meets the most diverse areas of activity in application
technology.

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
