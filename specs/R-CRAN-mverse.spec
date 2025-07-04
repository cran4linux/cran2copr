%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mverse
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Multiverse Analysis Made Simple

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dplyr >= 1.1
BuildRequires:    R-CRAN-multiverse >= 0.6.2
BuildRequires:    R-CRAN-ggupset >= 0.4.1
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggraph 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dplyr >= 1.1
Requires:         R-CRAN-multiverse >= 0.6.2
Requires:         R-CRAN-ggupset >= 0.4.1
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggraph 

%description
Extends 'multiverse' package (Sarma A., Kale A., Moon M., Taback N.,
Chevalier F., Hullman J., Kay M., 2021) <doi:10.31219/osf.io/yfbwm>, which
allows users perform to create explorable multiverse analysis in R. This
extension provides an additional level of abstraction to the 'multiverse'
package with the aim of creating user friendly syntax to researchers,
educators, and students in statistics. The 'mverse' syntax is designed to
allow piping and takes hints from the 'tidyverse' grammar. The package
allows users to define and inspect multiverse analysis using familiar
syntax in R.

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
