%global packname  lintr
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          2%{?dist}
Summary:          A 'Linter' for R Code

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 2.2.1
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-xmlparsedata >= 1.0.3
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-rstudioapi >= 0.2
BuildRequires:    R-CRAN-rex 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-codetools 
BuildRequires:    R-CRAN-cyclocomp 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-testthat >= 2.2.1
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-xmlparsedata >= 1.0.3
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-rstudioapi >= 0.2
Requires:         R-CRAN-rex 
Requires:         R-CRAN-crayon 
Requires:         R-codetools 
Requires:         R-CRAN-cyclocomp 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-stats 
Requires:         R-utils 

%description
Checks adherence to a given style, syntax errors and possible semantic
issues.  Supports on the fly checking of R code edited with 'RStudio IDE',
'Emacs', 'Vim', 'Sublime Text' and 'Atom'.

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
%doc %{rlibdir}/%{packname}/example
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/syntastic
%{rlibdir}/%{packname}/INDEX
