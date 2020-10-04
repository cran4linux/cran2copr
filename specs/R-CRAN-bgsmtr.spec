%global packname  bgsmtr
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          2%{?dist}%{?buildtag}
Summary:          Bayesian Group Sparse Multi-Task Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.3.3
BuildRequires:    R-CRAN-glmnet >= 2.0.13
BuildRequires:    R-CRAN-LaplacesDemon >= 16.1.0
BuildRequires:    R-CRAN-mnormt >= 1.5.4
BuildRequires:    R-CRAN-statmod >= 1.4.26
BuildRequires:    R-Matrix >= 1.2.6
BuildRequires:    R-CRAN-EDISON >= 1.1.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.5
BuildRequires:    R-CRAN-matrixcalc >= 1.0.3
BuildRequires:    R-CRAN-CholWishart >= 0.9.3
BuildRequires:    R-CRAN-miscTools >= 0.6.22
BuildRequires:    R-CRAN-inline >= 0.3.15
BuildRequires:    R-CRAN-coda >= 0.18.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-sparseMVN > 0.2.0
Requires:         R-methods >= 3.3.3
Requires:         R-CRAN-glmnet >= 2.0.13
Requires:         R-CRAN-LaplacesDemon >= 16.1.0
Requires:         R-CRAN-mnormt >= 1.5.4
Requires:         R-CRAN-statmod >= 1.4.26
Requires:         R-Matrix >= 1.2.6
Requires:         R-CRAN-EDISON >= 1.1.1
Requires:         R-CRAN-mvtnorm >= 1.0.5
Requires:         R-CRAN-matrixcalc >= 1.0.3
Requires:         R-CRAN-CholWishart >= 0.9.3
Requires:         R-CRAN-miscTools >= 0.6.22
Requires:         R-CRAN-inline >= 0.3.15
Requires:         R-CRAN-coda >= 0.18.1
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-sparseMVN > 0.2.0

%description
Implementation of Bayesian multi-task regression models and was developed
within the context of imaging genetics. The package can currently fit two
models. The Bayesian group sparse multi-task regression model of Greenlaw
et al. (2017)<doi:10.1093/bioinformatics/btx215> can be fit with
implementation using Gibbs sampling. An extension of this model developed
by Song, Ge et al. to accommodate both spatial correlation as well as
correlation across brain hemispheres can also be fit using either
mean-field variational Bayes or Gibbs sampling. The model can also be used
more generally for multivariate (non-imaging) phenotypes with spatial
correlation.

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
