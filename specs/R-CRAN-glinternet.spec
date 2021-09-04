%global __brp_check_rpaths %{nil}
%global packname  glinternet
%global packver   1.0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.12
Release:          1%{?dist}%{?buildtag}
Summary:          Learning Interactions via Hierarchical Group-Lasso Regularization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Group-Lasso INTERaction-NET. Fits linear pairwise-interaction models that
satisfy strong hierarchy: if an interaction coefficient is estimated to be
nonzero, then its two associated main effects also have nonzero estimated
coefficients. Accommodates categorical variables (factors) with arbitrary
numbers of levels, continuous variables, and combinations thereof.
Implements the machinery described in the paper "Learning interactions via
hierarchical group-lasso regularization" (JCGS 2015, Volume 24, Issue 3).
Michael Lim & Trevor Hastie (2015) <DOI:10.1080/10618600.2014.938812>.

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
