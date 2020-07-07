%global packname  mdpeer
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Graph-Constrained Regression with Enhanced RegularizationParameters Selection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-nlme 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-nlme 
Requires:         R-boot 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-glmnet 

%description
Provides graph-constrained regression methods in which regularization
parameters are selected automatically via estimation of equivalent Linear
Mixed Model formulation. 'riPEER' (ridgified Partially Empirical
Eigenvectors for Regression) method employs a penalty term being a linear
combination of graph-originated and ridge-originated penalty terms, whose
two regularization parameters are ML estimators from corresponding Linear
Mixed Model solution; a graph-originated penalty term allows imposing
similarity between coefficients based on graph information given whereas
additional ridge-originated penalty term facilitates parameters
estimation: it reduces computational issues arising from singularity in a
graph-originated penalty matrix and yields plausible results in situations
when graph information is not informative. 'riPEERc' (ridgified Partially
Empirical Eigenvectors for Regression with constant) method utilizes
addition of a diagonal matrix multiplied by a predefined (small) scalar to
handle the non-invertibility of a graph Laplacian matrix. 'vrPEER'
(variable reducted PEER) method performs variable-reduction procedure to
handle the non-invertibility of a graph Laplacian matrix.

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

%files
%{rlibdir}/%{packname}
