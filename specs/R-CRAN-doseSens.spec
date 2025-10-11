%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  doseSens
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conduct Sensitivity Analysis with Continuous Exposures and Binary or Continuous Outcomes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-lpSolve 

%description
Performs sensitivity analysis for the sharp null, attributable effects,
and weak nulls in matched studies with continuous exposures and binary or
continuous outcomes as described in Zhang, Small, Heng (2024)
<doi:10.48550/arXiv.2401.06909> and Zhang, Heng (2024)
<doi:10.48550/arXiv.2409.12848>. Two of the functions require installation
of the 'Gurobi' optimizer. Please see
<https://docs.gurobi.com/current/#refman/ins_the_r_package.html> for
guidance.

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
