%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MYIS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Moreau-Yosida' Importance Sampling for Statistical Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements 'Moreau-Yosida' Markov chain Monte Carlo ('MCMC') importance
sampling for parameter estimation and Bayesian inference under smooth,
non-differentiable, or light-tailed target posterior distributions and
arbitrary probability models with complete or censored data. Users supply
user-defined probability density functions, optional distribution
functions, parameter ranges, and observations subject to complete, right,
left, interval, Type-I, Type-II, progressive Type-II, first-failure, or
truncation schemes. Constructs 'Moreau-Yosida' envelopes, gradient-based
proposals ('MALA', 'HMC', or 'RWM'), self-normalized importance weights,
batch-means asymptotic variance estimates, and Bayesian marginal
quantiles. Methodologies are based on 'Shukla', 'Vats', and 'Chi' (2025)
<doi:10.48550/arXiv.2501.02228>, 'Pereyra' (2016)
<doi:10.1111/sjos.12208>, 'Durmus' and others (2022)
<doi:10.1214/22-EJS2027>, 'Chen' and 'Shao' (1999)
<doi:10.1214/ss/1009211804>, 'Roberts' and 'Rosenthal' (1998)
<doi:10.1214/aoap/1028903378>, 'Geweke' (1989) <doi:10.2307/2290062>,
'Hesterberg' (1995) <doi:10.1080/00031305.1995.10476138>, and
'Balakrishnan' and 'Aggarwala' (2000, ISBN:978-0-8176-4001-9).

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
