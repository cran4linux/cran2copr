%global packname  grattan
%global packver   1.8.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.0.1
Release:          3%{?dist}
Summary:          Australian Tax Policy Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-zoo >= 1.5.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-hutils >= 1.3.0
BuildRequires:    R-CRAN-ineq >= 0.2.10
BuildRequires:    R-CRAN-fy >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rsdmx 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-utils 
Requires:         R-CRAN-zoo >= 1.5.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-hutils >= 1.3.0
Requires:         R-CRAN-ineq >= 0.2.10
Requires:         R-CRAN-fy >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rsdmx 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-forecast 
Requires:         R-utils 

%description
Utilities for costing and evaluating Australian tax policy, including
high-performance tax and transfer calculators, a fast method of projecting
tax collections, and an interface to common indices from the Australian
Bureau of Statistics.  Written to support Grattan Institute's Australian
Perspectives program. For access to the 'taxstats' package, please run
install.packages("taxstats", repos =
"https://hughparsonage.github.io/tax-drat/", type = "source"). N.B. The
'taxstats' package is approximately 50 MB.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
