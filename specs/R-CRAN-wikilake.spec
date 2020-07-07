%global packname  wikilake
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}
Summary:          Scrape Lake Metadata Tables from Wikipedia

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-WikipediR 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-selectr 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-WikipediR 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-sp 
Requires:         R-graphics 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-selectr 
Requires:         R-CRAN-units 

%description
Scrape lake metadata tables from Wikipedia <http://www.wikipedia.org>.

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
