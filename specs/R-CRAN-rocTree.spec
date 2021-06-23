%global __brp_check_rpaths %{nil}
%global packname  rocTree
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Receiver Operating Characteristic (ROC)-Guided Classificationand Survival Tree

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-survival >= 2.38
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-data.tree >= 0.7.5
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-survival >= 2.38
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-data.tree >= 0.7.5
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-Rcpp 

%description
Receiver Operating Characteristic (ROC)-guided survival trees and ensemble
algorithms are implemented, providing a unified framework for
tree-structured analysis with censored survival outcomes. A time-invariant
partition scheme on the survivor population was considered to incorporate
time-dependent covariates. Motivated by ideas of randomized tests,
generalized time-dependent ROC curves were used to evaluate the
performance of survival trees and establish the optimality of the target
hazard/survival function. The optimality of the target hazard function
motivates us to use a weighted average of the time-dependent area under
the curve (AUC) on a set of time points to evaluate the prediction
performance of survival trees and to guide splitting and pruning. A
detailed description of the implemented methods can be found in Sun et al.
(2019) <arXiv:1809.05627>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
