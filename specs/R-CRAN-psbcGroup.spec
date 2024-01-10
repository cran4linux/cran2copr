%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psbcGroup
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Parametric and Semiparametric Bayesian Survival Models with Shrinkage and Grouping Priors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-LearnBayes 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-LearnBayes 
Requires:         R-CRAN-SuppDists 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-survival 

%description
Algorithms to implement various Bayesian penalized survival regression
models including: semiparametric proportional hazards models with lasso
priors (Lee et al., Int J Biostat, 2011 <doi:10.2202/1557-4679.1301>) and
three other shrinkage and group priors (Lee et al., Stat Anal Data Min,
2015 <doi:10.1002/sam.11266>); parametric accelerated failure time models
with group/ordinary lasso prior (Lee et al. Comput Stat Data Anal, 2017
<doi:10.1016/j.csda.2017.02.014>).

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
