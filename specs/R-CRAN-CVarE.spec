%global packname  CVarE
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Variance Estimator for Sufficient Dimension Reduction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mda 
Requires:         R-stats 
Requires:         R-CRAN-mda 

%description
Implementation of the CVE (Conditional Variance Estimation) method
proposed by Fertl, L. and Bura, E. (2021) <arXiv:2102.08782> and the ECVE
(Ensemble Conditional Variance Estimation) method introduced in Fertl, L.
and Bura, E. (2021) <arXiv:2102.13435>. CVE and ECVE are sufficient
dimension reduction methods in regressions with continuous response and
predictors. CVE applies to general additive error regression models while
ECVE generalizes to non-additive error regression models. They operate
under the assumption that the predictors can be replaced by a lower
dimensional projection without loss of information. It is a semiparametric
forward regression model based exhaustive sufficient dimension reduction
estimation method that is shown to be consistent under mild assumptions.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
