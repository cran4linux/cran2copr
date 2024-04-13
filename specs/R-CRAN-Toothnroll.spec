%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Toothnroll
%global packver   1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Dental Tissues Landmarking Measuring and Mapping

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grDevices >= 3.5
BuildRequires:    R-graphics >= 3.5
BuildRequires:    R-CRAN-colorRamps >= 2.3
BuildRequires:    R-CRAN-compositions >= 2.0
BuildRequires:    R-CRAN-Morpho >= 2.0
BuildRequires:    R-CRAN-mgcv >= 1.8
BuildRequires:    R-CRAN-oce >= 1.1
BuildRequires:    R-CRAN-Arothron >= 1.0
BuildRequires:    R-CRAN-alphashape3d >= 1.0
BuildRequires:    R-CRAN-morphomap >= 1.0
BuildRequires:    R-CRAN-stringr >= 1.0
BuildRequires:    R-CRAN-DescTools >= 0.99
BuildRequires:    R-CRAN-geometry >= 0.4.0
BuildRequires:    R-CRAN-lattice >= 0.2
BuildRequires:    R-CRAN-Rvcg >= 0.18
BuildRequires:    R-CRAN-rgl >= 0.1
BuildRequires:    R-CRAN-vegan 
Requires:         R-grDevices >= 3.5
Requires:         R-graphics >= 3.5
Requires:         R-CRAN-colorRamps >= 2.3
Requires:         R-CRAN-compositions >= 2.0
Requires:         R-CRAN-Morpho >= 2.0
Requires:         R-CRAN-mgcv >= 1.8
Requires:         R-CRAN-oce >= 1.1
Requires:         R-CRAN-Arothron >= 1.0
Requires:         R-CRAN-alphashape3d >= 1.0
Requires:         R-CRAN-morphomap >= 1.0
Requires:         R-CRAN-stringr >= 1.0
Requires:         R-CRAN-DescTools >= 0.99
Requires:         R-CRAN-geometry >= 0.4.0
Requires:         R-CRAN-lattice >= 0.2
Requires:         R-CRAN-Rvcg >= 0.18
Requires:         R-CRAN-rgl >= 0.1
Requires:         R-CRAN-vegan 

%description
Two- and three-dimensional morphometric maps of enamel and dentine
thickness and multivariate analysis. Volume calculation of dental
materials. Principal component analysis of thickness maps with associated
morphometric map variations.

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
