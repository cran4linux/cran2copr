%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prior3D
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          3D Prioritization Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-prioritizr >= 8.0.4
BuildRequires:    R-CRAN-maps >= 3.4.2
BuildRequires:    R-CRAN-readxl >= 1.4.3
BuildRequires:    R-CRAN-geodiv >= 1.1.0
BuildRequires:    R-CRAN-viridis >= 0.6.5
BuildRequires:    R-CRAN-rasterdiv >= 0.3.4
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-highs 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-prioritizr >= 8.0.4
Requires:         R-CRAN-maps >= 3.4.2
Requires:         R-CRAN-readxl >= 1.4.3
Requires:         R-CRAN-geodiv >= 1.1.0
Requires:         R-CRAN-viridis >= 0.6.5
Requires:         R-CRAN-rasterdiv >= 0.3.4
Requires:         R-CRAN-terra 
Requires:         R-CRAN-highs 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Three-dimensional systematic conservation planning, conducting nested
prioritization analyses across multiple depth levels and ensuring
efficient resource allocation throughout the water column. It provides a
structured workflow designed to address biodiversity conservation and
management challenges in the 3 dimensions, while facilitating users’
choices and parameterization (Doxa et al. 2025
<doi:10.1016/j.ecolmodel.2024.110919>).

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
