%global __brp_check_rpaths %{nil}
%global packname  factset.analyticsapi.engines
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          'FactSet' Engines API Client

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-rlang 

%description
Allow clients to fetch 'analytics' through API for Portfolio
'Analytics'('PA'), Style Performance Risk('SPAR') and 'Vault' products of
'FactSet'. Visit
<https://github.com/factset/analyticsapi-engines-r-sdk/tree/master/Engines>
for more information on the usage of package. Visit
<https://developer.factset.com/> for more information on products.

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
