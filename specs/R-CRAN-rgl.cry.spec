%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rgl.cry
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          'cry' and 'rgl' — Applications in Crystallography

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cry 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-utils 
Requires:         R-CRAN-cry 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rgl 
Requires:         R-utils 

%description
Visualizing crystal structures and selected area electron diffraction
(SAED) patterns.  It provides functions cry_demo() and dp_demo() to load a
file in 'CIF' (Crystallographic Information Framework) formats and display
crystal structures and electron diffraction patterns.  The function
dp_demo() also performs simple simulation of powder X-ray diffraction
(PXRD) patterns, and the results can be saved to a file in the working
directory.  The package has been tested on several platforms, including
Linux on 'Crostini' with a Core™ m3-8100Y Chromebook, I found that even on
this low-powered platform, the performance was acceptable. T. Hanashima
(2001) <https://www2.kek.jp/imss/pf/tools/sasaki/sinram/sinram.html> Todd
Helmenstine (2019)
<https://sciencenotes.org/molecule-atom-colors-cpk-colors/> Wikipedia
contributors (2023)
<https://en.wikipedia.org/w/index.php?title=Atomic_radius&oldid=1179864711>.

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
