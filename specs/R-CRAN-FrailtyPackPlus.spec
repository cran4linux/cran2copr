%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FrailtyPackPlus
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shared, Correlated, Additive, and Zero-Inflated Frailty Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-utils 

%description
Fits and compares shared, correlated, additive, zero-inflated promotion
cure-rate, and k-out-of-M one-shot device frailty survival models under
Bayesian Markov chain Monte Carlo (MCMC) and Maximum Likelihood Estimation
(MLE) frameworks. Supports ten baseline hazard distributions (Weibull,
Exponential, Generalized Exponential, Exponential Power, Linear Failure
Rate, Generalized Log-Logistic, Generalized Weibull, Generalized Rayleigh,
Weighted Exponential, Extended Weibull) and eight frailty distributions
(Gamma, Inverse Gaussian, Positive Stable, Compound Poisson, Compound
Negative Binomial, Generalized Lindley, Weighted Lindley, Mixture of
Inverse Gaussians). Implements reversed hazard rate (RHR) models for
bivariate left-censored survival data, additive shared frailty models
under random right censoring, and one-shot device reliability analysis.
Provides goodness-of-fit testing, information criteria (AIC, BIC, AICc,
HQIC, DIC, EAIC, EBIC, LPML), convergence diagnostics (Geweke,
Gelman-Rubin, Heidelberger-Welch), Bayes factors, residual analyses, and
diagnostic visualizations. Methodologies are based on Hanagal and Dabade
(2013) <doi:10.1016/j.spl.2013.07.015>, Hanagal and Dabade (2013)
<doi:10.1080/03610918.2012.661909>, Hanagal and Dabade (2015)
<doi:10.1080/03610926.2013.804561>, Hanagal and Bhambure (2015)
<doi:10.3233/MAS-140308>, Hanagal and Bhambure (2016)
<doi:10.1080/03610926.2014.901380>, Hanagal, Pandey, and Ganguly (2017)
<doi:10.1080/03610918.2015.1085559>, Hanagal and Pandey (2018)
<doi:10.1080/03610926.2018.1549256>, Hanagal (2020)
<doi:10.1080/03610926.2020.1736305>, Tyagi et al. (2021)
<doi:10.1007/s40314-021-01666-5>, Pandey, Hanagal, Tyagi, and Gupta (2021)
<doi:10.1142/S0218539321500406>, Tyagi, Pandey, and Chesneau (2022)
<doi:10.1007/s42519-021-00241-9>, Pandey, Hanagal, and Tyagi (2022)
<doi:10.2478/stattrans-2022-0048>, Tyagi, Pandey, and Chesneau (2022)
<doi:10.1007/s13571-022-00278-1>, Tyagi, Pandey, Hanagal, and Chesneau
(2024) <doi:10.1080/03610918.2024.2391874>, Kiprotich et al. (2025)
<doi:10.1080/02664763.2025.2560510>, Assuncao et al. (2026)
<doi:10.1002/bimj.70162>, Chen et al. (1999)
<doi:10.1080/01621459.1999.10474198>, Dunn and Smyth (1996)
<doi:10.1080/10618600.1996.10474708>, Ling et al. (2021)
<doi:10.3390/math9233032>, Yu, So, and Balakrishnan (2025)
<doi:10.1016/B978-0-44-331694-4.00006-2>, Balakrishnan, Ling, and So
(2021, ISBN:978-1-119-77795-3), and McGilchrist and Aisbett (1991)
<doi:10.2307/2532138>.

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
