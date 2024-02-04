%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AER
%global packver   1.2-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.12
Release:          1%{?dist}%{?buildtag}
Summary:          Applied Econometrics with R

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich >= 2.4.0
BuildRequires:    R-CRAN-survival >= 2.37.5
BuildRequires:    R-CRAN-car >= 2.0.19
BuildRequires:    R-CRAN-Formula >= 0.2.0
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-stats 
Requires:         R-CRAN-sandwich >= 2.4.0
Requires:         R-CRAN-survival >= 2.37.5
Requires:         R-CRAN-car >= 2.0.19
Requires:         R-CRAN-Formula >= 0.2.0
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-zoo 
Requires:         R-stats 

%description
Functions, data sets, examples, demos, and vignettes for the book
Christian Kleiber and Achim Zeileis (2008), Applied Econometrics with R,
Springer-Verlag, New York. ISBN 978-0-387-77316-2.
<doi:10.1007/978-0-387-77318-6> (See the vignette "AER" for a package
overview.)

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
