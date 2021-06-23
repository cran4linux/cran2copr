%global __brp_check_rpaths %{nil}
%global packname  DBItest
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          3%{?dist}%{?buildtag}
Summary:          Testing 'DBI' 'Backends'

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 2.0.0
BuildRequires:    R-CRAN-blob >= 1.2.0
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-hms >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-testthat >= 2.0.0
Requires:         R-CRAN-blob >= 1.2.0
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-hms >= 0.5.0
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-callr 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-withr 

%description
A helper that tests 'DBI' back ends for conformity to the interface.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
