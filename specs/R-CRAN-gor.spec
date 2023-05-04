%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gor
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithms for the Subject Graphs and Network Optimization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-stats 

%description
Informal implementation of some algorithms from Graph Theory and
Combinatorial Optimization which arise in the subject "Graphs and Network
Optimization" from first course of the EUPLA (Escuela Universitaria
Politecnica de La Almunia) degree of Data Engineering in Industrial
Processes. References used are: Cook et al (1998, ISBN:0-471-55894-X),
Korte, Vygen (2018) <doi:10.1007/978-3-662-56039-6>, Hromkovic (2004)
<doi:10.1007/978-3-662-05269-3>, Hartmann, Weigt (2005,
ISBN:978-3-527-40473-5).

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
