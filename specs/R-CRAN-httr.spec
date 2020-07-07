%global packname  httr
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}
Summary:          Tools for Working with URLs and HTTP

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 3.0.0
BuildRequires:    R-CRAN-openssl >= 0.8
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-curl >= 3.0.0
Requires:         R-CRAN-openssl >= 0.8
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-R6 

%description
Useful tools for working with HTTP organised by HTTP verbs (GET(), POST(),
etc). Configuration functions make it easy to control additional request
components (authenticate(), add_headers() and so on).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
