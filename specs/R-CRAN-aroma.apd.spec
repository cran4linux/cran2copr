%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aroma.apd
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Probe-Level Data File Format Used by 'aroma.affymetrix' [deprecated]

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.2.0
BuildRequires:    R-CRAN-R.methodsS3 >= 1.7.1
BuildRequires:    R-CRAN-R.oo >= 1.23.0
BuildRequires:    R-CRAN-R.huge >= 0.9.0
Requires:         R-CRAN-R.utils >= 2.2.0
Requires:         R-CRAN-R.methodsS3 >= 1.7.1
Requires:         R-CRAN-R.oo >= 1.23.0
Requires:         R-CRAN-R.huge >= 0.9.0

%description
DEPRECATED. Do not start building new projects based on this package. (The
(in-house) APD file format was initially developed to store Affymetrix
probe-level data, e.g. normalized CEL intensities.  Chip types can be
added to APD file and similar to methods in the affxparser package, this
package provides methods to read APDs organized by units (probesets).  In
addition, the probe elements can be arranged optimally such that the
elements are guaranteed to be read in order when, for instance, data is
read unit by unit.  This speeds up the read substantially.  This package
is supporting the Aroma framework and should not be used elsewhere.)

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
