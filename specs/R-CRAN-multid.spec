%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multid
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Difference Between Two Groups

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.88
BuildRequires:    R-CRAN-glmnet >= 4.1.2
BuildRequires:    R-stats >= 4.0.2
BuildRequires:    R-CRAN-emmeans >= 1.6.3
BuildRequires:    R-CRAN-pROC >= 1.18.0
BuildRequires:    R-CRAN-lme4 >= 1.1.27.1
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-lavaan >= 0.6.9
Requires:         R-CRAN-quantreg >= 5.88
Requires:         R-CRAN-glmnet >= 4.1.2
Requires:         R-stats >= 4.0.2
Requires:         R-CRAN-emmeans >= 1.6.3
Requires:         R-CRAN-pROC >= 1.18.0
Requires:         R-CRAN-lme4 >= 1.1.27.1
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-lavaan >= 0.6.9

%description
Estimation of multivariate differences between two groups (e.g.,
multivariate sex differences) with regularized regression methods and
predictive approach. See Lönnqvist & Ilmarinen (2021)
<doi:10.1007/s11109-021-09681-2> and Ilmarinen et al. (2022)
<doi:10.1177/08902070221088155>. Includes tools that help in understanding
difference score reliability, predictions of difference score variables,
conditional intra-class correlations, and heterogeneity of variance
estimates. Package development was supported by the Academy of Finland
research grant 338891.

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
