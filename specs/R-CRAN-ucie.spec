%global __brp_check_rpaths %{nil}
%global packname  ucie
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mapping 3D Data into CIELab Color Space

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-ptinpoly 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-remotes 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-ptinpoly 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-remotes 

%description
Returns a data frame with the names of the input data points and hex
colors (or CIELab coordinates). Data can be mapped to colors for use in
data visualization. It optimally maps data points into a polygon that
represents the CIELab colour space. Since Euclidean distance approximates
relative perceptual differences in CIELab color space, the result is a
color encoding that aims to capture much of the structure of the original
data.

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
