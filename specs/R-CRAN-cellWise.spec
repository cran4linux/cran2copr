%global packname  cellWise
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Analyzing Data with Cellwise Outliers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.600.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10.14
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-svd 
Requires:         R-CRAN-Rcpp >= 0.12.10.14
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-svd 

%description
Tools for detecting cellwise outliers and robust methods to analyze data
which may contain them. Contains the implementation of the algorithms
described in Rousseeuw and Van den Bossche (2018)
<doi:10.1080/00401706.2017.1340909>, Hubert et al. (2019)
<doi:10.1080/00401706.2018.1562989>, Raymaekers and Rousseeuw (2019)
<doi:10.1080/00401706.2019.1677270>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
