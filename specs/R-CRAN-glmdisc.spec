%global __brp_check_rpaths %{nil}
%global packname  glmdisc
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Discretization and Grouping for Logistic Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-caret >= 6.0.82
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-RcppNumerical 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-caret >= 6.0.82
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-gam 
Requires:         R-nnet 
Requires:         R-CRAN-RcppNumerical 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-graphics 

%description
A Stochastic-Expectation-Maximization (SEM) algorithm (Celeux et al.
(1995) <https://hal.inria.fr/inria-00074164>) associated with a Gibbs
sampler which purpose is to learn a constrained representation for
logistic regression that is called quantization (Ehrhardt et al. (2019)
<arXiv:1903.08920>). Continuous features are discretized and categorical
features' values are grouped to produce a better logistic regression
model. Pairwise interactions between quantized features are dynamically
added to the model through a Metropolis-Hastings algorithm (Hastings, W.
K. (1970) <doi:10.1093/biomet/57.1.97>).

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
