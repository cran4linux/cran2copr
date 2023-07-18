%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phacking
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis for p-Hacking in Meta-Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.2.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-metabias 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.2.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-metabias 
Requires:         R-CRAN-metafor 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rstantools

%description
Fits right-truncated meta-analysis (RTMA), a bias correction for the joint
effects of p-hacking (i.e., manipulation of results within studies to
obtain significant, positive estimates) and traditional publication bias
(i.e., the selective publication of studies with significant, positive
results) in meta-analyses [see Mathur MB (2022). "Sensitivity analysis for
p-hacking in meta-analyses." <doi:10.31219/osf.io/ezjsx>.]. Unlike
publication bias alone, p-hacking that favors significant, positive
results (termed "affirmative") can distort the distribution of affirmative
results. To bias-correct results from affirmative studies would require
strong assumptions on the exact nature of p-hacking. In contrast, joint
p-hacking and publication bias do not distort the distribution of
published nonaffirmative results when there is stringent p-hacking (e.g.,
investigators who hack always eventually obtain an affirmative result) or
when there is stringent publication bias (e.g., nonaffirmative results
from hacked studies are never published). This means that any published
nonaffirmative results are from unhacked studies. Under these assumptions,
RTMA involves analyzing only the published nonaffirmative results to
essentially impute the full underlying distribution of all results prior
to selection due to p-hacking and/or publication bias. The package also
provides diagnostic plots described in Mathur (2022).

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
