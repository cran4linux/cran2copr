%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hyperoverlap
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Overlap Detection in n-Dimensional Space

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-matlib 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-misc3d 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-matlib 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-misc3d 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-graphics 

%description
Uses support vector machines to identify a perfectly separating hyperplane
(linear or curvilinear) between two entities in high-dimensional space. If
this plane exists, the entities do not overlap. Applications include
overlap detection in morphological, resource or environmental dimensions.
More details can be found in: Brown et al. (2020)
<doi:10.1111/2041-210X.13363> .

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
