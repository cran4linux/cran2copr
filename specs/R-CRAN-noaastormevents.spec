%global packname  noaastormevents
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Explore NOAA Storm Events Database

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.1.18
BuildRequires:    R-CRAN-choroplethr >= 3.6.3
BuildRequires:    R-CRAN-maps >= 3.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-choroplethrMaps >= 1.0.1
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-htmltab >= 0.7.1
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-forcats >= 0.4.0
BuildRequires:    R-CRAN-rlang >= 0.3.3
BuildRequires:    R-CRAN-hurricaneexposure >= 0.1.0
Requires:         R-CRAN-XML >= 3.98.1.18
Requires:         R-CRAN-choroplethr >= 3.6.3
Requires:         R-CRAN-maps >= 3.3.0
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-choroplethrMaps >= 1.0.1
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-htmltab >= 0.7.1
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-CRAN-forcats >= 0.4.0
Requires:         R-CRAN-rlang >= 0.3.3
Requires:         R-CRAN-hurricaneexposure >= 0.1.0

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


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
