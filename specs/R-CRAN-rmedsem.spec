%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmedsem
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Mediation Analysis for SEMs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Conducts mediation analysis for structural equation models (SEM) estimated
with 'lavaan', 'blavaan', 'cSEM', or 'modsem'. Implements the Baron and
Kenny (1986) <doi:10.1037/0022-3514.51.6.1173> and Zhao, Lynch & Chen
(2010) <doi:10.1086/651257> approaches to determine the presence and type
of mediation. Supports covariance-based SEM, partial least squares SEM,
Bayesian SEM, and moderated mediation and mediated moderation models.
Tests indirect effects with the Sobel, Delta, Monte-Carlo, and bootstrap
methods or, for Bayesian models, with posterior summaries and equal-tailed
or highest density credible intervals. Reports the effect size measures
RIT, RID, and Upsilon of Lachowicz, Preacher and Kelley (2018)
<doi:10.1037/met0000165>. Results can be summarized, extracted with
standard methods such as summary(), coef() and confint(), and plotted.

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
