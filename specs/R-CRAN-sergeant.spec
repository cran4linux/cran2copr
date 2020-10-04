%global packname  sergeant
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          3%{?dist}%{?buildtag}
Summary:          Tools to Transform and Query Data with Apache Drill

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dbplyr >= 1.3.0
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-bit64 >= 0.9.7
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-DBI >= 0.7
BuildRequires:    R-CRAN-scales >= 0.4.1
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-purrr >= 0.2.2
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-jsonlite >= 1.5.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dbplyr >= 1.3.0
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-bit64 >= 0.9.7
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-DBI >= 0.7
Requires:         R-CRAN-scales >= 0.4.1
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-purrr >= 0.2.2
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-methods 

%description
Apache Drill is a low-latency distributed query engine designed to enable
data exploration and analysis on both relational and non-relational data
stores, scaling to petabytes of data. Methods are provided that enable
working with Apache Drill instances via the REST API, DBI methods and
using 'dplyr'/'dbplyr' idioms. Helper functions are included to facilitate
using official Drill Docker images/containers.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
