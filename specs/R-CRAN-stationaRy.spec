%global __brp_check_rpaths %{nil}
%global packname  stationaRy
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Detailed Meteorological Data from Stations All Over the World

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-downloader >= 0.4
BuildRequires:    R-CRAN-lutz >= 0.3.1
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-downloader >= 0.4
Requires:         R-CRAN-lutz >= 0.3.1
Requires:         R-CRAN-magrittr 

%description
Acquire hourly meteorological data from stations located all over the
world. There is a wealth of data available, with historic weather data
accessible from nearly 30,000 stations. The available data is
automatically downloaded from a data repository and processed into a
'tibble' for the exact range of years requested. A relative humidity
approximation is provided using the 'August-Roche-Magnus' formula, which
was adapted from Alduchov and Eskridge (1996)
<doi:10.1175%2F1520-0450%281996%29035%3C0601%3AIMFAOS%3E2.0.CO%3B2>.

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
%doc %{rlibdir}/%{packname}/710633-99999-2013.gz
%doc %{rlibdir}/%{packname}/710633-99999-2014.gz
%doc %{rlibdir}/%{packname}/710633-99999-2015.gz
%doc %{rlibdir}/%{packname}/710633-99999-2016.gz
%{rlibdir}/%{packname}/INDEX
