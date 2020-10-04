%global packname  DIZutils
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Utilities for 'DIZ' R Package Development

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RJDBC 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-config 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RJDBC 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 

%description
Utility functions used for R package development infrastructure inside the
data integration centers ('DIZ') to standardize and facilitate repetitive
tasks such as setting up a database connection or issuing notification
messages and to avoid redundancy.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
