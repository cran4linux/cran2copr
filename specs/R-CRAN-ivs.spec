%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ivs
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interval Vectors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-vctrs >= 0.6.0
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-vctrs >= 0.6.0

%description
Provides a library for generic interval manipulations using a new interval
vector class. Capabilities include: locating various kinds of
relationships between two interval vectors, merging overlaps within a
single interval vector, splitting an interval vector on its overlapping
endpoints, and applying set theoretical operations on interval vectors.
Many of the operations in this package were inspired by James Allen's
interval algebra, Allen (1983) <doi:10.1145/182.358434>.

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
