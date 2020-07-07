%global packname  GSE
%global packver   4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2
Release:          3%{?dist}
Summary:          Robust Estimation in the Presence of Cellwise and CasewiseContamination and Missing Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-cellWise 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.10.0
Requires:         R-MASS 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-cellWise 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 

%description
Robust Estimation of Multivariate Location and Scatter in the Presence of
Cellwise and Casewise Contamination and Missing Data.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
