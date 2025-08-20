%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaSVR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Support Vector Regression with Metaheuristic Algorithms Optimization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-hms 
Requires:         R-CRAN-e1071 
Requires:         R-stats 
Requires:         R-CRAN-hms 

%description
Provides a hybrid modeling framework combining Support Vector Regression
(SVR) with metaheuristic optimization algorithms, including the Archimedes
Optimization Algorithm (AO) (Hashim et al. (2021)
<doi:10.1007/s10489-020-01893-z>), Coot Bird Optimization (CBO) (Naruei &
Keynia (2021) <doi:10.1016/j.eswa.2021.115352>), and their hybrid (AOCBO),
as well as several others such as Harris Hawks Optimization (HHO) (Heidari
et al. (2019) <doi:10.1016/j.future.2019.02.028>), Gray Wolf Optimizer
(GWO) (Mirjalili et al. (2014) <doi:10.1016/j.advengsoft.2013.12.007>),
Ant Lion Optimization (ALO) (Mirjalili (2015)
<doi:10.1016/j.advengsoft.2015.01.010>), and Enhanced Harris Hawk
Optimization with Coot Bird Optimization (EHHOCBO) (Cui et al. (2023)
<doi:10.32604/cmes.2023.026019>). The package enables automatic tuning of
SVR hyperparameters (cost, gamma, and epsilon) to enhance prediction
performance. Suitable for regression tasks in domains such as renewable
energy forecasting and hourly data prediction. For more details about
implementation and parameter bounds see: Setiawan et al. (2021)
<doi:10.1016/j.procs.2020.12.003> and Liu et al. (2018)
<doi:10.1155/2018/6076475>.

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
