%global packname  BOSSreg
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Best Orthogonalized Subset Selection (BOSS)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Best orthogonalized subset selection (BOSS) is a least-squares (LS) based
subset selection method, that performs best subset selection upon an
orthogonalized basis of ordered predictors, with the computational effort
of a single ordinary LS fit. This package provides a highly optimized
implementation of BOSS and estimates a heuristic degrees of freedom for
BOSS, which can be plugged into an information criterion (IC) such as AICc
in order to select the subset from candidates. It provides various choices
of IC, including AIC, BIC, AICc, Cp and GCV. It also implements the
forward stepwise selection (FS) with no additional computational cost,
where the subset of FS is selected via cross-validation (CV). CV is also
an option for BOSS. For details see: Tian, Hurvich and Simonoff (2019),
"On the Use of Information Criteria for Subset Selection in Least Squares
Regression", <arXiv:1911.10191>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
