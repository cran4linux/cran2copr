%global packname  vstsr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Access to Visual Studio Team Services API via R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-xml2 

%description
Implementation of Visual Studio Team Services
<https://www.visualstudio.com/team-services/> API calls. It enables the
extraction of information about repositories, build and release
definitions and individual releases. It also helps create repositories and
work items within a project without logging into Visual Studio. There is
the ability to use any API service with a shell for any non-predefined
call.

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
%{rlibdir}/%{packname}/INDEX
