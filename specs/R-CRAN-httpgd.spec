%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  httpgd
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          A 'HTTP' Server Graphics Device

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cairo-devel
BuildRequires:    freetype-devel
BuildRequires:    libpng-devel
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-AsioHeaders >= 1.22.1
BuildRequires:    R-CRAN-cpp11 >= 0.2.4
BuildRequires:    R-CRAN-unigd 
Requires:         R-CRAN-unigd 

%description
A graphics device for R that is accessible via network protocols. This
package was created to make it easier to embed live R graphics in
integrated development environments and other applications. The included
'HTML/JavaScript' client (plot viewer) aims to provide a better overall
user experience when dealing with R graphics. The device asynchronously
serves graphics via 'HTTP' and 'WebSockets'.

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
