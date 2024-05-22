%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shiny.blueprint
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Palantir's 'Blueprint' for 'Shiny' Apps

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny.react >= 0.4.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
Requires:         R-CRAN-shiny.react >= 0.4.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-shiny 
Requires:         R-utils 

%description
Easily use 'Blueprint', the popular 'React' library from Palantir, in your
'Shiny' app. 'Blueprint' provides a rich set of UI components for creating
visually appealing applications and is optimized for building complex,
data-dense web interfaces. This package provides most components from the
underlying library, as well as special wrappers for some components to
make it easy to use them in 'R' without writing 'JavaScript' code.

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
