%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  petrinetR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Building, Visualizing, Exporting and Replaying Petri Nets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lifecycle 

%description
Functions for the construction of Petri Nets. Petri Nets can be replayed
by firing enabled transitions. Silent transitions will be hidden by the
execution handler. Also includes functionalities for the visualization of
Petri Nets and export of Petri Nets to PNML (Petri Net Markup Language)
files.

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
