%global __brp_check_rpaths %{nil}
%global packname  htmcglm
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hypothesis Testing for McGLMs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mcglm 
BuildRequires:    R-CRAN-sjmisc 
BuildRequires:    R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mcglm 
Requires:         R-CRAN-sjmisc 
Requires:         R-CRAN-stringr 

%description
Performs hypothesis testing for multivariate covariance generalized linear
models (McGLMs).  McGLM is a general framework for non-normal multivariate
data analysis, designed to handle multivariate response variables, along
with a wide range of temporal and spatial correlation structures defined
in terms of a covariance link function combined with a matrix linear
predictor involving known matrices. The models take non-normality into
account in the conventional way by means of a variance function, and the
mean structure is modelled by means of a link function and a linear
predictor. The models are fitted using an efficient Newton scoring
algorithm based on quasi-likelihood and Pearson estimating functions,
using only second-moment assumptions. This provides a unified approach to
a wide variety of different types of response variables and covariance
structures, including multivariate extensions of repeated measures, time
series, longitudinal, spatial and spatio-temporal structures. The package
offers a user-friendly interface for fitting McGLMs similar to the glm() R
function.

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
