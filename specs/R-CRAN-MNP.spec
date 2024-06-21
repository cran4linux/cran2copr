%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MNP
%global packver   3.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting the Multinomial Probit Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1
Requires:         R-core >= 2.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits the Bayesian multinomial probit model via Markov chain Monte Carlo.
The multinomial probit model is often used to analyze the discrete choices
made by individuals recorded in survey data. Examples where the
multinomial probit model may be useful include the analysis of product
choice by consumers in market research and the analysis of candidate or
party choice by voters in electoral studies. The MNP package can also fit
the model with different choice sets for each individual, and complete or
partial individual choice orderings of the available alternatives from the
choice set. The estimation is based on the efficient marginal data
augmentation algorithm that is developed by Imai and van Dyk (2005). "A
Bayesian Analysis of the Multinomial Probit Model Using the Data
Augmentation." Journal of Econometrics, Vol. 124, No. 2 (February), pp.
311-334. <doi:10.1016/j.jeconom.2004.02.002> Detailed examples are given
in Imai and van Dyk (2005). "MNP: R Package for Fitting the Multinomial
Probit Model."  Journal of Statistical Software, Vol. 14, No. 3 (May), pp.
1-32. <doi:10.18637/jss.v014.i03>.

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
