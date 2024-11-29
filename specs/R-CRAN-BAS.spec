%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BAS
%global packver   1.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Variable Selection and Model Averaging using Bayesian Adaptive Sampling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Package for Bayesian Variable Selection and Model Averaging in linear
models and generalized linear models using stochastic or deterministic
sampling without replacement from posterior distributions.  Prior
distributions on coefficients are from Zellner's g-prior or mixtures of
g-priors corresponding to the Zellner-Siow Cauchy Priors or the mixture of
g-priors from Liang et al (2008) <DOI:10.1198/016214507000001337> for
linear models or mixtures of g-priors from Li and Clyde (2019)
<DOI:10.1080/01621459.2018.1469992> in generalized linear models. Other
model selection criteria include AIC, BIC and Empirical Bayes estimates of
g. Sampling probabilities may be updated based on the sampled models using
sampling w/out replacement or an efficient MCMC algorithm which samples
models using a tree structure of the model space as an efficient hash
table.  See Clyde, Ghosh and Littman (2010) <DOI:10.1198/jcgs.2010.09049>
for details on the sampling algorithms. Uniform priors over all models or
beta-binomial prior distributions on model size are allowed, and for large
p truncated priors on the model space may be used to enforce sampling
models that are full rank. The user may force variables to always be
included in addition to imposing constraints that higher order
interactions are included only if their parents are included in the model.
This material is based upon work supported by the National Science
Foundation under Division of Mathematical Sciences grant 1106891. Any
opinions, findings, and conclusions or recommendations expressed in this
material are those of the author(s) and do not necessarily reflect the
views of the National Science Foundation.

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
