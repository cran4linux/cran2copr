%global packname  nhlscrape
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Scrapes the 'NHL' API for Statistical Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-xml2 

%description
Add game events to a database file to use for statistical analysis of
hockey games. This means we only call the 'NHL' API once for each game we
want to add. We will have very fast retrieval of data once games have been
added since the data is stored locally. We use the API located at
<https://statsapi.web.nhl.com/api/v1/teams> with supplemental data from
<https://www.nhl.com/scores/>. Other endpoints can be found at
<https://gitlab.com/dword4/nhlapi>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
