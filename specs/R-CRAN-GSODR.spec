%global packname  GSODR
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Global Surface Summary of the Day ('GSOD') Weather Data Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-purrr >= 0.2.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-purrr >= 0.2.0
Requires:         R-CRAN-curl 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Provides automated downloading, parsing, cleaning, unit conversion and
formatting of Global Surface Summary of the Day ('GSOD') weather data from
the from the USA National Centers for Environmental Information ('NCEI')
for use in R.  Units are converted from from United States Customary
System ('USCS') units to International System of Units ('SI'). Stations
may be individually checked for number of missing days defined by the
user, where stations with too many missing observations are omitted. Only
stations with valid reported latitude and longitude values are permitted
in the final data.  Additional useful elements, saturation vapour pressure
('es'), actual vapour pressure ('ea') and relative humidity are calculated
from the original data and included in the final data set.  The resulting
data include station identification information, state, country, latitude,
longitude, elevation, weather observations and associated flags.
Additional data are included with this R package: a list of elevation
values for stations between -60 and 60 degrees latitude derived from the
Shuttle Radar Topography Measuring Mission ('SRTM').  For information on
the 'GSOD' data from 'NCEI', please see the 'GSOD' 'readme.txt' file
available from, <http://www1.ncdc.noaa.gov/pub/data/gsod/readme.txt>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/paper
%doc %{rlibdir}/%{packname}/vector
%{rlibdir}/%{packname}/INDEX
