%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  atime
%global packver   2024.11.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2024.11.15
Release:          1%{?dist}%{?buildtag}
Summary:          Asymptotic Timing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-bench 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-bench 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-git2r 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Computing and visualizing comparative asymptotic timings of different
algorithms and code versions. Also includes functionality for comparing
empirical timings with expected references such as linear or quadratic,
<https://en.wikipedia.org/wiki/Asymptotic_computational_complexity> Also
includes functionality for measuring asymptotic memory and other
quantities.

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
