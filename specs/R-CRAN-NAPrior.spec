%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NAPrior
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Network Meta-Analytic Predictive Prior for Mid-Trial SoC Changes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 

%description
Implements the Network meta-Analytic Predictive (NAP) prior framework to
accommodate changes in the standard of care (SoC) during ongoing
randomized controlled trials (RCTs). The method synthesizes pre- and
post-change in-trial data by leveraging external evidence, particularly
head-to-head trials comparing the original and new standards of care, to
bridge the two evidence periods and enable principled borrowing. The
package provides utilities to construct NAP-based priors and perform
Bayesian inference for time-to-event endpoints using summarized trial
evidence.

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
