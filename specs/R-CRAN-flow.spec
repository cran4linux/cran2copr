%global __brp_check_rpaths %{nil}
%global packname  flow
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          View and Browse Code Using Flow Diagrams

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nomnoml 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-webshot 
BuildRequires:    R-CRAN-styler 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-nomnoml 
Requires:         R-utils 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-webshot 
Requires:         R-CRAN-styler 
Requires:         R-methods 
Requires:         R-CRAN-here 
Requires:         R-CRAN-lifecycle 

%description
Visualize as flow diagrams the logic of functions, expressions or scripts
in a static way or when running a call, and ease debugging. Advanced
features include analogs to 'debug' and 'debugonce' to target specific
functions to draw, an utility to draw the calls used in the tests of the
package in a markdown report, and an utility to draw all the functions of
one package in a markdown report.

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
