%global packname  wdpar
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Interface to the World Database on Protected Areas

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 3.2
BuildRequires:    R-CRAN-RSelenium >= 1.7.4
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-progress >= 1.2.0
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-countrycode >= 1.1.0
BuildRequires:    R-CRAN-cli >= 1.0.1
BuildRequires:    R-CRAN-sf >= 0.7.1
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-CRAN-wdman >= 0.2.4
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-lwgeom >= 0.1.4
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-curl >= 3.2
Requires:         R-CRAN-RSelenium >= 1.7.4
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-progress >= 1.2.0
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-countrycode >= 1.1.0
Requires:         R-CRAN-cli >= 1.0.1
Requires:         R-CRAN-sf >= 0.7.1
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-wdman >= 0.2.4
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-lwgeom >= 0.1.4
Requires:         R-utils 
Requires:         R-CRAN-sp 

%description
Fetch and clean data from the World Database on Protected Areas (WDPA).
Data is obtained from Protected Planet <http://protectedplanet.net>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
