%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multinomineq
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference for Multinomial Models with Inequality Constraints

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-RcppXPtrUtils 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-parallel 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-RcppXPtrUtils 

%description
Implements Gibbs sampling and Bayes factors for multinomial models with
linear inequality constraints on the vector of probability parameters. As
special cases, the model class includes models that predict a linear order
of binomial probabilities (e.g., p[1] < p[2] < p[3] < .50) and mixture
models assuming that the parameter vector p must be inside the convex hull
of a finite number of predicted patterns (i.e., vertices). A formal
definition of inequality-constrained multinomial models and the
implemented computational methods is provided in: Heck, D.W., &
Davis-Stober, C.P. (2019). Multinomial models with linear inequality
constraints: Overview and improvements of computational methods for
Bayesian inference. Journal of Mathematical Psychology, 91, 70-87.
<doi:10.1016/j.jmp.2019.03.004>. Inequality-constrained multinomial models
have applications in the area of judgment and decision making to fit and
test random utility models (Regenwetter, M., Dana, J., & Davis-Stober,
C.P. (2011). Transitivity of preferences. Psychological Review, 118,
42–56, <doi:10.1037/a0021150>) or to perform outcome-based strategy
classification to select the decision strategy that provides the best
account for a vector of observed choice frequencies (Heck, D.W., Hilbig,
B.E., & Moshagen, M. (2017). From information processing to decisions:
Formalizing and comparing probabilistic choice models. Cognitive
Psychology, 96, 26–40. <doi:10.1016/j.cogpsych.2017.05.003>).

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
