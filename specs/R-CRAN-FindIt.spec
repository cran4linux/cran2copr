%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FindIt
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Finding Heterogeneous Treatment Effects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-glinternet 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-limSolve 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-glinternet 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lmtest 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-limSolve 

%description
The heterogeneous treatment effect estimation procedure proposed by Imai
and Ratkovic (2013)<DOI: 10.1214/12-AOAS593>. The proposed method is
applicable, for example, when selecting a small number of most (or least)
efficacious treatments from a large number of alternative treatments as
well as when identifying subsets of the population who benefit (or are
harmed by) a treatment of interest. The method adapts the Support Vector
Machine classifier by placing separate LASSO constraints over the
pre-treatment parameters and causal heterogeneity parameters of interest.
This allows for the qualitative distinction between causal and other
parameters, thereby making the variable selection suitable for the
exploration of causal heterogeneity. The package also contains a class of
functions, CausalANOVA, which estimates the average marginal interaction
effects (AMIEs) by a regularized ANOVA as proposed by Egami and Imai
(2019). It contains a variety of regularization techniques to facilitate
analysis of large factorial experiments.

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
