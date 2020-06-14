%global packname  ajv
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Another JSON Schema Validator

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-RJSONIO 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-RJSONIO 

%description
A thin wrapper around the 'ajv' JSON validation package for JavaScript.
See <http://epoberezkin.github.io/ajv/> for details.

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
%doc %{rlibdir}/%{packname}/ajv.js
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/js-yaml.js
%{rlibdir}/%{packname}/INDEX
