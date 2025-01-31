%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dplR
%global packver   1.7.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.8
Release:          1%{?dist}%{?buildtag}
Summary:          Dendrochronology Program Library in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-XML >= 2.1.0
BuildRequires:    R-CRAN-R.utils >= 1.32.1
BuildRequires:    R-CRAN-Matrix >= 1.0.3
BuildRequires:    R-CRAN-matrixStats >= 0.50.2
BuildRequires:    R-CRAN-stringr >= 0.4
BuildRequires:    R-CRAN-digest >= 0.2.3
BuildRequires:    R-CRAN-stringi >= 0.2.3
BuildRequires:    R-CRAN-lattice >= 0.13.6
BuildRequires:    R-CRAN-png >= 0.1.2
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-XML >= 2.1.0
Requires:         R-CRAN-R.utils >= 1.32.1
Requires:         R-CRAN-Matrix >= 1.0.3
Requires:         R-CRAN-matrixStats >= 0.50.2
Requires:         R-CRAN-stringr >= 0.4
Requires:         R-CRAN-digest >= 0.2.3
Requires:         R-CRAN-stringi >= 0.2.3
Requires:         R-CRAN-lattice >= 0.13.6
Requires:         R-CRAN-png >= 0.1.2
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lifecycle 

%description
Perform tree-ring analyses such as detrending, chronology building, and
cross dating.  Read and write standard file formats used in
dendrochronology.

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
