%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  politicsR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculating Political System Metrics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ineq 
Requires:         R-CRAN-ineq 

%description
A toolbox to facilitate the calculation of political system indicators for
researchers. This package offers a variety of basic indicators related to
electoral systems, party systems, elections, and parliamentary studies, as
well as others. Main references are: Loosemore and Hanby (1971)
<doi:10.1017/S000712340000925X>; Gallagher (1991)
<doi:10.1016/0261-3794(91)90004-C>; Laakso and Taagepera (1979)
<doi:10.1177/001041407901200101>; Rae (1968)
<doi:10.1177/001041406800100305>; Hirschmaņ (1945) <ISBN:0-520-04082-1>;
Kesselman (1966) <doi:10.2307/1953769>; Jones and Mainwaring (2003)
<doi:10.1177/13540688030092002>; Rice (1925) <doi:10.2307/2142407>;
Pedersen (1979) <doi:10.1111/j.1475-6765.1979.tb01267.x>; SANTOS (2002)
<ISBN:85-225-0395-8>.

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
