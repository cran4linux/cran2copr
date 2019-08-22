%global packname  camsRad
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Client for CAMS Radiation Service

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-xml2 >= 1.0.0

%description
Copernicus Atmosphere Monitoring Service (CAMS) radiations service
provides time series of global, direct, and diffuse irradiations on
horizontal surface, and direct irradiation on normal plane for the actual
weather conditions as well as for clear-sky conditions. The geographical
coverage is the field-of-view of the Meteosat satellite, roughly speaking
Europe, Africa, Atlantic Ocean, Middle East. The time coverage of data is
from 2004-02-01 up to 2 days ago. Data are available with a time step
ranging from 15 min to 1 month. For license terms and to create an
account, please see
<http://www.soda-pro.com/web-services/radiation/cams-radiation-service>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
