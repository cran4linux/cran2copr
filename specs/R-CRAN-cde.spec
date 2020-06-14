%global packname  cde
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          2%{?dist}
Summary:          Download Data from the Catchment Data Explorer Website

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-viridisLite 

%description
Facilitates searching, download and plotting of Water Framework Directive
(WFD) reporting data for all waterbodies within the UK Environment Agency
area. The types of data that can be downloaded are: WFD status
classification data, Reasons for Not Achieving Good (RNAG) status,
objectives set for waterbodies, measures put in place to improve water
quality and details of associated protected areas. The site accessed is
<https://environment.data.gov.uk/catchment-planning/>. The data are made
available under the Open Government Licence v3.0
<https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/>.
This package has been peer-reviewed by rOpenSci (v. 0.4.0).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
