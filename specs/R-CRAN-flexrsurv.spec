%global __brp_check_rpaths %{nil}
%global packname  flexrsurv
%global packver   1.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Relative Survival Analysis

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-Epi 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-orthogonalsplinebasis 
BuildRequires:    R-CRAN-statmod 
Requires:         R-methods 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-Epi 
Requires:         R-CRAN-formula.tools 
Requires:         R-utils 
Requires:         R-CRAN-orthogonalsplinebasis 
Requires:         R-CRAN-statmod 

%description
Package for parametric relative survival analyses. It allows to model
non-linear and non-proportional effects using splines (B-spline and
truncated power basis). It also includes both non proportional and non
linear effects of Remontet, L. et al. (2007) <DOI:10.1002/sim.2656> and
Mahboubi, A. et al. (2011) <DOI:10.1002/sim.4208>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
