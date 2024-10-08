%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hhsmm
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Hidden Hybrid Markov/Semi-Markov Model Fitting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-CMAPSS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-splines2 
Requires:         R-CRAN-CMAPSS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-splines2 

%description
Develops algorithms for fitting, prediction, simulation and initialization
of the following models (1)- hidden hybrid Markov/semi-Markov model,
introduced by Guedon (2005) <doi:10.1016/j.csda.2004.05.033>, (2)-
nonparametric mixture of B-splines emissions (Langrock et al., 2015
<doi:10.1111/biom.12282>), (3)- regime switching regression model (Kim et
al., 2008 <doi:10.1016/j.jeconom.2007.10.002>) and auto-regressive hidden
hybrid Markov/semi-Markov model, (4)- spline-based nonparametric
estimation of additive state-switching models (Langrock et al., 2018
<doi:10.1111/stan.12133>) (5)- robust emission model proposed by Qin et
al, 2024 <doi:10.1007/s10479-024-05989-4> (6)- several emission
distributions, including mixture of multivariate normal (which can also
handle missing data using EM algorithm) and multi-nomial emission (for
modeling polymer or DNA sequences) (7)- tools for prediction of future
state sequence, computing the score of a new sequence, splitting the
samples and sequences to train and test sets, computing the information
measures of the models, computing the residual useful lifetime
(reliability) and many other useful tools ... (read for more description:
Amini et al., 2022 <doi:10.1007/s00180-022-01248-x> and its arxiv version:
<doi:10.48550/arXiv.2109.12489>).

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
