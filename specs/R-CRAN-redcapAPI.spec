%global packname  redcapAPI
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          3%{?dist}
Summary:          Interface to 'REDCap'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-labelVector 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-labelVector 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 

%description
Access data stored in 'REDCap' databases using the Application Programming
Interface (API).  'REDCap' (Research Electronic Data CAPture;
<https://projectredcap.org>) is a web application for building and
managing online surveys and databases developed at Vanderbilt University.
The API allows users to access data and project meta data (such as the
data dictionary) from the web programmatically.  The 'redcapAPI' package
facilitates the process of accessing data with options to prepare an
analysis-ready data set consistent with the definitions in a database's
data dictionary.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
