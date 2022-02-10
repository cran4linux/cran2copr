%global __brp_check_rpaths %{nil}
%global packname  gunsales
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis of Monthly Background Checks of Gun Purchases

License:          Apache License (== 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-seasonal 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-x13binary 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-seasonal 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-x13binary 

%description
Statistical analysis of monthly background checks of gun purchases for the
New York Times story "What Drives Gun Sales: Terrorism, Obama and Calls
for Restrictions" at
<http://www.nytimes.com/interactive/2015/12/10/us/gun-sales-terrorism-obama-restrictions.html?>
is provided.

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
