%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ptLasso
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Pretraining the Lasso

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Matrix 

%description
Implements lasso pretraining for generalized linear models for data with
grouped observations; data without grouped observations, but with
multinomial responses; data with multiple Gaussian responses; and data
with repeated measurements over time. The method fits a lasso model to an
initial dataset and then uses its support and coefficient values to guide
model fitting for a related task, which can improve performance by
leveraging larger datasets and preserve interpretability by identifying
features which are generally shared, and which are task specific. See
Craig et al. (2026) <doi:10.1093/jrsssb/qkaf050> for details. Model
fitting in this package is done with cv.glmnet() from the 'glmnet'
package, and syntax closely follows that of 'glmnet' (Friedman, Hastie and
Tibshirani (2010) <doi:10.18637/jss.v033.i01>).

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
