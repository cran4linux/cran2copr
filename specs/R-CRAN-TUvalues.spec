%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TUvalues
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Calculating Allocations in Game Theory using Exact and Approximated Methods

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-highs 
Requires:         R-utils 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-highs 

%description
The main objective of cooperative Transferable-Utility games (TU-games) is
to allocate a good among the agents involved. The package implements major
solution concepts including the Shapley value, Banzhaf value, and
egalitarian rules, alongside their extensions for structured games: the
Owen value and Banzhaf-Owen value for games with a priori unions, and the
Myerson value for communication games on networks. To address the inherent
exponential computational complexity of exact evaluation, the package
offers both exact algorithms and linear approximation methods based on
sampling, enabling the analysis of large-scale games. Additionally, it
supports core set-based solutions, allowing computation of the vertices
and the centroid of the core.

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
