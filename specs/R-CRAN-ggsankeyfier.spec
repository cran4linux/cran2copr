%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggsankeyfier
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Create Sankey and Alluvial Diagrams Using 'ggplot2'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-grid >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gridBezier 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vwline 
Requires:         R-grid >= 4.1.0
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gridBezier 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vwline 

%description
Sankey and alluvial diagrams visualise flows of quantities across stages
in stacked bars. This package makes it easy to create such diagrams using
'ggplot2'.

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
