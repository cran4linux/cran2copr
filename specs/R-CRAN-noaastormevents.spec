%global packname  noaastormevents
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Explore NOAA Storm Events Database

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.99.0.3
BuildRequires:    R-CRAN-choroplethr >= 3.7.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-maps >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-RCurl >= 1.98.1.2
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.13.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-tidyr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-choroplethrMaps >= 1.0.1
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-forcats >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-hurricaneexposure >= 0.1.1
Requires:         R-CRAN-XML >= 3.99.0.3
Requires:         R-CRAN-choroplethr >= 3.7.0
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-maps >= 3.3.0
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-RCurl >= 1.98.1.2
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-data.table >= 1.13.0
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-tidyr >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-choroplethrMaps >= 1.0.1
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-CRAN-forcats >= 0.5.0
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-hurricaneexposure >= 0.1.1

%description
Allows users to explore and plot data from the National Oceanic and
Atmospheric Administration (NOAA) Storm Events database through R for
United States counties. Functionality includes matching storm event
listings by time and location to hurricane best tracks data. This work was
supported by grants from the Colorado Water Center, the National Institute
of Environmental Health Sciences (R00ES022631) and the National Science
Foundation (1331399).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
