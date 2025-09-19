%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinystate
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Customization of Shiny Bookmarkable State

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 0.14
BuildRequires:    R-CRAN-archive 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-pins 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-shiny >= 0.14
Requires:         R-CRAN-archive 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-pins 
Requires:         R-CRAN-R6 

%description
Enhance the bookmarkable state feature of 'shiny' with additional
customization such as storage location and storage repositories leveraging
the 'pins' package.

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
