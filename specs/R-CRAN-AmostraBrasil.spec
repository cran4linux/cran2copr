%global packname  AmostraBrasil
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Generates Samples or Complete List of Brazilian IBGE (InstitutoBrasileiro De Geografia e Estatistica) Census Households,Geocoding it by Google Maps

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-foreign 
Requires:         R-methods 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-foreign 

%description
Generates samples or complete list of Brazilian IBGE (Instituto Brasileiro
de Geografia e Estatistica, see <http://www.ibge.gov.br/> for more
information) census households, geocoding it by Google Maps. The package
connects IBGE site and downloads maps and census data.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
