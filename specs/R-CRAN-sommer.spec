%global packname  sommer
%global packver   4.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.0
Release:          3%{?dist}
Summary:          Solving Mixed Model Equations in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-Matrix >= 1.1.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-Matrix >= 1.1.1
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-lattice 
Requires:         R-CRAN-crayon 

%description
Structural multivariate-univariate linear mixed model solver for
estimation of multiple random effects and unknown variance-covariance
structures (i.e. heterogeneous and unstructured variance models)
(Covarrubias-Pazaran, 2016 <doi:10.1371/journal.pone.0156744>; Maier et
al., 2015 <doi:10.1016/j.ajhg.2014.12.006>). ML/REML estimates can be
obtained using the Direct-Inversion Newton-Raphson and Direct-Inversion
Average Information algorithms. Designed for genomic prediction and genome
wide association studies (GWAS), particularly focused in the p > n problem
(more coefficients than observations) and dense known covariance
structures for levels of random effects. Spatial models can also be fitted
using i.e. the two-dimensional spline functionality available in sommer.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
