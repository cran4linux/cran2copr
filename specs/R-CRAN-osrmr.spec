%global packname  osrmr
%global packver   0.1.35
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.35
Release:          3%{?dist}%{?buildtag}
Summary:          Wrapper for the 'OSRM' API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-stringr 

%description
Wrapper around the 'Open Source Routing Machine (OSRM)' API
<http://project-osrm.org/>. 'osrmr' works with API versions 4 and 5 and
can handle servers that run locally as well as the 'OSRM' webserver.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
