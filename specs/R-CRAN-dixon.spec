%global __brp_check_rpaths %{nil}
%global packname  dixon
%global packver   0.0-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Nearest Neighbour Contingency Table Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-spatstat.geom 

%description
Function to test spatial segregation and association based in contingency
table analysis of nearest neighbour counts following Dixon (2002)
<doi:10.1080/11956860.2002.11682700>. Some 'Fortran' code has been
included to the original dixon2002() function of the 'ecespa' package to
improve speed.

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
