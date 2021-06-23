%global __brp_check_rpaths %{nil}
%global packname  OpenML
%global packver   1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10
Release:          3%{?dist}%{?buildtag}
Summary:          Open Machine Learning and Open Data Platform

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.1
BuildRequires:    R-CRAN-checkmate >= 1.8.2
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-BBmisc >= 1.11
BuildRequires:    R-CRAN-backports >= 1.1.0
BuildRequires:    R-CRAN-memoise >= 1.0.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
Requires:         R-CRAN-curl >= 4.1
Requires:         R-CRAN-checkmate >= 1.8.2
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-BBmisc >= 1.11
Requires:         R-CRAN-backports >= 1.1.0
Requires:         R-CRAN-memoise >= 1.0.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 

%description
We provide an R interface to 'OpenML.org' which is an online machine
learning platform where researchers can access open data, download and
upload data sets, share their machine learning tasks and experiments and
organize them online to work and collaborate with other researchers. The R
interface allows to query for data sets with specific properties, and
allows the downloading and uploading of data sets, tasks, flows and runs.
See <https://www.openml.org/guide/api> for more information.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
