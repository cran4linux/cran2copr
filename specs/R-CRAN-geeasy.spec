%global __brp_check_rpaths %{nil}
%global packname  geeasy
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Solve Generalized Estimating Equations for Clustered Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-geeM 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MESS 
Requires:         R-CRAN-geepack 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-geeM 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MESS 

%description
Estimation of generalized linear models with correlated/clustered
observations by use of generalized estimating equations (GEE). See e.g.
Halekoh and Højsgaard, (2005, <doi:10.18637/jss.v015.i02>), for details.
Several types of clustering are supported, including exchangeable variance
structures, AR1 structures, M-dependent, user-specified variance
structures and more. The model fitting computations are performed using
modified code from the 'geeM' package, while the interface and output
objects have been written to resemble the 'geepack' package. The package
also contains additional tools for working with and inspecting results
from the 'geepack' package, e.g. a 'confint' method for 'geeglm' objects
from 'geepack'.

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
