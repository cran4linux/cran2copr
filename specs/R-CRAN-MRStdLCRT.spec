%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MRStdLCRT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Robust Standardization for Longitudinal Cluster-Randomized Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-lme4 >= 1.1.30
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-gee 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-lme4 >= 1.1.30
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-reformulas 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-gee 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides estimation and leave-one-cluster-out jackknife standard errors
for four longitudinal cluster-randomized trial estimands: horizontal
individual average treatment effect (h-iATE), horizontal cluster average
treatment effect (h-cATE), vertical individual average treatment effect
(v-iATE), and vertical cluster-period average treatment effect (v-cATE),
using unadjusted and augmented (model-robust standardization) estimators.
The working model may be fit using linear mixed models for continuous
outcomes or generalized estimating equations and generalized linear mixed
models for binary outcomes. Period inclusion for aggregation is determined
automatically: only periods with both treated and control clusters are
included in the construction of the marginal means and treatment effect
contrasts. See Fang et al. (2025) <doi:10.48550/arXiv.2507.17190>.

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
