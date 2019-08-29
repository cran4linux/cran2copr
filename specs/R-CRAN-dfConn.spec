%global packname  dfConn
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Dynamic Functional Connectivity Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-doParallel 
Requires:         R-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-gplots 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-graphics 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-gtools 

%description
An implementation of multivariate linear process bootstrap (MLPB) method
and sliding window technique to assess the dynamic functional connectivity
(dFC) estimate by providing its confidence bands, based on Maria Kudela
(2017) <doi: 10.1016/j.neuroimage.2017.01.056>. It also integrates
features to visualize non-zero coverage for selected a-priori regions of
interest estimated by the dynamic functional connectivity model (dFCM) and
dynamic functional connectivity (dFC) curves for reward-related a-priori
regions of interest where the activation-based analysis reported.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
