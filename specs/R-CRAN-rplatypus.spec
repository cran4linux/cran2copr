%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rplatypus
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computer Vision for Medical Imaging

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.41
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-reticulate >= 1.41
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-CRAN-rlang 
Requires:         R-tools 
Requires:         R-utils 

%description
Semantic segmentation and object detection for medical images, from a
folder of pictures to a trained model and a figure, in a handful of lines
or one configuration file. Architectures, losses and training run on
'PyTorch' through 'pyplatypus', a 'Python' package which is installed and
isolated automatically; nothing has to be set up by hand. R keeps the
parts that make an analysis fast - reading and combining masks, drawing
boxes, plotting, comparing models.

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
