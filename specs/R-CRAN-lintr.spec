%global packname  lintr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          A 'Linter' for R Code

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi >= 0.2
BuildRequires:    R-CRAN-rex 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-codetools 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rstudioapi >= 0.2
Requires:         R-CRAN-rex 
Requires:         R-CRAN-crayon 
Requires:         R-codetools 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-httr 
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
%doc %{rlibdir}/%{packname}/syntastic
%{rlibdir}/%{packname}/INDEX
