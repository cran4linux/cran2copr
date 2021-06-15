%global packname  activityGCMM
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Circular Mixed Effect Mixture Models of Animal Activity Patterns

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-overlap 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-runjags 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-overlap 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Bayesian parametric generalized circular mixed effect mixture models
(GCMMs) for estimating animal activity patterns from camera trap data and
other nested data structures using 'JAGS', including automatic Bayesian
k-cluster selection and random circular intercepts for nested data. The
GCMM function automatically selects the number of components for the
mixture model (supporting up to 4 mixture components) based on a Bayesian
linear finite normal mixture model and fits a Bayesian parametric circular
mixed effect mixture model with one or two random effects as random
circular intercepts with a a von Mises or wrapped Cauchy distribution.
Provides graphs of the combined mixture model or separate mixture
components. Functionality is provided to allow quantitative comparisons
between model parameters. See Campbell et al. (in press) It's time to
expand our analyses of animal activity; Campbell et al. (in press)
Temporal and microspatial niche partitioning; Campbell et al. (in press) A
novel approach to comparing animal activity patterns. News, updates, and
tutorials will be available on www.atlasgoldenwolf.org/stats and
www.github.com/LizADCampbell .

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
