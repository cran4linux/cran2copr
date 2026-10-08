%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  turfLP
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          TURF Analysis with Integer Linear Programming

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-highs >= 1.14.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
Requires:         R-CRAN-highs >= 1.14.0
Requires:         R-CRAN-Matrix 
Requires:         R-stats 

%description
Finds product portfolios that maximize TURF (total unduplicated reach and
frequency) with integer linear programming, following Serra (2013)
<doi:10.1016/j.foodqual.2012.10.001>. The maximum reach problem is the
maximal covering location problem of Church and ReVelle (1974)
<doi:10.1007/BF01942293>. The package solves it as an integer linear
program, so it finds exact optima without enumerating every portfolio.
Ties on reach are broken by frequency and then by the harmonic mean of the
individual product reaches. The package also finds the smallest portfolio
that reaches every reachable respondent. For related work on TURF for
large data sets, see Ennis, Fayle, and Ennis (2012)
<doi:10.1016/j.foodqual.2011.06.004>.

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
