%global __brp_check_rpaths %{nil}
%global packname  aftgee
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Accelerated Failure Time Model with Generalized Estimating Equations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-MASS 

%description
A collection of methods for both the rank-based estimates and least-square
estimates to the Accelerated Failure Time (AFT) model. For rank-based
estimation, it provides approaches that include the computationally
efficient Gehan's weight and the general's weight such as the logrank
weight. Details of the rank-based estimation can be found in Chiou et al.
(2014) <doi:10.1007/s11222-013-9388-2> and Chiou et al. (2015)
<doi:10.1002/sim.6415>. For the least-square estimation, the estimating
equation is solved with generalized estimating equations (GEE). Moreover,
in multivariate cases, the dependence working correlation structure can be
specified in GEE's setting. Details on the least-squares estimation can be
found in Chiou et al. (2014) <doi:10.1007/s10985-014-9292-x>.

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
