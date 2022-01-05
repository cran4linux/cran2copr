%global __brp_check_rpaths %{nil}
%global packname  shar
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Species-Habitat Associations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-spatstat.core 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-classInt 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-spatstat.core 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-stats 
Requires:         R-utils 

%description
Analyse species-habitat associations in R. Therefore, information about
the location of the species (as a point pattern) is needed together with
environmental conditions (as a categorical raster). To test for
significance habitat associations, one of the two components is
randomized. Methods are mainly based on Plotkin et al. (2000)
<doi:10.1006/jtbi.2000.2158> and Harms et al. (2001)
<doi:10.1111/j.1365-2745.2001.00615.x>.

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
