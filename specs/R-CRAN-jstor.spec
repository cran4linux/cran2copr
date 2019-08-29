%global packname  jstor
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}
Summary:          Read Data from JSTOR/DfR

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-readr >= 1.3.0
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-tidyr >= 0.7.2
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-furrr >= 0.1.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-readr >= 1.3.0
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-tidyr >= 0.7.2
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-furrr >= 0.1.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 

%description
Functions and helpers to import metadata, ngrams and full-texts delivered
by Data for Research by JSTOR.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/pkgdown
%{rlibdir}/%{packname}/INDEX
