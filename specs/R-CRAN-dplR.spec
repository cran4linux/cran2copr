%global __brp_check_rpaths %{nil}
%global packname  dplR
%global packver   1.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Dendrochronology Program Library in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2
BuildRequires:    R-CRAN-XML >= 2.1.0
BuildRequires:    R-CRAN-plyr >= 1.8
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
Requires:         R-CRAN-XML >= 2.1.0
Requires:         R-CRAN-plyr >= 1.8
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
