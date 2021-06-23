%global __brp_check_rpaths %{nil}
%global packname  eva
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Extreme Value Analysis with Goodness-of-Fit Testing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-EnvStats 
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-EnvStats 

%description
Goodness-of-fit tests for selection of r in the r-largest order statistics
(GEVr) model. Goodness-of-fit tests for threshold selection in the
Generalized Pareto distribution (GPD). Random number generation and
density functions for the GEVr distribution. Profile likelihood for return
level estimation using the GEVr and Generalized Pareto distributions.
P-value adjustments for sequential, multiple testing error control.
Non-stationary fitting of GEVr and GPD. Bader, B., Yan, J. & Zhang, X.
(2016) <doi:10.1007/s11222-016-9697-3>. Bader, B., Yan, J. & Zhang, X.
(2018) <doi:10.1214/17-AOAS1092>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
