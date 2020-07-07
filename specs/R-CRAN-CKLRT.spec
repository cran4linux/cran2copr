%global packname  CKLRT
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}
Summary:          Composite Kernel Machine Regression Based on Likelihood RatioTest

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-mgcv 
BuildRequires:    R-MASS 
BuildRequires:    R-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-mgcv 
Requires:         R-MASS 
Requires:         R-nlme 
Requires:         R-stats 

%description
Composite Kernel Machine Regression based on Likelihood Ratio Test
(CKLRT): in this package, we develop a kernel machine regression framework
to model the overall genetic effect of a SNP-set, considering the possible
GE interaction. Specifically, we use a composite kernel to specify the
overall genetic effect via a nonparametric function and we model
additional covariates parametrically within the regression framework. The
composite kernel is constructed as a weighted average of two kernels, one
corresponding to the genetic main effect and one corresponding to the GE
interaction effect. We propose a likelihood ratio test (LRT) and a
restricted likelihood ratio test (RLRT) for statistical significance. We
derive a Monte Carlo approach for the finite sample distributions of LRT
and RLRT statistics. (N. Zhao, H. Zhang, J. Clark, A. Maity, M. Wu.
Composite Kernel Machine Regression based on Likelihood Ratio Test with
Application for Combined Genetic and Gene-environment Interaction Effect
(Submitted).)

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
%doc %{rlibdir}/%{packname}/CKLRT_package.pdf
%doc %{rlibdir}/%{packname}/CKLRT_package.Rmd
%doc %{rlibdir}/%{packname}/CKLRT_package.tex
%doc %{rlibdir}/%{packname}/svm.tex
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
