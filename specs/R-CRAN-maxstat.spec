%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  maxstat
%global packver   0.7-26
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.26
Release:          1%{?dist}%{?buildtag}
Summary:          Maximally Selected Rank Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.7.0
Requires:         R-core >= 1.7.0
BuildRequires:    R-CRAN-exactRankTests >= 0.8.23
BuildRequires:    R-CRAN-mvtnorm >= 0.5.10
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-exactRankTests >= 0.8.23
Requires:         R-CRAN-mvtnorm >= 0.5.10
Requires:         R-stats 
Requires:         R-graphics 

%description
Maximally selected rank statistics with several p-value approximations.

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
