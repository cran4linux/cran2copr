%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RGCCA
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized and Sparse Generalized Canonical Correlation Analysis for Multiblock Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-caret 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-ggrepel 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Multi-block data analysis concerns the analysis of several sets of
variables (blocks) observed on the same group of individuals. The main
aims of the RGCCA package are: to study the relationships between blocks
and to identify subsets of variables of each block which are active in
their relationships with the other blocks. This package allows to (i) run
R/SGCCA and related methods (link{rgcca}), (ii) help the user to find out
the optimal parameters for R/SGCCA such as regularization parameters (tau
or sparsity) (link{rgcca_permutation}, link{rgcca_cv}), (iii) evaluate
the stability of the RGCCA results and their significance
(link{rgcca_bootstrap} and link{rgcca_stability}), (iv) build predictive
models from the R/SGCCA (link{rgcca_predict}), (v) Generic print() and
plot() functions apply to all these functionalities.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
