%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpatialML
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Machine Learning

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0
BuildRequires:    R-CRAN-randomForest >= 4.7
BuildRequires:    R-CRAN-ranger >= 0.15.1
Requires:         R-CRAN-caret >= 6.0
Requires:         R-CRAN-randomForest >= 4.7
Requires:         R-CRAN-ranger >= 0.15.1

%description
Implements a spatial extension of the random forest algorithm (Georganos
et al. (2019) <doi:10.1080/10106049.2019.1595177>). Allows for a
geographically weighted random forest regression including a function to
find the optical bandwidth. (Georganos and Kalogirou (2022)
<https://www.mdpi.com/2220-9964/11/9/471>).

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
