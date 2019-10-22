%global packname  nandb
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}
Summary:          Number and Brightness Image Analysis

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-filesstrings >= 3.1.5
BuildRequires:    R-CRAN-withr >= 2.1.0
BuildRequires:    R-CRAN-ijtiff >= 2.0.2
BuildRequires:    R-CRAN-checkmate >= 1.9.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-autothresholdr >= 1.3.3
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-detrendr >= 0.6.2
BuildRequires:    R-CRAN-rlang >= 0.3.3
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-filesstrings >= 3.1.5
Requires:         R-CRAN-withr >= 2.1.0
Requires:         R-CRAN-ijtiff >= 2.0.2
Requires:         R-CRAN-checkmate >= 1.9.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-autothresholdr >= 1.3.3
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-detrendr >= 0.6.2
Requires:         R-CRAN-rlang >= 0.3.3
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reshape2 
Requires:         R-utils 
Requires:         R-CRAN-viridis 

%description
Calculation of molecular number and brightness from fluorescence
microscopy image series. The software was published in a 2016 paper
<doi:10.1093/bioinformatics/btx434>. The seminal paper for the technique
is Digman et al. 2008 <doi:10.1529/biophysj.107.114645>. A review of the
technique was published in 2017 <doi:10.1016/j.ymeth.2017.12.001>.

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
