%global packname  auth0
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}
Summary:          Secure Authentication in Shiny with Auth0

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-yaml 
Requires:         R-utils 

%description
Uses Auth0 API (see <https://auth0.com> for more information) to use a
simple and secure authentication system. It provides tools to log in and
out a shiny application using social networks or a list of e-mails.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bookmark
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/logout
%doc %{rlibdir}/%{packname}/simple
%doc %{rlibdir}/%{packname}/ui-server
%doc %{rlibdir}/%{packname}/ui-server-bookmark
%doc %{rlibdir}/%{packname}/ui-server-userinfo
%doc %{rlibdir}/%{packname}/userinfo
%{rlibdir}/%{packname}/INDEX
