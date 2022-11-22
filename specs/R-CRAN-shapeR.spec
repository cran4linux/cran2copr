%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shapeR
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Collection and Analysis of Otolith Shape Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-pixmap 
BuildRequires:    R-CRAN-wavethresh 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-pixmap 
Requires:         R-CRAN-wavethresh 
Requires:         R-methods 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-MASS 

%description
Studies otolith shape variation among fish populations. Otoliths are
calcified structures found in the inner ear of teleost fish and their
shape has been known to vary among several fish populations and stocks,
making them very useful in taxonomy, species identification and to study
geographic variations. The package extends previously described software
used for otolith shape analysis by allowing the user to automatically
extract closed contour outlines from a large number of images, perform
smoothing to eliminate pixel noise described in Haines and Crampton (2000)
<doi:10.1111/1475-4983.00148>, choose from conducting either a Fourier or
wavelet see Gençay et al (2001) <doi:10.1016/S0378-4371(00)00463-5>
transform to the outlines and visualize the mean shape. The output of the
package are independent Fourier or wavelet coefficients which can be
directly imported into a wide range of statistical packages in R. The
package might prove useful in studies of any two dimensional objects.

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
