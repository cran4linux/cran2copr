%global __brp_check_rpaths %{nil}
%global packname  txshift
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Estimation of the Causal Effects of Stochastic Interventions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-hal9001 >= 0.2.6
BuildRequires:    R-CRAN-haldensify >= 0.0.6
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-lspline 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-hal9001 >= 0.2.6
Requires:         R-CRAN-haldensify >= 0.0.6
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-lspline 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-cli 

%description
Efficient estimation of the population-level causal effects of stochastic
interventions on a continuous-valued exposure. Both one-step and targeted
minimum loss estimators are implemented for a causal parameter defined as
the counterfactual mean of an outcome of interest under a stochastic
intervention that may depend on the natural value of the exposure (i.e., a
modified treatment policy). To accommodate settings in which two-phase
sampling is employed, procedures for making use of inverse probability of
censoring weights are provided to facilitate construction of inefficient
and efficient one-step and targeted minimum loss estimators. The causal
parameter and its estimation were first described by Díaz and van der Laan
(2013) <doi:10.1111/j.1541-0420.2011.01685.x>, while the multiply robust
estimation procedure and its application to data arising in two-phase
sampling designs was detailed in NS Hejazi, MJ van der Laan, HE Janes, PB
Gilbert, and DC Benkeser (2020) <doi:10.1111/biom.13375>. Estimation of
nuisance parameters may be enhanced through the Super Learner ensemble
model in 'sl3', available for download from GitHub using
'remotes::install_github("tlverse/sl3")'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
