%global __brp_check_rpaths %{nil}
%global packname  MLDataR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Machine Learning Datasets for Supervised Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ConfusionTableR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-ConfusionTableR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-caret 

%description
Contains a collection of datasets for working with machine learning tasks.
It will contain datasets for supervised machine learning Jiang
(2020)<doi:10.1016/j.beth.2020.05.002> and will include datasets for
classification and regression. The aim of this package is to use data
generated around health and other domains.

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
