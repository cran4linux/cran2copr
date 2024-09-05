%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coffee
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Chronological Ordering for Fossils and Environmental Events

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rice >= 0.1.1
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-rice >= 0.1.1
Requires:         R-CRAN-data.table 

%description
While individual calibrated radiocarbon dates can span several centuries,
combining multiple dates together with any chronological constraints can
make a chronology much more robust and precise. This package uses Bayesian
methods to enforce the chronological ordering of radiocarbon and other
dates, for example for trees with multiple radiocarbon dates spaced at
exactly known intervals (e.g., 10 annual rings). For methods see Christen
2003 <doi:10.11141/ia.13.2>. Another example is sites where the relative
chronological position of the dates is taken into account - the ages of
dates further down a site must be older than those of dates further up
(Buck, Kenworthy, Litton and Smith 1991 <doi:10.1017/S0003598X00080534>;
Nicholls and Jones 2001 <doi:10.1111/1467-9876.00250>).

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
