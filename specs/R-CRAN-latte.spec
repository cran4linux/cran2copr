%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  latte
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'LattE' and '4ti2'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       4ti2
Recommends:       latte-integrale
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-mpoly 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-mpoly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-glue 

%description
Back-end connections to 'LattE' (<https://www.math.ucdavis.edu/~latte/>)
for counting lattice points and integration inside convex polytopes and
'4ti2' (<http://www.4ti2.de/>) for algebraic, geometric, and combinatorial
problems on linear spaces and front-end tools facilitating their use in
the 'R' ecosystem.

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
