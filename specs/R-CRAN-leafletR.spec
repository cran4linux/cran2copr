%global __brp_check_rpaths %{nil}
%global packname  leafletR
%global packver   0.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Web-Maps Based on the Leaflet JavaScript Library

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-brew 
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-utils 

%description
Display your spatial data on interactive web-maps using the open-source
JavaScript library Leaflet. 'leafletR' provides basic web-mapping
functionality to combine vector data and online map tiles from different
sources. See <http://leafletjs.com> for more information on Leaflet.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/files
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
