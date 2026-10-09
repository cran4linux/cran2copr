%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  transDIF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Score Comparability for Translated and Adapted Exams

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
An adaptation-comparability workflow for small, lower-scoring and
unbalanced language groups where standard differential item functioning
(DIF) tools (Magis, Beland, Tuerlinckx and De Boeck, 2010,
<doi:10.3758/BRM.42.3.847>) break down. Calibrates the Rasch model in each
language group, links the groups robustly through the densest cluster of
items rather than assuming DIF cancels out (on anchor selection see Kopf,
Zeileis and Strobl, 2015, <doi:10.1177/0013164414529792>), detects
small-sample DIF with an empirical-Bayes spike-and-slab model and local
false discovery rates (Efron, 2004, <doi:10.1198/016214504000000089>),
quantifies whether item-level DIF accumulates into different pass rates,
explains DIF by item features to give translators actionable guidance, and
drafts a comparability report.

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
