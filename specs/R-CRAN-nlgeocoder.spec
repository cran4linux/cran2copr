%global packname  nlgeocoder
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Geocoding for the Netherlands

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-jsonlite 

%description
R interface to the open location server API of 'Publieke Diensten Op de
Kaart' (<http://www.pdok.nl>). It offers geocoding, address suggestions
and lookup of geographical objects. Included is an utility function for
displaying leaflet tiles restricted to the Netherlands.

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
%doc %{rlibdir}/%{packname}/dev_team.png
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/nlgeocoder_gui
%doc %{rlibdir}/%{packname}/suggest
%doc %{rlibdir}/%{packname}/unconf.html
%doc %{rlibdir}/%{packname}/unconf.Rmd
%{rlibdir}/%{packname}/INDEX
