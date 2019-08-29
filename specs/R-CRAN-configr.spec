%global packname  configr
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          An Implementation of Parsing and Writing Configuration File(JSON/INI/YAML/TOML)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.3
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.2
BuildRequires:    R-CRAN-ini >= 0.2
BuildRequires:    R-CRAN-RcppTOML >= 0.1.3
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-yaml >= 2.1.3
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-jsonlite >= 1.2
Requires:         R-CRAN-ini >= 0.2
Requires:         R-CRAN-RcppTOML >= 0.1.3
Requires:         R-utils 
Requires:         R-CRAN-glue 

%description
Implements the JSON, INI, YAML and TOML parser for R setting and writing
of configuration file. The functionality of this package is similar to
that of package 'config'.

%prep
%setup -q -c -n %{packname}
find %{packname}/inst -type f -exec sed -Ei 's@#!( )*/usr/bin/(env )*python@#!/usr/bin/python2@g' {} \;

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
