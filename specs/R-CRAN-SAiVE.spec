%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SAiVE
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Functions Used for SAiVE Group Research, Collaborations, and Publications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-VSURF 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 
Requires:         R-CRAN-VSURF 

%description
Holds functions developed by the University of Ottawa's SAiVE
(Spatio-temporal Analysis of isotope Variations in the Environment)
research group with the intention of facilitating the re-use of code,
foster good code writing practices, and to allow others to benefit from
the work done by the SAiVE group. Contributions are welcome via the
'GitHub' repository <https://github.com/UO-SAiVE/SAiVE> by group members
as well as non-members.

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
