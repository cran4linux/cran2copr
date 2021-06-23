%global __brp_check_rpaths %{nil}
%global packname  magicaxis
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Pretty Scientific Plotting with Minor-Tick and Log Minor-Tick Support

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-celestial >= 1.4.1
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RANN 
Requires:         R-CRAN-celestial >= 1.4.1
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-RANN 

%description
Functions to make useful (and pretty) plots for scientific plotting.
Additional plotting features are added for base plotting, with particular
emphasis on making attractive log axis plots.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
