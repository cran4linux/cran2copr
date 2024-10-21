%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeomArchetypal
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Finds the Geometrical Archetypal Analysis of a Data Frame

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-archetypal 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-distances 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mirai 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-archetypal 
Requires:         R-CRAN-doParallel 
Requires:         R-methods 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-distances 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mirai 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-scales 

%description
Performs Geometrical Archetypal Analysis after creating Grid Archetypes
which are the Cartesian Product of all minimum, maximum variable values.
Since the archetypes are fixed now, we have the ability to compute the
convex composition coefficients for all our available data points much
faster by using the half part of Principal Convex Hull Archetypal method.
Additionally we can decide to keep as archetypes the closer to the Grid
Archetypes ones. Finally the number of archetypes is always 2 to the power
of the dimension of our data points if we consider them as a vector space.
Cutler, A., Breiman, L. (1994) <doi:10.1080/00401706.1994.10485840>.
Morup, M., Hansen, LK. (2012) <doi:10.1016/j.neucom.2011.06.033>.
Christopoulos, DT. (2024) <doi:10.13140/RG.2.2.14030.88642>.

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
