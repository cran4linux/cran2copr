%global packname  citr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          'RStudio' Add-in to Insert Markdown Citations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.0.0
BuildRequires:    R-CRAN-yaml >= 2.1.13
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-curl >= 1.1
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-rstudioapi >= 0.6
BuildRequires:    R-CRAN-RefManageR >= 0.14.2
BuildRequires:    R-CRAN-shiny >= 0.13.2
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-CRAN-assertthat >= 0.1
Requires:         R-methods >= 3.0.0
Requires:         R-CRAN-yaml >= 2.1.13
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-curl >= 1.1
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-rstudioapi >= 0.6
Requires:         R-CRAN-RefManageR >= 0.14.2
Requires:         R-CRAN-shiny >= 0.13.2
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-assertthat >= 0.1

%description
Functions and an 'RStudio' add-in that search 'Bib(La)TeX'-files or
'Zotero' libraries (via the 'Better BibTeX' plugin) to insert formatted
Markdown citations into the current document.

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
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
