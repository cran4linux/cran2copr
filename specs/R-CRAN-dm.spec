%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dm
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Relational Data Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-cli >= 2.2.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-vctrs >= 0.3.2
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-cli >= 2.2.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-vctrs >= 0.3.2
Requires:         R-CRAN-backports 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-memoise 
Requires:         R-methods 

%description
Provides tools for working with multiple related tables, stored as data
frames or in a relational database.  Multiple tables (data and metadata)
are stored in a compound object, which can then be manipulated with a
pipe-friendly syntax.

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
