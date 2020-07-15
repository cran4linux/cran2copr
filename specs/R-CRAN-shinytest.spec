%global packname  shinytest
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}
Summary:          Test Shiny Apps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 2.0.3
BuildRequires:    R-CRAN-shiny >= 1.3.2
BuildRequires:    R-CRAN-webdriver >= 1.0.5
BuildRequires:    R-CRAN-testthat >= 1.0.0
BuildRequires:    R-CRAN-rstudioapi >= 0.8.9002
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-debugme 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-pingr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rematch 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-httpuv 
Requires:         R-CRAN-callr >= 2.0.3
Requires:         R-CRAN-shiny >= 1.3.2
Requires:         R-CRAN-webdriver >= 1.0.5
Requires:         R-CRAN-testthat >= 1.0.0
Requires:         R-CRAN-rstudioapi >= 0.8.9002
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-debugme 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-pingr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rematch 
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-httpuv 

%description
For automated testing of Shiny applications, using a headless browser,
driven through 'WebDriver'.

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
%doc %{rlibdir}/%{packname}/diffviewerapp
%{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/recorder
%{rlibdir}/%{packname}/INDEX
