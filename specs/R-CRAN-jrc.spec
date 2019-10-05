%global packname  jrc
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Exchange Commands Between R and 'JavaScript'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 

%description
An 'httpuv' based bridge between R and 'JavaScript'. Provides an easy way
to exchange commands and data between a web page and a currently running R
session.

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
%doc %{rlibdir}/%{packname}/http_root
%{rlibdir}/%{packname}/INDEX
