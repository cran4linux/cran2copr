%global packname  rapbase
%global packver   1.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Base Functions and Resources for Rapporteket

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-gistr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-RJDBC 
BuildRequires:    R-CRAN-RMariaDB 
BuildRequires:    R-CRAN-sendmailR 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-gistr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-RJDBC 
Requires:         R-CRAN-RMariaDB 
Requires:         R-CRAN-sendmailR 
Requires:         R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
Provide common functions and resources for registry specific R-packages at
Rapporteket
<https://rapporteket.github.io/rapporteket/articles/short_introduction.html>.
This package is relevant for developers of packages/registries at
Rapporteket.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ansvarsforhold.tex
%doc %{rlibdir}/%{packname}/autoReport.yml
%doc %{rlibdir}/%{packname}/autoReportStandardEmailText.txt
%doc %{rlibdir}/%{packname}/dbConfig.yml
%doc %{rlibdir}/%{packname}/nowebChildAddAnnotation.Rnw
%doc %{rlibdir}/%{packname}/rapbaseConfig.yml
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
