%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vsmi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Selection for Multiple Imputed Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.60
BuildRequires:    R-CRAN-mice >= 3.16.0
BuildRequires:    R-CRAN-Matrix >= 1.6.1.1
BuildRequires:    R-CRAN-qif >= 1.5
Requires:         R-CRAN-MASS >= 7.3.60
Requires:         R-CRAN-mice >= 3.16.0
Requires:         R-CRAN-Matrix >= 1.6.1.1
Requires:         R-CRAN-qif >= 1.5

%description
Penalized weighted least-squares estimate for variable selection on
correlated multiply imputed data and penalized estimating equations for
generalized linear models with multiple imputation. Reference: Li, Y.,
Yang, H., Yu, H., Huang, H., Shen, Y*. (2023) "Penalized estimating
equations for generalized linear models with multiple imputation",
<doi:10.1214/22-AOAS1721>. Li, Y., Yang, H., Yu, H., Huang, H., Shen, Y*.
(2023) "Penalized weighted least-squares estimate for variable selection
on correlated multiply imputed data", <doi:10.1093/jrsssc/qlad028>.

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
