%global packname  huxtable
%global packver   4.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.6.1
Release:          1%{?dist}
Summary:          Easily Create and Style Tables for LaTeX, HTML and Other Formats

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
Like 'xtable', creates styled tables. Export to HTML, LaTeX, 'Word',
'Excel', 'PowerPoint' and RTF. Simple, modern interface to manipulate
borders, size, position, captions, colours, text styles and number
formatting. Table cells can span multiple rows and/or columns. Includes a
'huxreg' function for creation of regression tables, and 'quick_*'
one-liners to print data to a new document.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
