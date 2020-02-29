%global packname  pcadapt
%global packver   4.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.1
Release:          1%{?dist}
Summary:          Fast Principal Component Analysis for Outlier Detection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-bigutilsr >= 0.3
BuildRequires:    R-CRAN-mmapcharr >= 0.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-rmio 
Requires:         R-CRAN-bigutilsr >= 0.3
Requires:         R-CRAN-mmapcharr >= 0.3
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RSpectra 

%description
Methods to detect genetic markers involved in biological adaptation.
'pcadapt' provides statistical tools for outlier detection based on
Principal Component Analysis. Implements the method described in (Luu,
2016) <DOI:10.1111/1755-0998.12592>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
