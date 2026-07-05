%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  futureverse
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Install 'Futureverse' in One Go

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-futurize 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-progressify 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-futurize 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-progressify 
Requires:         R-CRAN-progressr 

%description
The 'Futureverse' is a set of packages for parallel and distributed
processing with the 'future' package at its core (Bengtsson, 2021,
<doi:10.32614/RJ-2021-048>). Another notable component is the 'futurize'
package (Bengtsson, 2026, <doi:10.48550/arXiv.2601.17578>) for turning
common sequential calls into parallel ones via a single function
futurize(). Similarly, the progressify() of the 'progressify' package
makes common calls to report of progress. This package is designed to make
it easy to install common 'Futureverse' packages in a single step. This
package is intended for end-users, interactive use, and R scripts.
Packages must not list it as a dependency - instead, explicitly declare
each 'Futureverse' package as a dependency as needed.

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
