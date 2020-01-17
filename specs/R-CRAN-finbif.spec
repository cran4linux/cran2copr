%global packname  finbif
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Interface for the 'Finnish Biodiversity Information Facility'API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-lutz 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr 
Requires:         R-graphics 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-lutz 
Requires:         R-methods 
Requires:         R-utils 

%description
A programmatic interface to the 'Finnish Biodiversity Information
Facility' ('FinBIF') API (<https://api.laji.fi>). 'FinBIF' aggregates
Finnish biodiversity data from multiple sources in a single open access
portal for researchers, citizen scientists, industry and government.
'FinBIF' allows users of biodiversity information to find, access, combine
and visualise data on Finnish plants, animals and microorganisms. The
'finbif' package makes the publicly available data in 'FinBIF' easily
accessible to programmers. Biodiversity information is available on
taxonomy and taxon occurrence. Occurrence data can be filtered by taxon,
time, location and other variables. The data accessed are conveniently
preformatted for subsequent analyses.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
