%global packname  rsconnect
%global packver   0.8.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.16
Release:          3%{?dist}
Summary:          Deployment Interface for R Markdown Documents and ShinyApplications

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.5
BuildRequires:    R-CRAN-rstudioapi >= 0.5
BuildRequires:    R-CRAN-packrat >= 0.4.8.1
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openssl 
Requires:         R-CRAN-yaml >= 2.1.5
Requires:         R-CRAN-rstudioapi >= 0.5
Requires:         R-CRAN-packrat >= 0.4.8.1
Requires:         R-CRAN-curl 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openssl 

%description
Programmatic deployment interface for 'RPubs', 'shinyapps.io', and
'RStudio Connect'. Supported content types include R Markdown documents,
Shiny applications, Plumber APIs, plots, and static web content.

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
%doc %{rlibdir}/%{packname}/cert
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/resources
%{rlibdir}/%{packname}/INDEX
