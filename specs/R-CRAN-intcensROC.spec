%global packname  intcensROC
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Fast Spline Function Based Constrained Maximum LikelihoodEstimator for AUC Estimation of Interval Censored Survival Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-pracma 

%description
The kernel of this 'Rcpp' based package is an efficient implementation of
the generalized gradient projection method for spline function based
constrained maximum likelihood estimator for interval censored survival
data (Wu, Yuan; Zhang, Ying. Partially monotone tensor spline estimation
of the joint distribution function with bivariate current status data.
Ann. Statist. 40, 2012, 1609-1636 <doi:10.1214/12-AOS1016>). The key
function computes the density function of the joint distribution of event
time and the marker and returns the receiver operating characteristic
(ROC) curve for the interval censored survival data as well as area under
the curve (AUC).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
