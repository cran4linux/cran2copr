%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sd2R
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stable Diffusion Image Generation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-ggmlR >= 0.5.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-ggmlR >= 0.5.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-later 
Requires:         R-CRAN-png 

%description
Provides Stable Diffusion image generation using the 'ggmlR' library, with
no 'Python' or external API dependencies. Supports text-to-image and
image-to-image generation for SD 1.x, SD 2.x, 'SDXL', Flux, and 'FLUX.2'.
A single sd_generate() function handles the entire pipeline, including
sampling and high-resolution output. Features multi-GPU support, a 'Shiny'
GUI, and runs on CPU or 'Vulkan' GPU across Linux, macOS, and Windows.

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
