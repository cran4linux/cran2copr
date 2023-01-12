%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmstcompsens
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Comparing Restricted Mean Survival Time as Sensitivity Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 

%description
Performs two-sample comparisons using the restricted mean survival time
(RMST) when survival curves end at different time points between groups.
This package implements a sensitivity approach that allows the threshold
timepoint tau to be specified after the longest survival time in the
shorter survival group. Two kinds of between-group contrast estimators
(the difference in RMST and the ratio of RMST) are computed: Uno et
al(2014)<doi:10.1200/JCO.2014.55.2208>, Uno et
al(2022)<https://CRAN.R-project.org/package=survRM2>, Ueno and
Morita(2023)<doi:10.1007/s43441-022-00484-z>.

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
