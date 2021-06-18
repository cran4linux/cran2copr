%global packname  visualFields
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Visual Fields

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flip >= 2.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-CRAN-flip >= 2.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-spatstat.geom 

%description
A collection of tools for analyzing the field of vision. It provides a
framework for development and use of innovative methods for visualization,
statistical analysis, and clinical interpretation of visual-field loss and
its change over time. It is intended to be a tool for collaborative
research.

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
