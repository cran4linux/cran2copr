%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cbass
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Classification -- Bayesian Adaptive Smoothing Splines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Fit multiclass Classification version of Bayesian Adaptive Smoothing
Splines (CBASS) to data using reversible jump MCMC. The multiclass
classification problem consists of a response variable that takes on
unordered categorical values with at least three levels, and a set of
inputs for each response variable. The CBASS model consists of a latent
multivariate probit formulation, and the means of the latent Gaussian
random variables are specified using adaptive regression splines. The MCMC
alternates updates of the latent Gaussian variables and the spline
parameters. All the spline parameters (variables, signs, knots, number of
interactions), including the number of basis functions used to model each
latent mean, are inferred. Functions are provided to process inputs,
initialize the chain, run the chain, and make predictions. Predictions are
made on a probabilistic basis, where, for a given input, the probabilities
of each categorical value are produced. See Marrs and Francom (2023)
"Multiclass classification using Bayesian multivariate adaptive regression
splines" Under review.

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
