%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtexture
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Application of Co-Occurrence Matrices and Haralick Texture

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 2.0
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-fitscape >= 0.1
BuildRequires:    R-CRAN-dlookr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-magrittr >= 2.0
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-fitscape >= 0.1
Requires:         R-CRAN-dlookr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
Generalizes application of gray-level co-occurrence matrix (GLCM) metrics
to objects outside of images. The current focus is to apply GLCM metrics
to the study of biological networks and fitness landscapes that are used
in studying evolutionary medicine and biology, particularly the evolution
of cancer resistance. The package was developed as part of the author's
publication in Physics in Medicine and Biology Barker-Clarke et al. (2023)
<doi:10.1088/1361-6560/ace305>. A general reference to learn more about
mathematical oncology can be found at Rockne et al. (2019)
<doi:10.1088/1478-3975/ab1a09>.

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
