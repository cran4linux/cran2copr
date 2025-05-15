%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  igapfill
%global packver   0.0.41
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.41
Release:          1%{?dist}%{?buildtag}
Summary:          Interface for Gap-Filling Earth Observation Datasets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.3
Requires:         R-core >= 2.15.3
BuildArch:        noarch
BuildRequires:    R-utils >= 4.5.0
BuildRequires:    R-CRAN-gtools >= 3.9.4
BuildRequires:    R-CRAN-raster >= 3.5.15
BuildRequires:    R-CRAN-terra >= 1.5.21
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-doParallel >= 1.0.17
BuildRequires:    R-CRAN-iterators >= 1.0.14
BuildRequires:    R-CRAN-gapfill >= 0.9.6.1
BuildRequires:    R-CRAN-numbers >= 0.8.5
BuildRequires:    R-CRAN-geoTS >= 0.1.8
BuildRequires:    R-CRAN-itertools >= 0.1.3
Requires:         R-utils >= 4.5.0
Requires:         R-CRAN-gtools >= 3.9.4
Requires:         R-CRAN-raster >= 3.5.15
Requires:         R-CRAN-terra >= 1.5.21
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-iterators >= 1.0.14
Requires:         R-CRAN-gapfill >= 0.9.6.1
Requires:         R-CRAN-numbers >= 0.8.5
Requires:         R-CRAN-geoTS >= 0.1.8
Requires:         R-CRAN-itertools >= 0.1.3

%description
Provides functions and a user-friendly console-based interface for the
efficient use of the main function of the R package 'gapfill' to fill
missing values of satellite images subsets. In addition to the R package
documentation, the 'gapfill' methods are introduced in Gerber et al.
(2018) <doi:10.1109/TGRS.2017.2785240>.

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
