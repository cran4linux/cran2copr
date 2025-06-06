%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tbm
%global packver   0.3-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Transformation Boosting Machines

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mboost >= 2.8.2
BuildRequires:    R-CRAN-mlt >= 1.0.6
BuildRequires:    R-CRAN-variables 
BuildRequires:    R-CRAN-basefun 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-coneproj 
BuildRequires:    R-methods 
Requires:         R-CRAN-mboost >= 2.8.2
Requires:         R-CRAN-mlt >= 1.0.6
Requires:         R-CRAN-variables 
Requires:         R-CRAN-basefun 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-coneproj 
Requires:         R-methods 

%description
Boosting the likelihood of conditional and shift transformation models as
introduced in <DOI:10.1007/s11222-019-09870-4>.

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
