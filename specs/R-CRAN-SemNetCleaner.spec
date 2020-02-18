%global packname  SemNetCleaner
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          An Automated Cleaning Tool for Semantic and Linguistic Data

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SemNetDictionaries >= 0.1.5
BuildRequires:    R-CRAN-hunspell 
BuildRequires:    R-CRAN-searcher 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-tcltk 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-htmlTable 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-SemNetDictionaries >= 0.1.5
Requires:         R-CRAN-hunspell 
Requires:         R-CRAN-searcher 
Requires:         R-CRAN-stringdist 
Requires:         R-tcltk 
Requires:         R-foreign 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-htmlTable 
Requires:         R-CRAN-stringi 

%description
Implements several functions that automates the cleaning and
spell-checking of text data. Also converges, finalizes, removes plurals
and continuous strings, and puts text data in binary format for semantic
network analysis. Uses the 'SemNetDictionaries' package to make the
cleaning process more accurate, efficient, and reproducible.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
