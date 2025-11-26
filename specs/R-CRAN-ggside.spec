%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggside
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Side Grammar Graphics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-grid 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-lifecycle 

%description
The grammar of graphics as shown in 'ggplot2' has provided an expressive
API for users to build plots. 'ggside' extends 'ggplot2' by allowing users
to add graphical information about one of the main panel's axis using a
familiar 'ggplot2' style API with tidy data. This package is particularly
useful for visualizing metadata on a discrete axis, or summary graphics on
a continuous axis such as a boxplot or a density distribution.

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
