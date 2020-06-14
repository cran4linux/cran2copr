%global packname  codemetar
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          2%{?dist}
Summary:          Generate 'CodeMeta' Metadata for R Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sessioninfo 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-pingr 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sessioninfo 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-pingr 

%description
The 'Codemeta' Project defines a 'JSON-LD' format for describing software
metadata, as detailed at <https://codemeta.github.io>. This package
provides utilities to generate, parse, and modify 'codemeta.json' files
automatically for R packages, as well as tools and examples for working
with 'codemeta.json' 'JSON-LD' more generally.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/schema
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
