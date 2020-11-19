%global packname  eoffice
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Export or Graph and Tables to 'Microsoft' Office and Import Figures and Tables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-rvg 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-CRAN-R.devices 
BuildRequires:    R-CRAN-devEMF 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-rvg 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplotify 
Requires:         R-CRAN-R.devices 
Requires:         R-CRAN-devEMF 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-plotly 

%description
Provides wrap functions to export and import graphics and data frames in R
to 'microsoft' office. And This package also provide write out figures
with lots of different formats. Since people may work on the platform
without GUI support, the package also provide function to easily write out
figures to lots of different type of formats. Now this package provide
function to extract colors from all types of figures and pdf files.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
