%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autoEnsemble
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Stacked Ensemble Classifier for Severe Class Imbalance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3.0
BuildRequires:    R-CRAN-h2o >= 3.34.0.0
BuildRequires:    R-CRAN-h2otools >= 0.3
Requires:         R-CRAN-curl >= 4.3.0
Requires:         R-CRAN-h2o >= 3.34.0.0
Requires:         R-CRAN-h2otools >= 0.3

%description
A stacking solution for modeling imbalanced and severely skewed data. It
automates the process of building homogeneous or heterogeneous stacked
ensemble models by selecting "best" models according to different
criteria. In doing so, it strategically searches for and selects diverse,
high-performing base-learners to construct ensemble models optimized for
skewed data. This package is particularly useful for addressing class
imbalance in datasets, ensuring robust and effective model outcomes
through advanced ensemble strategies which aim to stabilize the model,
reduce its overfitting, and further improve its generalizability.

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
