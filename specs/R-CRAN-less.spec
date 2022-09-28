%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  less
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Learning with Subset Stacking

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-wordspace 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-MLmetrics 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-wordspace 

%description
"Learning with Subset Stacking" is a supervised learning algorithm that is
based on training many local estimators on subsets of a given dataset, and
then passing their predictions to a global estimator. You can find the
details about LESS in our manuscript at <arXiv:2112.06251>.

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
