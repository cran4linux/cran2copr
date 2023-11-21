%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesWatch
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Change-Point Detection for Process Monitoring with Fault Detection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-parallel >= 3.6.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-gridExtra >= 0.9
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Hotelling 
BuildRequires:    R-CRAN-CholWishart 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-BDgraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ess 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-parallel >= 3.6.2
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-gridExtra >= 0.9
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Hotelling 
Requires:         R-CRAN-CholWishart 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-BDgraph 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-ess 

%description
Bayes Watch fits an array of Gaussian Graphical Mixture Models to
groupings of homogeneous data in time, called regimes, which are modeled
as the observed states of a Markov process with unknown transition
probabilities.  In doing so, Bayes Watch defines a posterior distribution
on a vector of regime assignments, which gives meaningful expressions on
the probability of every possible change-point.  Bayes Watch also allows
for an effective and efficient fault detection system that assesses what
features in the data where the most responsible for a given change-point.
For further details, see: Alexander C. Murph et al. (2023)
<arXiv:2310.02940>.

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
