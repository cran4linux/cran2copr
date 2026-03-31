%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  misl
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Imputation by Super Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-parsnip >= 1.2.0
BuildRequires:    R-CRAN-rsample >= 1.2.0
BuildRequires:    R-CRAN-tune >= 1.2.0
BuildRequires:    R-CRAN-future.apply >= 1.11.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-workflows >= 1.1.0
BuildRequires:    R-CRAN-recipes >= 1.0.0
BuildRequires:    R-CRAN-stacks >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-parsnip >= 1.2.0
Requires:         R-CRAN-rsample >= 1.2.0
Requires:         R-CRAN-tune >= 1.2.0
Requires:         R-CRAN-future.apply >= 1.11.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-workflows >= 1.1.0
Requires:         R-CRAN-recipes >= 1.0.0
Requires:         R-CRAN-stacks >= 1.0.0
Requires:         R-stats 
Requires:         R-utils 

%description
Performs multiple imputation of missing data using an ensemble super
learner built with the tidymodels framework. For each incomplete column, a
stacked ensemble of candidate learners is trained on a bootstrap sample of
the observed data and used to generate imputations via predictive mean
matching (continuous), probability draws (binary), or cumulative
probability draws (categorical). Supports parallelism across imputed
datasets via the future framework.

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
