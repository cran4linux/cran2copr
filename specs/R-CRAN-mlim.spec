%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlim
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Imputation with Automated Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3.0
BuildRequires:    R-CRAN-h2o >= 3.34.0.0
BuildRequires:    R-CRAN-md.log >= 0.2.0
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-missRanger 
BuildRequires:    R-CRAN-memuse 
Requires:         R-CRAN-curl >= 4.3.0
Requires:         R-CRAN-h2o >= 3.34.0.0
Requires:         R-CRAN-md.log >= 0.2.0
Requires:         R-CRAN-mice 
Requires:         R-CRAN-missRanger 
Requires:         R-CRAN-memuse 

%description
Using automated machine learning, the package fine-tunes an Elastic Net
(default) or Gradient Boosting, Random Forest, Deep Learning, Extreme
Gradient Boosting, or Stacked Ensemble machine learning model for imputing
the missing observations of each variable. This procedure has been
implemented for the first time by this package and is expected to
outperform other packages for imputing missing data that do not fine-tune
their models. The main idea is to allow the model to set its own
parameters for imputing each variable instead of setting fixed predefined
parameters to impute all variables of the dataset.

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
