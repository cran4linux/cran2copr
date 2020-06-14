%global packname  autothresholdr
%global packver   1.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          2%{?dist}
Summary:          An R Port of the 'ImageJ' Plugin 'Auto Threshold'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-filesstrings >= 3.1.5
BuildRequires:    R-CRAN-ijtiff >= 2.0.2
BuildRequires:    R-CRAN-checkmate >= 1.9.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-rlang >= 0.3.3
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
Requires:         R-CRAN-filesstrings >= 3.1.5
Requires:         R-CRAN-ijtiff >= 2.0.2
Requires:         R-CRAN-checkmate >= 1.9.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-rlang >= 0.3.3
Requires:         R-CRAN-purrr 
Requires:         R-stats 

%description
Algorithms for automatically finding appropriate thresholds for numerical
data, with special functions for thresholding images. Provides the
'ImageJ' 'Auto Threshold' plugin functionality to R users. See
<http://imagej.net/Auto_Threshold> and Landini et al. (2017)
<DOI:10.1111/jmi.12474>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
