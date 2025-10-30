%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chisquare
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Chi-Square and G-Square Test of Independence, Power and Residual Analysis, Measures of Categorical Association

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gt >= 0.3.1
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-gt >= 0.3.1
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides the facility to perform the chi-square and G-square test of
independence, calculates the retrospective power of the traditional
chi-square test, compute permutation and Monte Carlo p-value, and provides
measures of association for tables of any size such as Phi, Phi corrected,
odds ratio with 95 percent CI and p-value, Yule' Q and Y, adjusted
contingency coefficient, Cramer's V, V corrected, V standardised,
bias-corrected V, W, Cohen's w, Goodman-Kruskal's lambda, and tau. It also
calculates standardised, moment-corrected standardised, and adjusted
standardised residuals, and their significance, as well as the Quetelet
Index, IJ association factor, and adjusted standardised counts. It also
computes the chi-square-maximising version of the input table. Different
outputs are returned in nicely formatted tables.

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
