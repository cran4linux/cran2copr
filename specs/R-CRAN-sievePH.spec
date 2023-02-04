%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sievePH
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Sieve Analysis Methods for Proportional Hazards Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-scales 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-scales 

%description
Implements semiparametric estimation and testing procedures for a
continuous, possibly multivariate, mark-specific hazard ratio
(treatment/placebo) of an event of interest in a randomized treatment
efficacy trial with a time-to-event endpoint, as described in Juraska M
and Gilbert PB (2013), Mark-specific hazard ratio model with multivariate
continuous marks: an application to vaccine efficacy. Biometrics 69(2):328
337 <doi:10.1111/biom.12016>, and in Juraska M and Gilbert PB (2016),
Mark-specific hazard ratio model with missing multivariate marks. Lifetime
Data Analysis 22(4): 606-25 <doi:10.1007/s10985-015-9353-9>. The former
considers continuous multivariate marks fully observed in all subjects who
experience the event of interest, whereas the latter extends the previous
work to allow multivariate marks that are subject to
missingness-at-random. For models with missing marks, two estimators are
implemented based on (i) inverse probability weighting (IPW) of complete
cases, and (ii) augmentation of the IPW estimating functions by leveraging
correlations between the mark and auxiliary data to 'impute' the expected
profile score vectors for subjects with missing marks. The augmented IPW
estimator is doubly robust and recommended for use with incomplete mark
data. The methods make two key assumptions: (i) the time-to-event is
assumed to be conditionally independent of the mark given treatment, and
(ii) the weight function in the semiparametric density ratio/biased
sampling model is assumed to be exponential. Diagnostic testing procedures
for evaluating validity of both assumptions are implemented. Summary and
plotting functions are provided for estimation and inferential results.

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
