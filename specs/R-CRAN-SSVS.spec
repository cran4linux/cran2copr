%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSVS
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Stochastic Search Variable Selection (SSVS)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-BoomSpikeSlab 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-BoomSpikeSlab 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-gridExtra 

%description
Functions for performing stochastic search variable selection (SSVS) for
binary and continuous outcomes and visualizing the results. SSVS is a
Bayesian variable selection method used to estimate the probability that
individual predictors should be included in a regression model. Using MCMC
estimation, the method samples thousands of regression models in order to
characterize the model uncertainty regarding both the predictor set and
the regression parameters. For details see Bainter, McCauley, Wager, and
Losin (2020) Improving practices for selecting a subset of important
predictors in psychology: An application to predicting pain, Advances in
Methods and Practices in Psychological Science 3(1), 66-80
<DOI:10.1177/2515245919885617>.

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
