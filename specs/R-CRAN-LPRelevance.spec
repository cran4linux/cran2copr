%global __brp_check_rpaths %{nil}
%global packname  LPRelevance
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Relevance-Integrated Statistical Inference Engine

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BayesGOF 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-locfdr 
BuildRequires:    R-CRAN-Bolstad2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-caret 
Requires:         R-stats 
Requires:         R-CRAN-BayesGOF 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-locfdr 
Requires:         R-CRAN-Bolstad2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-caret 

%description
Provide methods to perform customized inference at individual level by
taking contextual covariates into account. Three main functions are
provided in this package: (i) LASER(): it generates specially-designed
artificial relevant samples for a given case; (ii) g2l.proc(): computes
customized fdr(z|x); and (iii) rEB.proc(): performs empirical Bayes
inference based on LASERs. The details can be found in Mukhopadhyay, S.,
and Wang, K (2021, <arXiv:2004.09588>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
