%global packname  exampletestr
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Help for Writing Unit Tests Based on Function Examples

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-filesstrings >= 3.1.5
BuildRequires:    R-CRAN-withr >= 2.1.0
BuildRequires:    R-CRAN-checkmate >= 1.9.3
BuildRequires:    R-CRAN-usethis >= 1.5.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-ore >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-fs >= 1.2.3
BuildRequires:    R-CRAN-styler >= 1.2.0
BuildRequires:    R-CRAN-clipr >= 0.7.0
BuildRequires:    R-CRAN-rstudioapi >= 0.4
BuildRequires:    R-CRAN-rlang >= 0.3.3
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-roxygen2 
Requires:         R-CRAN-filesstrings >= 3.1.5
Requires:         R-CRAN-withr >= 2.1.0
Requires:         R-CRAN-checkmate >= 1.9.3
Requires:         R-CRAN-usethis >= 1.5.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-ore >= 1.4.0
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-fs >= 1.2.3
Requires:         R-CRAN-styler >= 1.2.0
Requires:         R-CRAN-clipr >= 0.7.0
Requires:         R-CRAN-rstudioapi >= 0.4
Requires:         R-CRAN-rlang >= 0.3.3
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-roxygen2 

%description
Take the examples written in your documentation of functions and use them
to create shells (skeletons which must be manually completed by the user)
of test files to be tested with the 'testthat' package. Sort of like
python 'doctests' for R.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/CODE_OF_CONDUCT.md
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
