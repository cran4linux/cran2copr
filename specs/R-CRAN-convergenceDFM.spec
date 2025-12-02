%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  convergenceDFM
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Convergence and Dynamic Factor Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-zoo 

%description
Tests convergence in macro-financial panels combining Dynamic Factor
Models (DFM) and mean-reverting Ornstein-Uhlenbeck (OU) processes.
Provides: (i) static/approximate DFMs for large panels with VAR/VECM
stability checks, Portmanteau tests and rolling out-of-sample R^2,
following Stock and Watson (2002) <doi:10.1198/073500102317351921> and the
Generalized Dynamic Factor Model of Forni, Hallin, Lippi and Reichlin
(2000) <doi:10.1162/003465300559037>; (ii) cointegration analysis à la
Johansen (1988) <doi:10.1016/0165-1889(88)90041-3>; (iii) OU-based
convergence and half-life summaries grounded in Uhlenbeck and Ornstein
(1930) <doi:10.1103/PhysRev.36.823> and Vasicek (1977)
<doi:10.1016/0304-405X(77)90016-2>; (iv) robust inference via 'sandwich'
HC/HAC estimators (Zeileis (2004) <doi:10.18637/jss.v011.i10>) and
regression diagnostics ('lmtest'); and (v) optional PLS-based factor
preselection (Mevik and Wehrens (2007) <doi:10.18637/jss.v018.i02>).
Functions emphasize reproducibility and clear, publication-ready
summaries.

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
