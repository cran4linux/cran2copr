%global __brp_check_rpaths %{nil}
%global packname  iscoCrosswalks
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Crosswalks Between Classifications of Occupations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-labourR 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-labourR 
Requires:         R-CRAN-Rdpack 

%description
Allows the user to perform approximate matching between the occupational
classifications using concordances provided by the Institute for
Structural Research and Faculty of Economics, University of Warsaw,
<doi:10.1111/ecot.12145>. The crosswalks offer a complete step-by-step
mapping of Standard Occupational Classification (2010) data to the
International Standard Classification of Occupations (2008). We propose a
mapping method based on the aforementioned research that converts
measurements to the smallest possible unit of the target taxonomy, and
then performs an aggregation/estimate to the requested degree Occupational
Hierarchical level.

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
