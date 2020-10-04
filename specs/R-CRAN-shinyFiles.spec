%global packname  shinyFiles
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Server-Side File System Viewer for Shiny

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-fs >= 1.2.6
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-tools 
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-fs >= 1.2.6
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-tools 

%description
Provides functionality for client-side navigation of the server side file
system in shiny apps. In case the app is running locally this gives the
user direct access to the file system without the need to "download" files
to a temporary location. Both file and folder selection as well as file
saving is available.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/example
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
