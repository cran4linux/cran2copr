%global __brp_check_rpaths %{nil}
%global packname  learnr
%global packver   0.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.1
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Tutorials for R

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.14
BuildRequires:    R-CRAN-rmarkdown >= 1.12
BuildRequires:    R-CRAN-shiny >= 1.0
BuildRequires:    R-CRAN-renv >= 0.8.0
BuildRequires:    R-CRAN-htmltools >= 0.3.5
BuildRequires:    R-CRAN-ellipsis >= 0.2.0.1
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-knitr >= 1.14
Requires:         R-CRAN-rmarkdown >= 1.12
Requires:         R-CRAN-shiny >= 1.0
Requires:         R-CRAN-renv >= 0.8.0
Requires:         R-CRAN-htmltools >= 0.3.5
Requires:         R-CRAN-ellipsis >= 0.2.0.1
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-checkmate 

%description
Create interactive tutorials using R Markdown. Use a combination of
narrative, figures, videos, exercises, and quizzes to create self-paced
tutorials for learning about R and R packages.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/lib
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/tutorials
%{rlibdir}/%{packname}/INDEX
