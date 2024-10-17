%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cols4all
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Colors for all

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-colorspace >= 2.1
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-spacesXYZ 
Requires:         R-CRAN-colorspace >= 2.1
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-png 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-spacesXYZ 

%description
Color palettes for all people, including those with color vision
deficiency. Popular color palette series have been organized by type and
have been scored on several properties such as color-blind-friendliness
and fairness (i.e. do colors stand out equally?). Own palettes can also be
loaded and analysed. Besides the common palette types (categorical,
sequential, and diverging) it also includes cyclic and bivariate color
palettes. Furthermore, a color for missing values is assigned to each
palette.

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
