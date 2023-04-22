%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chisquare
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Chi-Square and G-Square Test of Independence, Residual Analysis, and Measures of Categorical Association

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics >= 4.2.0
BuildRequires:    R-stats >= 4.2.0
BuildRequires:    R-CRAN-gt >= 0.3.1
Requires:         R-graphics >= 4.2.0
Requires:         R-stats >= 4.2.0
Requires:         R-CRAN-gt >= 0.3.1

%description
Provides the facility to perform the chi-square and G-square test of
independence, calculates permutation-based p value, and provides measures
of association such as Phi, odds ratio with 95 percent CI and p value,
adjusted contingency coefficient, Cramer's V and 95 percent CI,
bias-corrected Cramer's V, Cohen's w, Goodman-Kruskal's lambda, gamma and
its p value, and tau, Cohen's k and its 95 percent CI. It also calculates
standardized, moment-corrected standardized, and adjusted standardized
residuals, and their significance. Different outputs are returned in
nicely formatted tables.

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
