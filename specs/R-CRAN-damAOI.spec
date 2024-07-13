%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  damAOI
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create an 'Area of Interest' Around a Constructed Dam for Comparative Impact Evaluations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-smoothr 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-shinydashboard 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-units 
Requires:         R-CRAN-smoothr 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-shinydashboard 

%description
Define a spatial 'Area of Interest' (AOI) around a constructed dam using
hydrology data. Dams have environmental and social impacts, both positive
and negative. Current analyses of dams have no consistent way to specify
at what spatial extent we should evaluate these impacts. 'damAOI'
implements methods to adjust reservoir polygons to match
satellite-observed surface water areas, plot upstream and downstream
rivers using elevation data and accumulated river flow, and draw buffers
clipped by river basins around reservoirs and relevant rivers. This helps
to consistently determine the areas which could be impacted by dam
construction, facilitating comparative analysis and informed
infrastructure investments.

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
