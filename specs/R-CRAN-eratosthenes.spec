%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eratosthenes
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Archaeological Synchronism

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-paletteer 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-paletteer 

%description
Estimation of unknown historical or archaeological dates subject to
relationships with other relative dates and absolute constraints, derived
as marginal densities from the full joint conditional, using a two-stage
Gibbs sampler with consistent batch means to assess convergence. Features
reporting on Monte Carlo standard errors, as well as tools for rule-based
estimation of dates of production and use of artifact types, aligning and
checking relative sequences, and evaluating the impact of the omission of
relative/absolute events upon one another.

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
