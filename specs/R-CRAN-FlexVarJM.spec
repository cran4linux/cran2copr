%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FlexVarJM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Joint Models with Subject-Specific Variance

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lcmm 
BuildRequires:    R-CRAN-marqLevAlg 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-splines 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lcmm 
Requires:         R-CRAN-marqLevAlg 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-survminer 
Requires:         R-utils 

%description
Estimation of mixed models including a subject-specific variance which can
be time and covariate dependent. In the joint model framework, the package
handles left truncation and allows a flexible dependence structure between
the competing events and the longitudinal marker. The estimation is
performed under the frequentist framework, using the Marquardt-Levenberg
algorithm. (Courcoul, Tzourio, Woodward, Barbieri, Jacqmin-Gadda (2023)
<arXiv:2306.16785>).

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
