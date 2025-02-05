%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmcmc
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Markov Chain Monte Carlo Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-withr 

%description
Functions for simulating Markov chains using the Barker proposal to
compute Markov chain Monte Carlo (MCMC) estimates of expectations with
respect to a target distribution on a real-valued vector space. The Barker
proposal, described in Livingstone and Zanella (2022)
<doi:10.1111/rssb.12482>, is a gradient-based MCMC algorithm inspired by
the Barker accept-reject rule. It combines the robustness of simpler MCMC
schemes, such as random-walk Metropolis, with the efficiency of
gradient-based methods, such as the Metropolis adjusted Langevin
algorithm. The key function provided by the package is sample_chain(),
which allows sampling a Markov chain with a specified target distribution
as its stationary distribution. The chain is sampled by generating
proposals and accepting or rejecting them using a Metropolis-Hasting
acceptance rule. During an initial warm-up stage, the parameters of the
proposal distribution can be adapted, with adapters available to both:
tune the scale of the proposals by coercing the average acceptance rate to
a target value; tune the shape of the proposals to match covariance
estimates under the target distribution. As well as the default Barker
proposal, the package also provides implementations of alternative
proposal distributions, such as (Gaussian) random walk and Langevin
proposals. Optionally, if 'BridgeStan's R interface
<https://roualdes.github.io/bridgestan/latest/languages/r.html>, available
on GitHub <https://github.com/roualdes/bridgestan>, is installed, then
'BridgeStan' can be used to specify the target distribution to sample
from.

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
