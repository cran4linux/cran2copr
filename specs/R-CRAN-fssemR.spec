%global packname  fssemR
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Fused Sparse Structural Equation Models to Jointly Infer GeneRegulatory Network

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-glmnet 
Requires:         R-MASS 

%description
An optimizer of Fused-Sparse Structural Equation Models, which is the
state of the art jointly fused sparse maximum likelihood function for
structural equation models proposed by Xin Zhou and Xiaodong Cai (2018
<doi:10.1101/466623>).

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
%doc %{rlibdir}/%{packname}/00_SparsemaximumLiklihood.R
%doc %{rlibdir}/%{packname}/01_RidgeRegression.R
%doc %{rlibdir}/%{packname}/02_FSSEMsolver.R
%doc %{rlibdir}/%{packname}/03_QTLNet.R
%doc %{rlibdir}/%{packname}/04_FSSEMsolver2.R
%doc %{rlibdir}/%{packname}/05_DataprocLungCancer.R
%doc %{rlibdir}/%{packname}/06_RunMatrixEQTL.R
%doc %{rlibdir}/%{packname}/07_glmnetBackend.R
%doc %{rlibdir}/%{packname}/08_DataprocGastricCancer.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/README.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
