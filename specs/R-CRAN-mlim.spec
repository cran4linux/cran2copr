%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlim
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Single and Multiple Imputation with Automated Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3.2
BuildRequires:    R-CRAN-h2o >= 3.34.0.0
BuildRequires:    R-CRAN-md.log >= 0.2.0
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-missRanger 
BuildRequires:    R-CRAN-memuse 
Requires:         R-CRAN-curl >= 4.3.2
Requires:         R-CRAN-h2o >= 3.34.0.0
Requires:         R-CRAN-md.log >= 0.2.0
Requires:         R-CRAN-mice 
Requires:         R-CRAN-missRanger 
Requires:         R-CRAN-memuse 

%description
Machine learning algorithms have been used for performing single missing
data imputation and most recently, multiple imputations. However, this is
the first attempt for using automated machine learning algorithms for
performing both single and multiple imputation. Automated machine learning
is a procedure for fine-tuning the model automatic, performing a random
search for a model that results in less error, without overfitting the
data. The main idea is to allow the model to set its own parameters for
imputing each variable separately instead of setting fixed predefined
parameters to impute all variables of the dataset. Using automated machine
learning, the package fine-tunes an Elastic Net (default) or Gradient
Boosting, Random Forest, Deep Learning, Extreme Gradient Boosting, or
Stacked Ensemble machine learning model (from one or a combination of
other supported algorithms) for imputing the missing observations. This
procedure has been implemented for the first time by this package and is
expected to outperform other packages for imputing missing data that do
not fine-tune their models. The multiple imputation is implemented via
bootstrapping without letting the duplicated observations to harm the
cross-validation procedure, which is the way imputed variables are
evaluated. Most notably, the package implements automated procedure for
handling imputing imbalanced data (class rarity problem), which happens
when a factor variable has a level that is far more prevalent than the
other(s). This is known to result in biased predictions, hence, biased
imputation of missing data. However, the autobalancing procedure ensures
that instead of focusing on maximizing accuracy (classification error) in
imputing factor variables, a fairer procedure and imputation method is
practiced.

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
