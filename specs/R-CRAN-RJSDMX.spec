%global packname  RJSDMX
%global packver   2.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.3
Release:          3%{?dist}
Summary:          R Interface to SDMX Web Services

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.6.4
BuildRequires:    R-CRAN-rJava >= 0.8.8
Requires:         R-CRAN-zoo >= 1.6.4
Requires:         R-CRAN-rJava >= 0.8.8

%description
Provides functions to retrieve data and metadata from providers that
disseminate data by means of SDMX web services. SDMX (Statistical Data and
Metadata eXchange) is a standard that has been developed with the aim of
simplifying the exchange of statistical information. More about the SDMX
standard and the SDMX Web Services can be found at: <https://sdmx.org>.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/configuration.properties
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/Licence.pdf
%{rlibdir}/%{packname}/INDEX
