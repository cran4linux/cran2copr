%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpTe2M
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Modeling and Monitoring of Spatio-Temporal Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 

%description
Spatio-temporal data have become increasingly popular in many research
fields. Such data often have complex structures that are difficult to
describe and estimate. This package provides reliable tools for modeling
complicated spatio-temporal data. It also includes tools of online process
monitoring to detect possible change-points in a spatio-temporal process
over time. More specifically, the package implements the spatio-temporal
mean estimation procedure described in Yang and Qiu (2018)
<doi:10.1002/sim.7622>, the spatio-temporal covariance estimation
procedure discussed in Yang and Qiu (2019) <doi:10.1002/sim.8315>, the
three-step method for the joint estimation of spatio-temporal mean and
covariance functions suggested by Yang and Qiu (2022)
<doi:10.1007/s10463-021-00787-2>, the spatio-temporal disease surveillance
method discussed in Qiu and Yang (2021) <doi:10.1002/sim.9150> that can
accommodate the covariate effect, the spatial-LASSO-based process
monitoring method proposed by Qiu and Yang (2022)
<doi:10.1080/00224065.2022.2081104>, and the online spatio-temporal
disease surveillance method described in Yang and Qiu (2020)
<doi:10.1080/24725854.2019.1696496>.

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
