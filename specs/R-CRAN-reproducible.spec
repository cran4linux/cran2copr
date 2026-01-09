%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reproducible
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Enhance Reproducibility of R Code

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       /usr/bin/unrar
BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-CRAN-fpCompare 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-lobstr 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-cli 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-filelock 
Requires:         R-CRAN-fpCompare 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-lobstr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
A collection of high-level, machine- and OS-independent tools for making
reproducible and reusable content in R. The two workhorse functions are
'Cache()' and 'prepInputs()'. 'Cache()' allows for nested caching, is
robust to environments and objects with environments (like functions), and
deals with some classes of file-backed R objects e.g., from 'terra' and
'raster' packages. Both functions have been developed to be foundational
components of data retrieval and processing in continuous workflow
situations. In both functions, efforts are made to make the first and
subsequent calls of functions have the same result, but faster at
subsequent times by way of checksums and digesting. Several features are
still under development, including cloud storage of cached objects
allowing for sharing between users. Several advanced options are
available, see '?reproducibleOptions()'.

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
