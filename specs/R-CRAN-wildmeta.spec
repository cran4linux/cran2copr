%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wildmeta
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster Wild Bootstrapping for Meta-Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clubSandwich >= 0.5.4
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-robumeta 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-stats 
Requires:         R-CRAN-clubSandwich >= 0.5.4
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-robumeta 
Requires:         R-CRAN-metafor 
Requires:         R-stats 

%description
Conducts single coefficient tests and multiple-contrast hypothesis tests
of meta-regression models using cluster wild bootstrapping, based on
methods examined in Joshi, Pustejovsky, and Beretvas (2022)
<DOI:10.1002/jrsm.1554>.

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
