%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ROptimus
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Parallel General-Purpose Adaptive Optimisation Engine

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.4.2
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-iterators >= 1.0.9
BuildRequires:    R-CRAN-doParallel >= 1.0.11
Requires:         R-parallel >= 3.4.2
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-iterators >= 1.0.9
Requires:         R-CRAN-doParallel >= 1.0.11

%description
A general-purpose optimisation engine that supports i) Monte Carlo
optimisation with Metropolis criterion [Metropolis et al. (1953)
<doi:10.1063/1.1699114>, Hastings (1970) <doi:10.1093/biomet/57.1.97>] and
Acceptance Ratio Simulated Annealing [Kirkpatrick et al. (1983)
<doi:10.1126/science.220.4598.671>, Černý (1985) <doi:10.1007/BF00940812>]
on multiple cores, and ii) Acceptance Ratio Replica Exchange Monte Carlo
Optimisation. In each case, the system pseudo-temperature is dynamically
adjusted such that the observed acceptance ratio is kept near to the
desired (fixed or changing) acceptance ratio.

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
