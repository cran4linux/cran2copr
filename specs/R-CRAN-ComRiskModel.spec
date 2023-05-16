%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ComRiskModel
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting of Complementary Risk Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-AdequacyModel 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-AdequacyModel 
Requires:         R-graphics 
Requires:         R-stats 

%description
Evaluates the probability density function (PDF), cumulative distribution
function (CDF), quantile function (QF), random numbers and maximum
likelihood estimates (MLEs) of well-known complementary binomial-G,
complementary negative binomial-G and complementary geometric-G families
of distributions taking baseline models such as exponential, extended
exponential, Weibull, extended Weibull, Fisk, Lomax, Burr-XII and Burr-X.
The functions also allow computing the goodness-of-fit measures namely the
Akaike-information-criterion (AIC), the Bayesian-information-criterion
(BIC), the minimum value of the negative log-likelihood (-2L) function,
Anderson-Darling (A) test, Cramer-Von-Mises (W) test, Kolmogorov-Smirnov
test, P-value and convergence status. Moreover, some commonly used data
sets from the fields of actuarial, reliability, and medical science are
also provided. Related works include: a) Tahir, M. H., & Cordeiro, G. M.
(2016). Compounding of distributions: a survey and new generalized
classes. Journal of Statistical Distributions and Applications, 3, 1-35.
<doi:10.1186/s40488-016-0052-1>.

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
