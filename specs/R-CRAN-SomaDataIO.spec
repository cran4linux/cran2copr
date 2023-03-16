%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SomaDataIO
%global packver   6.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Input/Output 'SomaScan' Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.2
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-usethis >= 2.0.1
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-methods 
Requires:         R-CRAN-tibble >= 3.1.2
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-usethis >= 2.0.1
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-CRAN-lifecycle >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-methods 

%description
Load and export 'SomaScan' data via the 'SomaLogic Operating Co., Inc.'
proprietary text file called an ADAT ('*.adat'). For file format see
<https://github.com/SomaLogic/SomaLogic-Data/blob/master/README.md>. The
package also exports auxiliary functions for manipulating, wrangling, and
extracting relevant information from an ADAT object once in memory.

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
