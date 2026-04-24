%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  babebi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation and Validation for Small-N Designs with Rater Bias

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
Approximate Bayesian inference and Monte Carlo validation for small-N
repeated-measures designs with two time points and two raters. The package
is intended for applications in which sample size is limited and the
observed outcome may be affected by rater-specific bias. User-supplied
data are standardised into a common long-format structure. Pre-post
effects are analysed using difference scores in a linear model with a
rater indicator as covariate. Posterior summaries for the regression
coefficients are obtained from a large-sample normal approximation centred
at the least-squares estimate with plug-in covariance under a flat
improper prior. Evidence for a non-zero pre-post effect, adjusted for
rater differences, is summarised using a BIC-based approximation to the
Bayes factor for comparison between models with and without the pre-post
effect. Monte Carlo validation uses design quantities estimated from the
observed data, including sample size, mean pre-post change, and
second-rater additive discrepancy, and summarises inferential performance
in terms of bias, root mean squared error, credible interval coverage,
posterior tail probabilities, and mean Bayes factor values. For background
on the BIC approximation and Bayes factors, see Schwarz (1978)
<doi:10.1214/aos/1176344136> and Kass and Raftery (1995)
<doi:10.1080/01621459.1995.10476572>.

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
