%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesQRCount
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Bayesian Quantile Regression for Count Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Implements Bayesian quantile regression for count data using the jittering
technique for discrete data smoothing and an asymmetric Laplace
distribution likelihood. Supports adaptive variable selection via a
random-bridge penalty with a beta prior on the power parameter, as well as
fixed-bridge and Lasso penalties. Utilizes Markov chain Monte Carlo with
Gibbs sampling and adaptive Metropolis-Hastings algorithms for posterior
inference, provides Gelman-Rubin convergence diagnostics, and predicts
conditional quantiles for count responses. Methodology and applications
are based on the following key references: Luo, Zhou, Hu, and Li (2026,
Journal of Mathematics, 2026:1543166, <doi:10.1155/jom/1543166>), Koenker
and Bassett (1978, Econometrica, 46, 33-50, <doi:10.2307/1913643>),
Machado and Santos Silva (2005, Journal of the American Statistical
Association, 100, 1226-1237, <doi:10.1198/016214505000000330>), Yu and
Moyeed (2001, Statistics and Probability Letters, 54, 437-447,
<doi:10.1016/S0167-7152(01)00124-9>), Polson, Scott, and Windle (2014,
Journal of the Royal Statistical Society Series B, 76, 713-733,
<doi:10.1111/rssb.12042>), Park and Casella (2008, Journal of the American
Statistical Association, 103, 681-686, <doi:10.1198/016214508000000337>),
and Roberts and Rosenthal (2009, Journal of Computational and Graphical
Statistics, 18, 349-367, <doi:10.1198/jcgs.2009.06134>).

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
