%global packname  filesstrings
%global packver   3.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.5
Release:          3%{?dist}
Summary:          Handy File and String Manipulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 2.1.0
BuildRequires:    R-CRAN-tibble >= 2.0.1
BuildRequires:    R-CRAN-checkmate >= 1.9.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-ore >= 1.4.0
BuildRequires:    R-CRAN-stringi >= 1.3.1
BuildRequires:    R-CRAN-strex >= 1.1.1
BuildRequires:    R-CRAN-matrixStats >= 0.50.0
BuildRequires:    R-CRAN-rlang >= 0.3.3
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-withr >= 2.1.0
Requires:         R-CRAN-tibble >= 2.0.1
Requires:         R-CRAN-checkmate >= 1.9.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-ore >= 1.4.0
Requires:         R-CRAN-stringi >= 1.3.1
Requires:         R-CRAN-strex >= 1.1.1
Requires:         R-CRAN-matrixStats >= 0.50.0
Requires:         R-CRAN-rlang >= 0.3.3
Requires:         R-CRAN-stringr 

%description
This started out as a package for file and string manipulation. Since
then, the 'fs' and 'strex' packages emerged, offering functionality
previously given by this package (but it's done better in these new ones).
Those packages have hence almost pushed 'filesstrings' into extinction.
However, it still has a small number of unique, handy file manipulation
functions which can be seen in the vignette. One example is a function to
remove spaces from all file names in a directory.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
