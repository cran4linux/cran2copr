%global packname  dbplyr
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          A 'dplyr' Back End for Databases

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.2.2
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-glue >= 1.2.0
BuildRequires:    R-CRAN-DBI >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-tidyselect >= 0.2.4
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.2.2
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-glue >= 1.2.0
Requires:         R-CRAN-DBI >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-tidyselect >= 0.2.4
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-methods 
Requires:         R-utils 

%description
A 'dplyr' back end for databases that allows you to work with remote
database tables as if they are in-memory data frames. Basic features works
with any database that has a 'DBI' back end; more advanced features
require 'SQL' translation to be provided by the package author.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
