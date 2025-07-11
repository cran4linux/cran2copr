%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RBaM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Modeling: Estimate a Computer Model and Make Uncertain Predictions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-R.utils 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-rlang 
Requires:         R-tools 
Requires:         R-CRAN-tidyr 

%description
An interface to the 'BaM' (Bayesian Modeling) engine, a 'Fortran'-based
executable aimed at estimating a model with a Bayesian approach and using
it for prediction, with a particular focus on uncertainty quantification.
Classes are defined for the various building blocks of 'BaM' inference
(model, data, error models, Markov Chain Monte Carlo (MCMC) samplers,
predictions). The typical usage is as follows: (1) specify the model to be
estimated; (2) specify the inference setting (dataset, parameters, error
models...); (3) perform Bayesian-MCMC inference; (4) read, analyse and use
MCMC samples; (5) perform prediction experiments. Technical details are
available (in French) in Renard (2017)
<https://hal.science/hal-02606929v1>. Examples of applications include
Mansanarez et al. (2019) <doi:10.1029/2018WR023389>, Le Coz et al. (2021)
<doi:10.1002/hyp.14169>, Perret et al. (2021) <doi:10.1029/2020WR027745>,
Darienzo et al. (2021) <doi:10.1029/2020WR028607> and Perret et al. (2023)
<doi:10.1061/JHEND8.HYENG-13101>.

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
