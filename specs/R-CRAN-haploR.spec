%global packname  haploR
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}
Summary:          Query 'HaploReg', 'RegulomeDB'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-RUnit 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-RCurl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-RUnit 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-RCurl 

%description
A set of utilities for querying 'HaploReg'
<http://archive.broadinstitute.org/mammals/haploreg/haploreg.php>,
'RegulomeDB' <http://www.regulomedb.org> web-based tools. The package
connects to 'HaploReg', 'RegulomeDB' searches and downloads results,
without opening web pages, directly from R environment. Results are stored
in a data frame that can be directly used in various kinds of downstream
analyses.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
