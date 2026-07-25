%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  semFromKeys
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Run 'lavaan' Models from Keys Lists

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-tools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-withr 
Requires:         R-tools 

%description
Specifying 'lavaan' models manually can be time consuming when multiple
similar models are required. The 'semFromKeys' package streamlines the
process of running 'lavaan' models by generating model code from simple
keys lists and running entire collections of models at once. The package
was inspired by the process used in the code for Bainbridge, T. F.,
Ludeke, S. G., & Smillie, L. D. (2022) <doi:10.1037/pspp0000395>. The
package also optionally checks that identical models have not been run on
the same data, which saves time when code needs to be run again.

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
