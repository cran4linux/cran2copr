%global packname  strex
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Extra String Manipulation Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-processx >= 3.3.1
BuildRequires:    R-CRAN-tibble >= 2.0.1
BuildRequires:    R-CRAN-checkmate >= 1.9.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-ore >= 1.4.0
BuildRequires:    R-CRAN-stringi >= 1.3.1
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-matrixStats >= 0.50.0
BuildRequires:    R-CRAN-rlang >= 0.3.3
BuildRequires:    R-stats 
Requires:         R-CRAN-processx >= 3.3.1
Requires:         R-CRAN-tibble >= 2.0.1
Requires:         R-CRAN-checkmate >= 1.9.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-ore >= 1.4.0
Requires:         R-CRAN-stringi >= 1.3.1
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-matrixStats >= 0.50.0
Requires:         R-CRAN-rlang >= 0.3.3
Requires:         R-stats 

%description
There are some things that I wish were easier with the 'stringr' or
'stringi' packages. The foremost of these is the extraction of numbers
from strings. 'stringr' and 'stringi' make you figure out the regular
expression for yourself; 'strex' takes care of this for you. There are
many other handy functionalities in 'strex'. Contributions to this package
are encouraged: it is intended as a miscellany of string manipulation
functions that cannot be found in 'stringi' or 'stringr'.

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
%doc %{rlibdir}/%{packname}/CODE_OF_CONDUCT.md
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
