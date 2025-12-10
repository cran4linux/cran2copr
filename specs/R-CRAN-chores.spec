%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chores
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Large Language Model Assistants

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.3
BuildRequires:    R-CRAN-shiny >= 1.9.1
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-ellmer >= 0.4.0
BuildRequires:    R-CRAN-streamy >= 0.2.1
BuildRequires:    R-CRAN-rstudioapi >= 0.17.1
BuildRequires:    R-CRAN-miniUI >= 0.1.1.1
Requires:         R-CRAN-cli >= 3.6.3
Requires:         R-CRAN-shiny >= 1.9.1
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-ellmer >= 0.4.0
Requires:         R-CRAN-streamy >= 0.2.1
Requires:         R-CRAN-rstudioapi >= 0.17.1
Requires:         R-CRAN-miniUI >= 0.1.1.1

%description
Provides a collection of ergonomic large language model assistants
designed to help you complete repetitive, hard-to-automate tasks quickly.
After selecting some code, press the keyboard shortcut you've chosen to
trigger the package app, select an assistant, and watch your chore be
carried out. While the package ships with a number of chore helpers for R
package development, users can create custom helpers just by writing some
instructions in a markdown file.

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
