%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BNSP
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Non- And Semi-Parametric Model Fitting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-threejs 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-label.switching 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-threejs 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-label.switching 

%description
MCMC algorithms & processing functions for: 1. single response multiple
regression, see Papageorgiou, G. (2018) <doi: 10.32614/RJ-2018-069>, 2.
multivariate response multiple regression, with nonparametric models for
the means, the variances and the correlation matrix, with variable
selection, see Papageorgiou, G. and Marshall, B. C. (2020) <doi:
10.1080/10618600.2020.1739534>, 3. joint mean-covariance models for
multivariate responses, see Papageorgiou, G. (2022) <doi:
10.1002/sim.9376>, and 4.Dirichlet process mixtures, see Papageorgiou, G.
(2019) <doi: 10.1111/anzs.12273>.

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
