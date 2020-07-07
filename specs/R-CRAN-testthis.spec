%global packname  testthis
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Utils and 'RStudio' Addins to Make Testing Even More Fun

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-usethis >= 0.1.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-usethis >= 0.1.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-rprojroot 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-testthat 
Requires:         R-tools 
Requires:         R-utils 

%description
Utility functions and 'RStudio' addins for writing, running and organizing
automated tests. Integrates tightly with the packages 'testthat',
'devtools' and 'usethis'.  Hotkeys can be assigned to the 'RStudio' addins
for running tests in a single file or to switch between a source file and
the associated test file. In addition, testthis provides function to
manage and run tests in subdirectories of the test/testthat directory.

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
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
