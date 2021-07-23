%global __brp_check_rpaths %{nil}
%global packname  objectProperties
%global packver   0.6.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.7
Release:          1%{?dist}%{?buildtag}
Summary:          A Factory of Self-Describing Properties

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12
Requires:         R-core >= 2.12
BuildArch:        noarch
BuildRequires:    R-CRAN-objectSignals >= 0.10.2
BuildRequires:    R-methods 
Requires:         R-CRAN-objectSignals >= 0.10.2
Requires:         R-methods 

%description
Supports the definition of sets of properties on objects. Observers can
listen to changes on individual properties or the set as a whole. The
properties are meant to be fully self-describing. In support of this,
there is a framework for defining enumerated types, as well as other
bounded types, as S4 classes.

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
