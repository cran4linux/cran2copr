%global packname  geoparser
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Interface to the Geoparser.io API for Identifying andDisambiguating Places Mentioned in Text

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-digest 

%description
A wrapper for the Geoparser.io API version 0.4.0 (see
<https://geoparser.io/>), which is a web service that identifies places
mentioned in text, disambiguates those places, and returns detailed data
about the places found in the text. Basic, limited API access is free with
paid plans to accommodate larger workloads.

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
%{rlibdir}/%{packname}/INDEX
