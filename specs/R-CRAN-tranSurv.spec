%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tranSurv
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Transformation-Based Regression under Dependent Truncation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-truncSP 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-SQUAREM 
BuildRequires:    R-methods 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-truncSP 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-SQUAREM 
Requires:         R-methods 

%description
A latent, quasi-independent truncation time is assumed to be linked with
the observed dependent truncation time, the event time, and an unknown
transformation parameter via a structural transformation model. The
transformation parameter is chosen to minimize the conditional Kendall's
tau (Martin and Betensky, 2005) <doi:10.1198/016214504000001538> or the
regression coefficient estimates (Jones and Crowley, 1992)
<doi:10.2307/2336782>. The marginal distribution for the truncation time
and the event time are completely left unspecified. The methodology is
applied to survival curve estimation and regression analysis.

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
