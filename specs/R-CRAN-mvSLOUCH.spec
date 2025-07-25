%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mvSLOUCH
%global packver   2.7.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.7
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Stochastic Linear Ornstein-Uhlenbeck Models for Phylogenetic Comparative Hypotheses

License:          GPL (>= 2) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.3
BuildRequires:    R-CRAN-PCMBase >= 1.2.10
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ouch 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-CRAN-ape >= 5.3
Requires:         R-CRAN-PCMBase >= 1.2.10
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ouch 
Requires:         R-stats 
Requires:         R-CRAN-matrixcalc 

%description
Fits multivariate Ornstein-Uhlenbeck types of models to continues trait
data from species related by a common evolutionary history. See K.
Bartoszek, J, Pienaar, P. Mostad, S. Andersson, T. F. Hansen (2012)
<doi:10.1016/j.jtbi.2012.08.005> and K. Bartoszek, and J. Tredgett Clarke,
J. Fuentes-Gonzalez, V. Mitov, J. Pienaar, M. Piwczynski, R. Puchalka, K.
Spalik, K. L. Voje (2024) <doi:10.1111/2041-210X.14376>. The suggested
PCMBaseCpp package (which significantly speeds up the likelihood
calculations) can be obtained from
<https://github.com/venelin/PCMBaseCpp/>.

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
