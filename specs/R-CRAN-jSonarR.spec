%global packname  jSonarR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          jSonar Analytics Platform API for R

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.1
Requires:         R-core >= 2.12.1
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 

%description
This package enables users to access MongoDB by running queries and
returning their results in R data frames. Usually, data in MongoDB is only
available in the form of a JSON document. jSonarR uses data processing and
conversion capabilities in the jSonar Analytics Platform and the JSON
Studio Gateway (http://www.jsonstudio.com), to convert it to a tabular
format which is easy to use with existing R packages.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
