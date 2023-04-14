%global __brp_check_rpaths %{nil}
%global packname  hurricaneexposure
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Explore and Map County-Level Hurricane Exposure in the UnitedStates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-maps >= 3.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-ggmap >= 3.0.0
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-mapproj >= 1.2.6
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-rlang >= 0.4.2
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-lazyeval >= 0.2.2
Requires:         R-CRAN-maps >= 3.3.0
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-ggmap >= 3.0.0
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-mapproj >= 1.2.6
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-rlang >= 0.4.2
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-lazyeval >= 0.2.2

%description
Allows users to create time series of tropical storm exposure histories
for chosen counties for a number of hazard metrics (wind, rain, distance
from the storm, etc.). This package interacts with data available through
the 'hurricaneexposuredata' package, which is available in a 'drat'
repository. To access this data package, see the instructions at
<https://github.com/geanders/hurricaneexposure>. The size of the
'hurricaneexposuredata' package is approximately 20 MB. This work was
supported in part by grants from the National Institute of Environmental
Health Sciences (R00ES022631), the National Science Foundation (1331399),
and a NASA Applied Sciences Program/Public Health Program Grant
(NNX09AV81G).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
