%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  moderate.mediation
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Moderated Mediation Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-distr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-distr 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-foreach 

%description
Causal moderated mediation analysis using the methods proposed by Qin and
Wang (2022). Causal moderated mediation analysis is crucial for
investigating how, for whom, and where a treatment is effective by
assessing the heterogeneity of mediation mechanism across individuals and
contexts. This package enables researchers to estimate and test the
conditional and moderated mediation effects, assess their sensitivity to
unmeasured pre-treatment confounding, and visualize the results. The
package is built based on the quasi-Bayesian Monte Carlo method, because
it has relatively better performance at small sample sizes, and its
running speed is the fastest. The package is applicable to a treatment of
any scale, a binary or continuous mediator, a binary or continuous
outcome, and one or more moderators of any scale.

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
