%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  calibmsm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calibration Plots for the Transition Probabilities from Multistate Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mstate 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mstate 
Requires:         R-CRAN-rms 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-VGAM 

%description
Assess the calibration of an existing (i.e. previously developed)
multistate model through calibration plots. Calibration is assessed using
one of three methods. 1) Calibration methods for binary logistic
regression models applied at a fixed time point in conjunction with
inverse probability of censoring weights. 2) Calibration methods for
multinomial logistic regression models applied at a fixed time point in
conjunction with inverse probability of censoring weights. 3)
Pseudo-values estimated using the Aalen-Johansen estimator of observed
risk. All methods are applied in conjunction with landmarking when
required. These calibration plots evaluate the calibration (in a
validation cohort of interest) of the transition probabilities estimated
from an existing multistate model. While package development has focused
on multistate models, calibration plots can be produced for any model
which utilises information post baseline to update predictions (e.g.
dynamic models); competing risks models; or standard single outcome
survival models, where predictions can be made at any landmark time. The
underpinning methodology is currently undergoing peer review; see Pate et
al. (2023) <arXiv:2308.13394> and Pate et al. (2023)
<https://alexpate30.github.io/calibmsm/articles/Overview.html>.

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
