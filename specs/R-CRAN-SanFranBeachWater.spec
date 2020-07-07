%global packname  SanFranBeachWater
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Downloads and Tidies the San Francisco Public UtilitiesCommission Beach Water Quality Monitoring Program Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.3.3
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-readr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.3.3
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-readr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-rvest >= 0.3.2

%description
Downloads and tidies the San Francisco Public Utilities Commission Beach
Water Quality Monitoring Program data. Data sets can be downloaded per
beach, or the raw data can be downloaded. See
<https://sfwater.org/cfapps/lims/beachmain1.cfm>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
