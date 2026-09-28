%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CPHazard
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hazard Change Point Models for Different Lifetime Distributions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lamW 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-EnvStats 
Requires:         R-CRAN-lamW 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-EnvStats 

%description
Estimates the parameters of models with a single change-point in the
hazard rate for time-to-event data. Supported models include the
exponential (Gijbels & Gürler (2003)
<doi:10.1023/B:LIDA.0000012424.71723.9d>, Matthews & Farewell (1982)
<doi:10.2307/2530460>), Exponential-Lindley (Joshi & Rattihalli (2020)
<doi:10.1007/978-981-15-5414-8_29>), Lindley (Joshi, Jose, & Bhati (2016)
<doi:10.1080/03610918.2015.1096381>), log-logistic (Nadar, Upadhyay, &
Joshi (2025) <doi:10.3390/math13091457>), and Weibull (Williams & Kim
(2013) <doi:10.1080/03610926.2011.600505>) hazard change-point models.
Provides functions for generating random variates and evaluating the
probability density function (PDF) and the cumulative distribution
function (CDF) of the fitted change-point models. Includes Kaplan-Meier
and Nelson-Aalen diagnostic plots, together with goodness-of-fit measures
such as the Akaike Information Criterion (AIC), the Bayesian Information
Criterion (BIC), distance metrics such as the L1-norm and L2-norm, and the
Kolmogorov-Smirnov (K-S) statistic for model evaluation.

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
