%global packname  detrendr
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}
Summary:          Detrend Images

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-RcppParallel >= 4.4.3
BuildRequires:    R-CRAN-filesstrings >= 3.1.5
BuildRequires:    R-CRAN-withr >= 2.1.0
BuildRequires:    R-CRAN-ijtiff >= 2.0.2
BuildRequires:    R-CRAN-checkmate >= 1.9.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-autothresholdr >= 1.3.3
BuildRequires:    R-CRAN-stringi >= 1.3.1
BuildRequires:    R-CRAN-fs >= 1.3.1
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-rlang >= 0.3.3
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sigmoid 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-RcppParallel >= 4.4.3
Requires:         R-CRAN-filesstrings >= 3.1.5
Requires:         R-CRAN-withr >= 2.1.0
Requires:         R-CRAN-ijtiff >= 2.0.2
Requires:         R-CRAN-checkmate >= 1.9.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-autothresholdr >= 1.3.3
Requires:         R-CRAN-stringi >= 1.3.1
Requires:         R-CRAN-fs >= 1.3.1
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-rlang >= 0.3.3
Requires:         R-parallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sigmoid 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-assertthat 

%description
Detrend fluorescence microscopy image series for fluorescence fluctuation
and correlation spectroscopy ('FCS' and 'FFS') analysis. This package
contains functionality published in a 2016 paper
<doi:10.1093/bioinformatics/btx434> but it has been extended since then
with the Robin Hood algorithm and thus contains unpublished work.

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
