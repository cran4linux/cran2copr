%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  linreg
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Regression and Model Selection Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-lmtest 
Requires:         R-stats 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-car 
Requires:         R-CRAN-lmtest 

%description
Provides a comprehensive framework for linear regression modeling and
associated statistical analysis. The package implements methods for
correlation analysis, including computation of correlation matrices with
corresponding significance levels and visualization via correlation
heatmaps. It supports estimation of multiple linear regression models,
along with automated model selection through backward elimination
procedures based on statistical significance criteria. In addition, the
package offers a suite of diagnostic tools to assess key assumptions of
linear regression, including multicollinearity using variance inflation
factors, heteroscedasticity using the Goldfeld-Quandt test, and normality
of residuals using the Shapiro-Wilk test. These functionalities, as
described in Draper and Smith (1998) <doi:10.1002/9781118625590>, are
designed to facilitate robust model building, evaluation, and
interpretation in applied statistical and data analytical contexts.

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
