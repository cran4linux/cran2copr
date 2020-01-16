%global packname  rym
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}
Summary:          R Interface to Yandex Metrica API

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Allows work with 'Management API' for load counters, segments, filters,
user permissions and goals list from Yandex Metrica, 'Reporting API'
allows you to get information about the statistics of site visits and
other data without using the web interface, 'Logs API' allows to receive
non-aggregated data and 'Compatible with Google Analytics Core Reporting
API v3' allows receive information about site traffic and other data using
field names from Google Analytics Core API. For more information see
official documents
<https://tech.yandex.ru/metrika/doc/api2/concept/about-docpage/>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/logo
%{rlibdir}/%{packname}/INDEX
