%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  parttime
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Partial Datetime Handling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-vctrs >= 0.2.0
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-utils 
Requires:         R-CRAN-vctrs >= 0.2.0
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-pillar 
Requires:         R-utils 

%description
Datetimes and timestamps are invariably an imprecise notation, with any
partial representation implying some amount of uncertainty. To handle
this, 'parttime' provides classes for embedding partial missingness as a
central part of its datetime classes. This central feature allows for more
ergonomic use of datetimes for challenging datetime computation, including
calculations of overlapping date ranges, imputations, and more thoughtful
handling of ambiguity that arises from uncertain time zones. This package
was developed first and foremost with pharmaceutical applications in mind,
but aims to be agnostic to application to accommodate general use cases
just as conveniently.

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
