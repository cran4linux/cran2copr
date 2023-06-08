%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RelimpPCR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Relative Importance PCA Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-relaimpo 
BuildRequires:    R-CRAN-Rmisc 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-logger 
Requires:         R-CRAN-relaimpo 
Requires:         R-CRAN-Rmisc 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-logger 

%description
Performs Principal Components Analysis (also known as PCA) dimensionality
reduction in the context of a linear regression. In most cases, PCA
dimensionality reduction is performed independent of the response variable
for a regression. This captures the majority of the variance of the
model's predictors, but may not actually be the optimal dimensionality
reduction solution for a regression against the response variable. An
alternative method, optimized for a regression against the response
variable, is to use both PCA and a relative importance measure. This
package applies PCA to a given data frame of predictors, and then
calculates the relative importance of each PCA factor against the response
variable. It outputs ordered factors that are optimized for model fit. By
performing dimensionality reduction with this method, an individual can
achieve a the same r-squared value as performing just PCA, but with fewer
PCA factors. References: Yuri Balasanov (2017) <https://ilykei.com>.

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
