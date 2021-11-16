%global __brp_check_rpaths %{nil}
%global packname  BMRMM
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Implementation of the Bayesian Markov (Renewal) Mixed Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-CRAN-logOfGamma 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mhsmm 
BuildRequires:    R-CRAN-multicool 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-fields 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gsubfn 
Requires:         R-CRAN-logOfGamma 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mhsmm 
Requires:         R-CRAN-multicool 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-utils 

%description
The Bayesian Markov renewal mixed models take sequentially observed
categorical data with continuous duration times, being either state
duration or inter-state duration. These models comprehensively analyze the
stochastic dynamics of both state transitions and duration times under the
influence of multiple exogenous factors and random individual effect. The
default setting flexibly models the transition probabilities using
Dirichlet mixtures and the duration times using gamma mixtures. It also
provides the flexibility of modeling the categorical sequences using
Bayesian Markov mixed models alone, either ignoring the duration times
altogether or dividing duration time into multiples of an additional
category in the sequence by a user-specific unit. The package allows
extensive inference of the state transition probabilities and the duration
times as well as relevant plots and graphs. It also includes a synthetic
data set to demonstrate the desired format of input data set and the
utility of various functions. Methods for Bayesian Markov renewal mixed
models are as described in: Abhra Sarkar et al., (2018)
<doi:10.1080/01621459.2018.1423986> and Yutong Wu et al., (2021)
<arXiv:2107.07648>.

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
