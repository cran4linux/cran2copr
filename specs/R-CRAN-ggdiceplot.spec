%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggdiceplot
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dice Plot Visualization for 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-legendry 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-legendry 
Requires:         R-CRAN-scales 

%description
Provides 'ggplot2' extensions for creating dice-based visualizations where
each dot position represents a specific categorical variable. The package
includes geom_dice() for displaying presence/absence of categorical
variables using traditional dice patterns. Each dice position (1-6)
represents a different category, with dots shown only when that category
is present. This allows intuitive visualization of up to 6 categorical
variables simultaneously.

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
