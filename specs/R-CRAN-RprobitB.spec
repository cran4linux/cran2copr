%global __brp_check_rpaths %{nil}
%global packname  RprobitB
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Probit Choice Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-plotROC 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-plotROC 
Requires:         R-CRAN-MASS 

%description
Bayes estimation of probit choice models, both in the cross-sectional and
panel setting. The package can analyze binary, multivariate, ordered, and
ranked choices, and places a special focus on modeling heterogeneity of
choice behavior among deciders. The main functionality includes model
fitting via Markov chain Monte Carlo methods, tools for convergence
diagnostic, choice data simulation, in-sample and out-of-sample choice
prediction, and model selection using information criteria and Bayes
factors. The latent class model extension facilitates preference-based
decider classification, where the number of latent classes can be inferred
via the Dirichlet process or a weight-based updating scheme. This allows
for flexible modeling of choice behavior without the need to impose
structural constraints. For a reference on the method see Oelschlaeger and
Bauer (2021) <https://trid.trb.org/view/1759753>.

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
