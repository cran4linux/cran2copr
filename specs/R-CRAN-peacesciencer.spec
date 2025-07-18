%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  peacesciencer
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools and Data for Quantitative Peace Science Research

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stevemisc >= 1.6.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-isard 
Requires:         R-CRAN-stevemisc >= 1.6.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-isard 

%description
These are useful tools and data sets for the study of quantitative peace
science. The goal for this package is to include tools and data sets for
doing original research that mimics well what a user would have to
previously get from a software package that may not be well-sourced or
well-supported. Those software bundles were useful the extent to which
they encourage replications of long-standing analyses by starting the
data-generating process from scratch. However, a lot of the functionality
can be done relatively quickly and more transparently in the R programming
language.

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
