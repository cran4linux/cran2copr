%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  landsat
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Radiometric and Topographic Correction of Satellite Imagery

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 2.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lmodel2 
BuildRequires:    R-CRAN-mgcv 
Requires:         R-CRAN-sp >= 2.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-lmodel2 
Requires:         R-CRAN-mgcv 

%description
Processing of Landsat or other multispectral satellite imagery. Includes
relative normalization, image-based radiometric correction, and
topographic correction options. The original package description was
published as Goslee (2011) <doi:10.18637/jss.v043.i04>, and details of the
topographic corrections in Goslee (2012) <doi:10.14358/PERS.78.9.973>.

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
