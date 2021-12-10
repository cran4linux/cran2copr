%global __brp_check_rpaths %{nil}
%global packname  sirt
%global packver   3.11-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.11.21
Release:          1%{?dist}%{?buildtag}
Summary:          Supplementary Item Response Theory Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-CDM 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TAM 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pbv 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CDM 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-TAM 
Requires:         R-utils 

%description
Supplementary functions for item response models aiming to complement
existing R packages. The functionality includes among others
multidimensional compensatory and noncompensatory IRT models (Reckase,
2009, <doi:10.1007/978-0-387-89976-3>), MCMC for hierarchical IRT models
and testlet models (Fox, 2010, <doi:10.1007/978-1-4419-0742-4>), NOHARM
(McDonald, 1982, <doi:10.1177/014662168200600402>), Rasch copula model
(Braeken, 2011, <doi:10.1007/s11336-010-9190-4>; Schroeders, Robitzsch &
Schipolowski, 2014, <doi:10.1111/jedm.12054>), faceted and hierarchical
rater models (DeCarlo, Kim & Johnson, 2011,
<doi:10.1111/j.1745-3984.2011.00143.x>), ordinal IRT model (ISOP;
Scheiblechner, 1995, <doi:10.1007/BF02301417>), DETECT statistic (Stout,
Habing, Douglas & Kim, 1996, <doi:10.1177/014662169602000403>), local
structural equation modeling (LSEM; Hildebrandt, Luedtke, Robitzsch,
Sommer & Wilhelm, 2016, <doi:10.1080/00273171.2016.1142856>).

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
