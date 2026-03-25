%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stopmotion
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Build Stop Motion Animations from Image Sequences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-checkmate 

%description
A pipeline-friendly toolkit for assembling stop motion animations from
sequences of still images. Provides functions to read image directories,
restructure frame sequences (duplicate, splice, arrange), apply per-frame
pixel transformations (rotate, wiggle, flip, flop, blur, scale, crop,
trim, border, background), and export the result as a GIF. All
transformation functions accept a 'frames' argument to target any subset
of frames, bridging the gap between 'magick' functions that operate on an
entire image stack and fine-grained stop motion editing. Image processing
is performed via 'ImageMagick Studio LLC' (2024)
<https://imagemagick.org>.

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
