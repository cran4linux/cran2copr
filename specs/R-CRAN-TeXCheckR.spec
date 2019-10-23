%global packname  TeXCheckR
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Parses LaTeX Documents for Errors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-hunspell >= 2.5
BuildRequires:    R-CRAN-data.table >= 1.9.0
BuildRequires:    R-CRAN-hutils >= 0.8.0
BuildRequires:    R-CRAN-clisymbols 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-hunspell >= 2.5
Requires:         R-CRAN-data.table >= 1.9.0
Requires:         R-CRAN-hutils >= 0.8.0
Requires:         R-CRAN-clisymbols 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-zoo 

%description
Checks LaTeX documents and .bib files for typing errors, such as spelling
errors, incorrect quotation marks. Also provides useful functions for
parsing and linting bibliography files.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
