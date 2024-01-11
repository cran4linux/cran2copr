%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BaSkePro
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Model to Archaeological Faunal Skeletal Profiles

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Tool to perform Bayesian inference of carcass processing/transport
strategy and bone attrition from archaeofaunal skeletal profiles
characterized by percentages of MAU (Minimum Anatomical Units). The
approach is based on a generative model for skeletal profiles that
replicates the two phases of formation of any faunal assemblage: initial
accumulation as a function of human transport strategies and subsequent
attrition.Two parameters define this model: 1) the transport preference
(alpha), which can take any value between - 1 (mostly axial contribution)
and 1 (mostly appendicular contribution) following strategies constructed
as a function of butchering efficiency of different anatomical elements
and the results of ethnographic studies, and 2) degree of attrition
(beta), which can vary between 0 (no attrition) and 10 (maximum attrition)
and relates the survivorship of bone elements to their maximum bone
density. Starting from uniform prior probability distribution functions of
alpha and beta, a Monte Carlo Markov Chain sampling based on a random walk
Metropolis-Hasting algorithm is adopted to derive the posterior
probability distribution functions, which are then available for
interpretation. During this process, the likelihood of obtaining the
observed percentages of MAU given a pair of parameter values is estimated
by the inverse of the Chi2 statistic, multiplied by the proportion of
elements within a 1 percent of the observed value. See Ana B.
Marin-Arroyo, David Ocio (2018).<doi:10.1080/08912963.2017.1336620>.

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
