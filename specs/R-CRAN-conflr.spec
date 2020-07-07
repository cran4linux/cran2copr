%global packname  conflr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Client for 'Confluence' API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-askpass 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-askpass 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 

%description
Provides utilities for working with various 'Confluence' API
<https://docs.atlassian.com/ConfluenceServer/rest/latest/>, including a
functionality to convert an R Markdown document to 'Confluence' format and
upload it to 'Confluence' automatically.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
