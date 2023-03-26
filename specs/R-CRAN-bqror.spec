%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bqror
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Quantile Regression for Ordinal Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-NPflow 
BuildRequires:    R-CRAN-invgamma 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-NPflow 
Requires:         R-CRAN-invgamma 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-progress 

%description
Package provides functions for estimation and inference in Bayesian
quantile regression with ordinal outcomes. An ordinal model with 3 or more
outcomes (labeled OR1 model) is estimated by a combination of Gibbs
sampling and Metropolis-Hastings (MH) algorithm. Whereas an ordinal model
with exactly 3 outcomes (labeled OR2 model) is estimated using a Gibbs
sampling algorithm. The summary output presents the posterior mean,
posterior standard deviation, 95%% credible intervals, and the inefficiency
factors along with the two model comparison measures – logarithm of
marginal likelihood and the deviance information criterion (DIC). The
package also provides functions for computing the covariate effects and
other functions that aids either the estimation or inference in quantile
ordinal models. Rahman, M. A. (2016).“Bayesian Quantile Regression for
Ordinal Models.” Bayesian Analysis, 11(1): 1-24 <doi: 10.1214/15-BA939>.
Yu, K., and Moyeed, R. A. (2001). “Bayesian Quantile Regression.”
Statistics and Probability Letters, 54(4): 437–447 <doi:
10.1016/S0167-7152(01)00124-9>. Koenker, R., and Bassett, G.
(1978).“Regression Quantiles.” Econometrica, 46(1): 33-50 <doi:
10.2307/1913643>. Chib, S. (1995). “Marginal likelihood from the Gibbs
output.” Journal of the American Statistical Association,
90(432):1313–1321, 1995. <doi: 10.1080/01621459.1995.10476635>. Chib, S.,
and Jeliazkov, I. (2001). “Marginal likelihood from the
Metropolis-Hastings output.” Journal of the American Statistical
Association, 96(453):270–281, 2001. <doi: 10.1198/016214501750332848>.

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
