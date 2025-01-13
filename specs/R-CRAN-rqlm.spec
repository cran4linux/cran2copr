%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rqlm
%global packver   2.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Modified Poisson and Least-Squares Regressions for Binary Outcome and Their Generalizations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-mice 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-mice 

%description
Modified Poisson and least-squares regression analyses for binary outcomes
of Zou (2004) <doi:10.1093/aje/kwh090> and Cheung (2007)
<doi:10.1093/aje/kwm223> have been standard multivariate analysis methods
to estimate risk ratio and risk difference in clinical and epidemiological
studies. This R package involves an easy-to-handle function to implement
these analyses by simple commands. Missing data analysis tools (multiple
imputation) are also involved. In addition, recent studies have shown the
ordinary robust variance estimator possibly has serious bias under small
or moderate sample size situations for these methods. This package also
provides computational tools to calculate alternative accurate confidence
intervals (Noma and Gosho (2024) <Forthcoming>).

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
