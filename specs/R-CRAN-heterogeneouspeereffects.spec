%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  heterogeneouspeereffects
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Heterogeneous Peer Effect

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Heterogeneous Peer Effect Package provides two-step Generalized Method of
Moments (GMM) estimators for heterogeneous peer effects in group-level
treatment models developed by Pasquier, Rossi and Wang (2026)
<https://crest.science/wp-content/uploads/2026/09/2026-11.pdf>. The
package separates the direct effect of treatment from within-group and
between-group spillover effects, using a cross-fitted, semiparametric
approach that leaves the propensity score unspecified and estimates it
nonparametrically. Two identification settings are implemented: one in
which eligibility for treatment coincides with group identity, and one in
which identity is orthogonal to eligibility, allowing peer effects to
differ across subgroups (e.g. by gender). Point estimates, standard
errors, and test statistics are returned for the direct effect and for
each within- and between-group peer effect.

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
