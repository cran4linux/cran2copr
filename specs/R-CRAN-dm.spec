%global packname  dm
%global packver   0.1.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.12
Release:          1%{?dist}%{?buildtag}
Summary:          Relational Data Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 2.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.3
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-vctrs >= 0.3.2
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cli >= 2.2.0
Requires:         R-CRAN-dplyr >= 1.0.3
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-vctrs >= 0.3.2
Requires:         R-CRAN-backports 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 

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
