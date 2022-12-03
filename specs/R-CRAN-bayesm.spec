%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesm
%global packver   3.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference for Marketing/Micro-Econometrics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Covers many important models used in marketing and micro-econometrics
applications. The package includes: Bayes Regression (univariate or
multivariate dep var), Bayes Seemingly Unrelated Regression (SUR), Binary
and Ordinal Probit, Multinomial Logit (MNL) and Multinomial Probit (MNP),
Multivariate Probit, Negative Binomial (Poisson) Regression, Multivariate
Mixtures of Normals (including clustering), Dirichlet Process Prior
Density Estimation with normal base, Hierarchical Linear Models with
normal prior and covariates, Hierarchical Linear Models with a mixture of
normals prior and covariates, Hierarchical Multinomial Logits with a
mixture of normals prior and covariates, Hierarchical Multinomial Logits
with a Dirichlet Process prior and covariates, Hierarchical Negative
Binomial Regression Models, Bayesian analysis of choice-based conjoint
data, Bayesian treatment of linear instrumental variables models, Analysis
of Multivariate Ordinal survey data with scale usage heterogeneity (as in
Rossi et al, JASA (01)), Bayesian Analysis of Aggregate Random Coefficient
Logit Models as in BLP (see Jiang, Manchanda, Rossi 2009) For further
reference, consult our book, Bayesian Statistics and Marketing by Rossi,
Allenby and McCulloch (Wiley 2005) and Bayesian Non- and Semi-Parametric
Methods and Applications (Princeton U Press 2014).

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
