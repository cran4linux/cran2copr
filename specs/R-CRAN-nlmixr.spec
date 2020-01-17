%global packname  nlmixr
%global packver   1.1.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1.3
Release:          1%{?dist}
Summary:          Nonlinear Mixed Effects Models in Population Pharmacokineticsand Pharmacodynamics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-vpc >= 1.0.0
BuildRequires:    R-CRAN-RxODE >= 0.9.1.7
BuildRequires:    R-CRAN-RcppArmadillo >= 0.5.600.2.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-dparser >= 0.1.8
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-lattice 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lbfgs 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-rex 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-n1qn1 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-sys 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-huxtable 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-lbfgsb3c 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-vpc >= 1.0.0
Requires:         R-CRAN-RxODE >= 0.9.1.7
Requires:         R-CRAN-RcppArmadillo >= 0.5.600.2.0
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-brew 
Requires:         R-lattice 
Requires:         R-parallel 
Requires:         R-CRAN-lbfgs 
Requires:         R-CRAN-dparser >= 0.1.8
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-rex 
Requires:         R-CRAN-minqa 
Requires:         R-Matrix 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-n1qn1 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-nlme 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-sys 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-huxtable 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-yaml 

%description
Fit and compare nonlinear mixed-effects models in differential equations
with flexible dosing information commonly seen in pharmacokinetics and
pharmacodynamics (Almquist, Leander, and Jirstrand 2015
<doi:10.1007/s10928-015-9409-1>). Differential equation solving is by
compiled C code provided in the 'RxODE' package (Wang, Hallow, and James
2015 <doi:10.1002/psp4.12052>).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHT
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/nlmixr-template.docx
%doc %{rlibdir}/%{packname}/quadrule.diff
%doc %{rlibdir}/%{packname}/revision.txt
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/TODOs.txt
%doc %{rlibdir}/%{packname}/tools
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
