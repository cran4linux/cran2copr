%global packname  optiSel
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Optimum Contribution Selection and Population Genetics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-CRAN-nadiv 
BuildRequires:    R-CRAN-pedigree 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ECOSolveR 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-optiSolve 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-Matrix 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-kinship2 
Requires:         R-CRAN-nadiv 
Requires:         R-CRAN-pedigree 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-stringr 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-purrr 
Requires:         R-graphics 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magic 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ECOSolveR 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-optiSolve 

%description
A framework for the optimization of breeding programs via optimum
contribution selection and mate allocation. An easy to use set of function
for computation of optimum contributions of selection candidates, and of
the population genetic parameters to be optimized. These parameters can be
estimated using pedigree or genotype information, and include kinships,
kinships at native haplotype segments, and breed composition of crossbred
individuals. They are suitable for managing genetic diversity, removing
introgressed genetic material, and accelerating genetic gain.
Additionally, functions are provided for computing genetic contributions
from ancestors, inbreeding coefficients, the native effective size, the
native genome equivalent, pedigree completeness, and for preparing and
plotting pedigrees.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
