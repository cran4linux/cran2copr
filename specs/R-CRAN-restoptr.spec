%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  restoptr
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Restoration Planning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.6.17
BuildRequires:    R-CRAN-crayon >= 1.4.1
BuildRequires:    R-CRAN-rJava >= 1.0.6
BuildRequires:    R-CRAN-units >= 0.8.0
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
Requires:         R-CRAN-terra >= 1.6.17
Requires:         R-CRAN-crayon >= 1.4.1
Requires:         R-CRAN-rJava >= 1.0.6
Requires:         R-CRAN-units >= 0.8.0
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 

%description
Flexible framework for ecological restoration planning. It aims to
identify priority areas for restoration efforts using optimization
algorithms (based on Justeau-Allaire et al. 2021
<doi:10.1111/1365-2664.13803>). Priority areas can be identified by
maximizing landscape indices, such as the effective mesh size (Jaeger 2000
<doi:10.1023/A:1008129329289>), or the integral index of connectivity
(Pascual-Hortal & Saura 2006 <doi:10.1007/s10980-006-0013-z>).
Additionally, constraints can be used to ensure that priority areas
exhibit particular characteristics (e.g., ensure that particular places
are not selected for restoration, ensure that priority areas form a single
contiguous network). Furthermore, multiple near-optimal solutions can be
generated to explore multiple options in restoration planning. The package
leverages the 'Choco-solver' software to perform optimization using
constraint programming (CP) techniques (<https://choco-solver.org/>).

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
