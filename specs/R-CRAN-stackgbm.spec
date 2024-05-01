%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stackgbm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stacked Gradient Boosting Machines

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rlang 

%description
A minimalist implementation of model stacking by Wolpert (1992)
<doi:10.1016/S0893-6080(05)80023-1> for boosted tree models. A classic,
two-layer stacking model is implemented, where the first layer generates
features using gradient boosting trees, and the second layer employs a
logistic regression model that uses these features as inputs. Utilities
for training the base models and parameters tuning are provided, allowing
users to experiment with different ensemble configurations easily. It aims
to provide a simple and efficient way to combine multiple gradient
boosting models to improve predictive model performance and robustness.

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
