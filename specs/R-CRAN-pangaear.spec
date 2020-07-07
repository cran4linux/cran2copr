%global packname  pangaear
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Client for the 'Pangaea' Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-tibble >= 1.1
BuildRequires:    R-CRAN-crul >= 0.4.0
BuildRequires:    R-CRAN-oai >= 0.2.2
BuildRequires:    R-CRAN-hoardr >= 0.2.0
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-tibble >= 1.1
Requires:         R-CRAN-crul >= 0.4.0
Requires:         R-CRAN-oai >= 0.2.2
Requires:         R-CRAN-hoardr >= 0.2.0
Requires:         R-CRAN-png 

%description
Tools to interact with the 'Pangaea' Database (<https://www.pangaea.de>),
including functions for searching for data, fetching 'datasets' by
'dataset' 'ID', and working with the 'Pangaea' 'OAI-PMH' service.

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
