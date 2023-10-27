%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vtable
%global packver   1.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Table for Variable Documentation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-sjlabelled 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-sjlabelled 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-knitr 

%description
Automatically generates HTML variable documentation including variable
names, labels, classes, value labels (if applicable), value ranges, and
summary statistics. See the vignette "vtable" for a package overview.

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
