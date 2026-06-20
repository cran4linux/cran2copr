%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Time.R
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimates Time of Concentration and Lag Time for Watersheds

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readxl 
Requires:         R-utils 

%description
Estimation of time of concentration and lag times for watersheds based on
their morphometric characteristics. It includes various methods for
calculation and offers plotting functionalities for comparative analysis.
For more details see Bransby-Williams (1922, ISSN 2214-5818), Kirpich
(1940) <https://hess.copernicus.org/articles/24/2655/2020/>, Kerby (1959,
ISBN-13, 979-8355357214), Johnstone & Cross (1949, ISBN:9780823211234),
California Division of Highways (1942, ISSN:0012-7353), Clark (1945)
<doi:10.1061/TACEAT.0005800>, Giandotti (1934)
<doi:10.1080/02626667.2017.1384549>, Passini (1972, ISBN:84-7433-040-8),
Témez (1978, ISBN:84-7433-040-8), Pérez (1962, ISSN:0012-7353), Pilgrim
(1977) <doi:10.1029/WR013i003p00587>, Bureau of Reclamation (1973,
ISBN:9780913232123), Valencia-Zuluaga (1983)
<https://repositorio.unal.edu.co/>, Ventura & Heras (1964)
<doi:10.1061/9780784413548.005>, Soil Conservation Service (1972,
ISBN:OL15009517M), Soil Conservation Service (1986)
<https://www.ars.usda.gov/research/software/download/?softwareid=527>, US
Navy - Technical Publication Navdocks (1972) <ISBN:978-1289256234>,
Federal Aviation Administration (1970, ISBN:9780913236543), Natural
Environment Research Council (1975, ISBN:9780114501234), Mimikou (1984)
<doi:10.1080/02626668409490922>, Watt & Chow (1985) <doi:10.1139/l85-031>,
Haktanir & Sezen (1990) <doi:10.1080/02626669009492423>.

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
