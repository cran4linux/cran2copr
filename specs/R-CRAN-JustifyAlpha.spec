%global __brp_check_rpaths %{nil}
%global packname  JustifyAlpha
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Justifying Alpha Levels for Hypothesis Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-Superpower 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-qpdf 
Requires:         R-stats 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-Superpower 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-qpdf 

%description
Functions to justify alpha levels for statistical hypothesis tests by
avoiding Lindley's paradox, or by minimizing or balancing error rates. For
more information about the package please read the following: Maier &
Lakens (2021) <doi:10.31234/osf.io/ts4r6>).

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
