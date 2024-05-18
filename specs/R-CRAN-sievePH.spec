%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sievePH
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sieve Analysis Methods for Proportional Hazards Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-np 

%description
Implements a suite of semiparametric and nonparametric kernel-smoothed
estimation and testing procedures for continuous mark-specific stratified
hazard ratio (treatment/placebo) models in a randomized treatment efficacy
trial with a time-to-event endpoint. Semiparametric methods, allowing
multivariate marks, are described in Juraska M and Gilbert PB (2013),
Mark-specific hazard ratio model with multivariate continuous marks: an
application to vaccine efficacy. Biometrics 69(2):328-337
<doi:10.1111/biom.12016>, and in Juraska M and Gilbert PB (2016),
Mark-specific hazard ratio model with missing multivariate marks. Lifetime
Data Analysis 22(4):606-25 <doi:10.1007/s10985-015-9353-9>. Nonparametric
kernel-smoothed methods, allowing univariate marks only, are described in
Sun Y and Gilbert PB (2012), Estimation of stratified mark‐specific
proportional hazards models with missing marks. Scandinavian Journal of
Statistics}, 39(1):34-52 <doi:10.1111/j.1467-9469.2011.00746.x>, and in
Gilbert PB and Sun Y (2015), Inferences on relative failure rates in
stratified mark-specific proportional hazards models with missing marks,
with application to human immunodeficiency virus vaccine efficacy trials.
Journal of the Royal Statistical Society Series C: Applied Statistics,
64(1):49-73 <doi:10.1111/rssc.12067>. Both semiparametric and
nonparametric approaches consider two scenarios: (1) the mark is fully
observed in all subjects who experience the event of interest, and (2) the
mark is subject to missingness-at-random in subjects who experience the
event of interest. For models with missing marks, estimators are
implemented based on (i) inverse probability weighting (IPW) of complete
cases (for the semiparametric framework), and (ii) augmentation of the IPW
estimating functions by leveraging correlations between the mark and
auxiliary data to 'impute' the augmentation term for subjects with missing
marks (for both the semiparametric and nonparametric framework). The
augmented IPW estimators are doubly robust and recommended for use with
incomplete mark data. The semiparametric methods make two key assumptions:
(i) the time-to-event is assumed to be conditionally independent of the
mark given treatment, and (ii) the weight function in the semiparametric
density ratio/biased sampling model is assumed to be exponential.
Diagnostic testing procedures for evaluating validity of both assumptions
are implemented. Summary and plotting functions are provided for
estimation and inferential results.

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
