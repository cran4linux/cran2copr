%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AcuityView
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Package for Displaying Visual Scenes as They May Appear to an Animal with Lower Acuity

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotrix >= 3.2.3
BuildRequires:    R-CRAN-fftwtools >= 0.9.7
BuildRequires:    R-CRAN-imager >= 0.40.1
BuildRequires:    R-tools 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-plotrix >= 3.2.3
Requires:         R-CRAN-fftwtools >= 0.9.7
Requires:         R-CRAN-imager >= 0.40.1
Requires:         R-tools 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
This code provides a simple method for representing a visual scene as it
may be seen by an animal with less acute vision. When using (or for more
information), please cite the original publication.

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
