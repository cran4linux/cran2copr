%global packname  haven
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          3%{?dist}
Summary:          Import and Export 'SPSS', 'Stata' and 'SAS' Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-forcats >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-CRAN-readr >= 0.1.0
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-forcats >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-CRAN-readr >= 0.1.0
Requires:         R-CRAN-hms 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
Import foreign statistical formats into R via the embedded 'ReadStat' C
library, <https://github.com/WizardMac/ReadStat>.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
