%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  INLAspacetime
%global packver   0.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial and Spatio-Temporal Models using 'INLA'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildRequires:    R-CRAN-INLAtools >= 0.0.5
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-fmesher 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-INLAtools >= 0.0.5
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-fmesher 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 

%description
Prepare objects to implement models over spatial and spacetime domains
with the 'INLA' package (<https://www.r-inla.org>). These objects contain
data to for the 'cgeneric' interface in 'INLA', enabling fast parallel
computations. We implemented the spatial barrier model, see Bakka et. al.
(2019) <doi:10.1016/j.spasta.2019.01.002>, and some of the spatio-temporal
models proposed in Lindgren et. al. (2024)
<https://raco.cat/index.php/SORT/article/view/428665>. Details are
provided in the available vignettes and from the URL bellow.

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
