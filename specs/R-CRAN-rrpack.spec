%global packname  rrpack
%global packver   0.1-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}
Summary:          Reduced-Rank Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lassoshooting 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lassoshooting 
Requires:         R-MASS 

%description
Multivariate regression methodologies including reduced-rank regression
(RRR) proposed by Chen et al. (2013) <doi:10.1093/biomet/ast036>,
reduced-rank ridge regression (RRS) proposed by Mukherjee and Zhu (2011)
<doi:10.1002/sam.10138>, robust reduced-rank regression (R4) proposed by
She and Chen (2017) <doi:10.1093/biomet/asx032>,
generalized/mixed-response reduced-rank regression (mRRR) proposed by Luo
et al. (2018) <doi:10.1016/j.jmva.2018.04.011>, row-sparse reduced-rank
regression (SRRR) proposed by Chen and Huang (2012)
<doi:10.1080/01621459.2012.734178>, reduced-rank regression with a sparse
singular value decomposition (RSSVD) proposed by Chen et al. (2012)
<doi:10.1111/j.1467-9868.2011.01002.x> and sparse and orthogonal factor
regression (SOFAR) proposed by Uematsu et al. (2019)
<doi:10.1109/TIT.2019.2909889>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
