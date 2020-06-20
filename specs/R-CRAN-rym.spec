%global packname  rym
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
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
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-purrr 

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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
