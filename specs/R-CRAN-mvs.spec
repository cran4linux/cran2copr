%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mvs
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for High-Dimensional Multi-View Learning

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 1.9.8
BuildRequires:    R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-glmnet >= 1.9.8
Requires:         R-CRAN-foreach >= 1.4.4

%description
Methods for high-dimensional multi-view learning based on the multi-view
stacking (MVS) framework. For technical details on the MVS and stacked
penalized logistic regression (StaPLR) methods see Van Loon, Fokkema,
Szabo, & De Rooij (2020) <doi:10.1016/j.inffus.2020.03.007> and Van Loon
et al. (2022) <doi:10.3389/fnins.2022.830630>.

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
