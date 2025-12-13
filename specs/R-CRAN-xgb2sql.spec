%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xgb2sql
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Convert Trained 'XGBoost' Model to SQL Query

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xgboost >= 3.1.2.1
BuildRequires:    R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-xgboost >= 3.1.2.1
Requires:         R-CRAN-data.table >= 1.12.0

%description
This tool enables in-database scoring of 'XGBoost' models built in R, by
translating trained model objects into SQL query. 'XGBoost'
<https://github.com/dmlc/xgboost> provides parallel tree boosting (also
known as gradient boosting machine, or GBM) algorithms in a highly
efficient, flexible and portable way. GBM algorithm is introduced by
Friedman (2001) <doi:10.1214/aos/1013203451>, and more details on
'XGBoost' can be found in Chen & Guestrin (2016)
<doi:10.1145/2939672.2939785>.

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
