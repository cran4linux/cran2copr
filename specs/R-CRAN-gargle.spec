%global packname  gargle
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Utilities for Working with Google APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-fs >= 1.3.1
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-fs >= 1.3.1
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-CRAN-withr 

%description
Provides utilities for working with Google APIs
<https://developers.google.com/apis-explorer>.  This includes functions
and classes for handling common credential types and for preparing,
executing, and processing HTTP requests.

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
%doc %{rlibdir}/%{packname}/discovery-doc-ingest
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/secret
%{rlibdir}/%{packname}/INDEX
