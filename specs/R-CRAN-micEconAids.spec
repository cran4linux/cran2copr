%global __brp_check_rpaths %{nil}
%global packname  micEconAids
%global packver   0.6-20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.20
Release:          1%{?dist}%{?buildtag}
Summary:          Demand Analysis with the Almost Ideal Demand System (AIDS)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-systemfit >= 1.1.12
BuildRequires:    R-CRAN-micEcon >= 0.6.0
BuildRequires:    R-CRAN-miscTools >= 0.6.0
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-stats 
Requires:         R-CRAN-systemfit >= 1.1.12
Requires:         R-CRAN-micEcon >= 0.6.0
Requires:         R-CRAN-miscTools >= 0.6.0
Requires:         R-CRAN-lmtest 
Requires:         R-stats 

%description
Functions and tools for analysing consumer demand with the Almost Ideal
Demand System (AIDS) suggested by Deaton and Muellbauer (1980).

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
