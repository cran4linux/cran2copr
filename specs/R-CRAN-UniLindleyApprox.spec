%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UniLindleyApprox
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Point Estimation Using Lindley's Approximation Under Censoring Schemes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MASS 

%description
Performs Bayesian point estimation using Lindley's Approximation (1980)
<doi:10.1111/j.2517-6161.1980.tb01102.x> for arbitrary univariate
probability distributions under numerous censoring and truncation schemes.
Users supply the probability density function (PDF), cumulative
distribution function (CDF), survival function, log-prior density, initial
parameter vector, support bounds, and observed data; the package
automatically computes Bayesian point estimates under various loss
functions using Lindley's approximation. Supported schemes include
complete data, right censoring, left censoring, interval censoring, random
censoring, block random censoring, Type-I censoring, Type-II censoring,
progressive Type-II censoring, progressive first failure censoring, joint
Type-I censoring, joint Type-II censoring, balanced joint progressive
Type-II censoring, hybrid censoring, hybrid Type-I censoring, hybrid
Type-II censoring, Type-I hybrid censoring, Type-II progressively hybrid
censoring, doubly Type-II censoring, middle censoring, right truncation,
and left truncation. The package computes posterior expectations of
arbitrary smooth functions, supports multiple loss functions (squared
error loss function (SELF), weighted squared error loss function (WSELF),
modified quadratic squared error loss function (MQSELF), precautionary
loss function (PLF), entropy loss function (ELF), linear-exponential
(LINEX), generalized entropy loss function (GELF), Kullback-Leibler loss
function (K-Loss), and user-defined), provides model selection criteria
(Akaike information criterion (AIC), Bayesian information criterion (BIC),
corrected Akaike information criterion (AICc), Hannan-Quinn information
criterion (HQIC), consistent Akaike information criterion (CAIC), Kullback
information criterion (KIC)), goodness-of-fit statistics
(Kolmogorov-Smirnov, Anderson-Darling, Cramer-von Mises, Watson,
Chi-square), residual analysis (Cox-Snell, Martingale, Deviance, Pearson,
Generalized, Randomized quantile), comprehensive visualization tools,
prediction utilities, and simulation functions for benchmarking
estimators. Methods are described in Lindley (1980)
<doi:10.1111/j.2517-6161.1980.tb01102.x>, Tierney and Kadane (1986)
<doi:10.2307/2234555>, Tierney, Kass, and Kadane (1989)
<doi:10.2307/2335663>, Nagar, Kumar, and Krishna (2026)
<doi:10.59467/IJASS.2026.22.1>, Goel, Kumar, and Krishna (2026,
"Estimation in power Lindley distributions using balanced joint
progressively Type-II censored data"), Wu and Kus (2009)
<doi:10.1016/j.csda.2009.03.010>, Goel and Krishna (2026)
<doi:10.1007/s13198-026-03208-w>, Balakrishnan and Aggarwala (2000,
ISBN:978-1-4612-1334-5), Mondal and Kundu (2020)
<doi:10.1080/03610926.2018.1554128>, Ding and Gui (2023)
<doi:10.3390/math11092003>, Prajapati, Mitra, and Kundu (2019)
<doi:10.1007/s13571-018-0167-0>, Yadav, Jaiswal, and Yadav (2026)
<doi:10.1007/s11135-026-02647-8>, Iyer, Jammalamadaka, and Kundu (2008)
<doi:10.1016/j.jspi.2007.03.062>, Banerjee and Kundu (2008)
<doi:10.1109/TR.2008.916890>, and Kundu and Joarder (2006)
<doi:10.1016/j.csda.2005.05.002>.

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
