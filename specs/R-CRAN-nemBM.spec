%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nemBM
%global packver   1.00.00
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.00.00
Release:          1%{?dist}%{?buildtag}
Summary:          Using Network Evolution Models to Generate Networks with Selected Blockmodel Type

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-blockmodeling 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-blockmodeling 

%description
To study network evolution models and different blockmodeling approaches.
Various functions enable generating (temporal) networks with a selected
blockmodel type, taking into account selected local network mechanisms.
The development of this package is financially supported by the Slovenian
Research Agency (www.arrs.gov.si) within the research programs P5-0168 and
the research project J7-8279 (Blockmodeling multilevel and temporal
networks).

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
