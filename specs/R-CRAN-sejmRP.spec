%global packname  sejmRP
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          3%{?dist}%{?buildtag}
Summary:          An Information About Deputies and Votings in Polish Diet fromSeventh to Eighth Term of Office

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-cluster 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xml2 

%description
Set of functions that access information about deputies and votings in
Polish diet from webpage <http://www.sejm.gov.pl>. The package was
developed as a result of an internship in MI2 Group -
<http://mi2.mini.pw.edu.pl>, Faculty of Mathematics and Information
Science, Warsaw University of Technology.

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
%{rlibdir}/%{packname}/INDEX
