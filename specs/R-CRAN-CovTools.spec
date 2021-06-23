%global __brp_check_rpaths %{nil}
%global packname  CovTools
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Tools for Covariance Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-geigen 
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-SHT 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-geigen 
Requires:         R-CRAN-shapes 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-Rdpack 
Requires:         R-utils 
Requires:         R-CRAN-SHT 

%description
Covariance is of universal prevalence across various disciplines within
statistics. We provide a rich collection of geometric and inferential
tools for convenient analysis of covariance structures, topics including
distance measures, mean covariance estimator, covariance hypothesis test
for one-sample and two-sample cases, and covariance estimation. For an
introduction to covariance in multivariate statistical analysis, see
Schervish (1987) <doi:10.1214/ss/1177013111>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
