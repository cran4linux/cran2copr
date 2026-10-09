%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  silentema
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Missingness Graphs and Sensitivity Analysis for EMA Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Tools for diagnosing and correcting informative nonresponse in ecological
momentary assessment (EMA) and other experience-sampling designs. Declares
the assumed nonresponse mechanism as a dynamic missingness graph built
from a taxonomy of seven motifs, following the graphical missing-data
framework of Mohan and Pearl (2021) <doi:10.1080/01621459.2021.1874961>;
checks by d-separation which within-person and between-person estimands of
a two-level vector autoregressive model remain recoverable and by which
estimator; tests whether skipped prompts were informative (the silence
test and the sensor-gap test, with cluster-robust inference after Cameron
and Miller (2015) <doi:10.3368/jhr.50.2.317>); estimates the temporal and
contemporaneous networks from answered adjacent prompts with the
half-panel jackknife of Dhaene and Jochmans (2015)
<doi:10.1093/restud/rdv007>, by inverse-probability weighting on an
observed context, and by full-information maximum likelihood with the
state-space expectation-maximization (EM) algorithm of Shumway and Stoffer
(1982) <doi:10.1111/j.1467-9892.1982.tb00349.x>; profiles the estimates
over a self-censoring sensitivity parameter (inverse-probability weighting
with a fixed probit selection model whose intercept is calibrated to the
response rate); calibrates that parameter from passive sensors, randomized
probes, or the post-skip contrast; computes worst-case bounds for person
means in the spirit of Manski (2003) <doi:10.1007/b97478>; writes a
preregistration-ready missingness declaration; and simulates
experience-sampling data under every motif. The methods are described in
Yu (2026, manuscript under review); the accompanying materials are
archived at <https://osf.io/x6d2t/>.

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
