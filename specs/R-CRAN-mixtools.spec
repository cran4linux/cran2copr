%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixtools
%global packver   2.0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Analyzing Finite Mixture Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-segmented 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
Analyzes finite mixture models for various parametric and semiparametric
settings.  This includes mixtures of parametric distributions (normal,
multivariate normal, multinomial, gamma), various Reliability Mixture
Models (RMMs), mixtures-of-regressions settings (linear regression,
logistic regression, Poisson regression, linear regression with
changepoints, predictor-dependent mixing proportions, random effects
regressions, hierarchical mixtures-of-experts), and tools for selecting
the number of components (bootstrapping the likelihood ratio test
statistic, mixturegrams, and model selection criteria).  Bayesian
estimation of mixtures-of-linear-regressions models is available as well
as a novel data depth method for obtaining credible bands.  This package
is based upon work supported by the National Science Foundation under
Grant No. SES-0518772 and the Chan Zuckerberg Initiative: Essential Open
Source Software for Science (Grant No. 2020-255193).

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
