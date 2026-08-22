%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NeutroCODsAnalysis
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Neutrosophic Analysis Crossover Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Provides methods for Neutrosophic Analysis of Variance (NANOVA) and
Neutrosophic Analysis of Covariance (NANCOVA) for crossover designs, as
well as NANOVA for multi-session designs with direct and residual effects
using interval-valued observations. For crisp data, users can enter
identical lower and upper values for the response and covariate variables
to obtain results equivalent to classical Analysis of Variance (ANOVA) and
Analysis of Covariance (ANCOVA), respectively. The basic concepts of
neutrosophic statistics are based on Smarandache (2014)
<https://fs.unm.edu/NeutrosophicStatistics.pdf>, while the analysis
procedures implemented in this package are newly developed.

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
