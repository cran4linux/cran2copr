%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  piar
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Price Index Aggregation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-CRAN-gpindex >= 0.6.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-CRAN-gpindex >= 0.6.1
Requires:         R-stats 
Requires:         R-utils 

%description
Most price indexes are made with a two-step procedure, where
period-over-period elemental indexes are first calculated for a collection
of elemental aggregates at each point in time, and then aggregated
according to a price index aggregation structure. These indexes can then
be chained together to form a time series that gives the evolution of
prices with respect to a fixed base period. This package contains a
collection of functions that revolve around this work flow, making it easy
to build standard price indexes, and implement the methods described by
Balk (2008, <doi:10.1017/CBO9780511720758>), von der Lippe (2007,
<doi:10.3726/978-3-653-01120-3>), and the CPI manual (2020,
<doi:10.5089/9781484354841.069>) for bilateral price indexes.

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
