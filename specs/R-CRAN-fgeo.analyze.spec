%global __brp_check_rpaths %{nil}
%global packname  fgeo.analyze
%global packver   1.1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.14
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze ForestGEO Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 2.1.2
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-glue >= 1.3.1
BuildRequires:    R-CRAN-fgeo.tool >= 1.2.4
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-withr >= 2.1.2
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-fgeo.tool >= 1.2.4
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
To help you access, transform, analyze, and visualize ForestGEO data, we
developed a collection of R packages
(<https://forestgeo.github.io/fgeo/>). This package, in particular, helps
you to implement analyses of plot species distributions, topography,
demography, and biomass. It also includes a torus translation test to
determine habitat associations of tree species as described by Zuleta et
al. (2018) <doi:10.1007/s11104-018-3878-0>. To learn more about ForestGEO
visit <https://forestgeo.si.edu/>.

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
