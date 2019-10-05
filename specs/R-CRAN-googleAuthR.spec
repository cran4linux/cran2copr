%global packname  googleAuthR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Authenticate and Create Google APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-memoise >= 1.1.0
BuildRequires:    R-CRAN-gargle >= 0.3.1
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-memoise >= 1.1.0
Requires:         R-CRAN-gargle >= 0.3.1
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-digest 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

%description
Create R functions that interact with OAuth2 Google APIs
<https://developers.google.com/apis-explorer/> easily, with auto-refresh
and Shiny compatibility.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/css
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/googledrive_shiny_demo
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/js_auth_demo
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/server_side_auth_demo
%doc %{rlibdir}/%{packname}/server_side_auth_function
%doc %{rlibdir}/%{packname}/signin_demo
%{rlibdir}/%{packname}/INDEX
