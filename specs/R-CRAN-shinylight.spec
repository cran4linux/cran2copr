%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinylight
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Web Interface to 'R' Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-grDevices >= 3.6.2
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-httpuv >= 1.5.4
BuildRequires:    R-CRAN-later >= 1.0
Requires:         R-grDevices >= 3.6.2
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-httpuv >= 1.5.4
Requires:         R-CRAN-later >= 1.0

%description
Web front end for your 'R' functions producing plots or tables. If you
have a function or set of related functions, you can make them available
over the internet through a web browser. This is the same motivation as
the 'shiny' package, but note that the development of 'shinylight' is not
in any way linked to that of 'shiny' (beyond the use of the 'httpuv'
package). You might prefer 'shinylight' to 'shiny' if you want a lighter
weight deployment with easier horizontal scaling, or if you want to
develop your front end yourself in JavaScript and HTML just using a
lightweight remote procedure call interface to your R code on the server.

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
