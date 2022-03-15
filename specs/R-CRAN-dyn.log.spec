%global __brp_check_rpaths %{nil}
%global packname  dyn.log
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Logging for R Inspired by Configuration Driven Development

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-yaml >= 2.2.1
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-crayon >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-rlang >= 0.4.12
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-yaml >= 2.2.1
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-crayon >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-rlang >= 0.4.12

%description
A comprehensive and dynamic configuration driven logging package for R.
While there are several excellent logging solutions already in the R
ecosystem, I always feel constrained in some way by each of them. Every
project is designed differently to solve it's domain specific problem, and
ultimately the utility of a logging solution is its ability to adapt to
this design. This is the raison d'être for 'dyn.log': to provide a modular
design, template mechanics and a configuration-based integration model, so
that the logger can integrate deeply into your design, even though it
knows nothing about it.

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
