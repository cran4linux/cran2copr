%global packname  climaemet
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Climate AEMET Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggthemes >= 4.2.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-climatol >= 3.1.2
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-gganimate >= 1.0.5
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-ggpubr >= 0.4.0
BuildRequires:    R-CRAN-gtable >= 0.3.0
BuildRequires:    R-CRAN-jpeg >= 0.1.8.1
BuildRequires:    R-methods 
Requires:         R-CRAN-ggthemes >= 4.2.0
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-climatol >= 3.1.2
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-gganimate >= 1.0.5
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-ggpubr >= 0.4.0
Requires:         R-CRAN-gtable >= 0.3.0
Requires:         R-CRAN-jpeg >= 0.1.8.1
Requires:         R-methods 

%description
Tools to download the climatic data of the Spanish Meteorological Agency
(AEMET) directly from R using their API <https://opendata.aemet.es/> and
create scientific graphs (climate charts, trend analysis of climate time
series, temperature and precipitation anomalies maps, warming stripes
graphics, climatograms, etc.).

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
