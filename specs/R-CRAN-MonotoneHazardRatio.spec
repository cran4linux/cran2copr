%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MonotoneHazardRatio
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Estimation and Inference of a Monotone Hazard Ratio Function

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-survival 

%description
Nonparametric estimation and inference of a non-decreasing monotone hazard
ratio from a right censored survival dataset.  The estimator is based on a
generalized Grenander typed estimator, and the inference procedure relies
on direct plugin estimation of a first order derivative.  More details
please refer to the paper "Nonparametric inference under a monotone hazard
ratio order" by Y. Wu and T. Westling (2023) <doi:10.1214/23-EJS2173>.

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
