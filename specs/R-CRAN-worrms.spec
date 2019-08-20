%global packname  worrms
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          World Register of Marine Species (WoRMS) Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-crul >= 0.6.0
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-crul >= 0.6.0
Requires:         R-CRAN-data.table 

%description
Client for World Register of Marine Species
(<http://www.marinespecies.org/>). Includes functions for each of the API
methods, including searching for names by name, date and common names,
searching using external identifiers, fetching synonyms, as well as
fetching taxonomic children and taxonomic classification.

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
