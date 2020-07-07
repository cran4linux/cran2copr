%global packname  shinyEventLogger
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Logging Events in Shiny Apps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mongolite 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-bupaR 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mongolite 
Requires:         R-CRAN-R.utils 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-bupaR 

%description
Logging framework dedicated for complex shiny apps. Different types of
events can be logged (value of a variable, multi-line output of a
function, result of a unit test, custom error, warning, or diagnostic
message). Each event can be logged with a list of parameters that are
event-specific, common for events within the same scope, session-specific,
or app-wide. Logging can be done simultaneously to R console, browser
JavaScript console, a file log, and a database (MongoDB). Log data can be
further analyzed with the help of process-mining techniques from 'bupaR'
package.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
