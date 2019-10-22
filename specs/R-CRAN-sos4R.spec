%global packname  sos4R
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Client for OGC Sensor Observation Services

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.2.2
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-xml2 >= 1.2.2
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringr 

%description
A client for Sensor Observation Services (SOS, see
<https://www.opengeospatial.org/standards/sos>) as specified by the Open
Geospatial Consortium (OGC). With the package users can retrieve
(meta)data from SOS instances and interactively create requests for near
real-time observation data based on the available sensors, phenomena,
observations etc. using thematic, temporal, and spatial filtering.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/sos4r_cheat-sheet.pdf
%{rlibdir}/%{packname}/INDEX
