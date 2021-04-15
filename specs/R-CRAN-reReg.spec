%global packname  reReg
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Recurrent Event Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-reda >= 0.5.0
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-SQUAREM 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-directlabels 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-reda >= 0.5.0
Requires:         R-CRAN-BB 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-SQUAREM 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-directlabels 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-scam 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rootSolve 

%description
A comprehensive collection of practical and easy-to-use tools for
regression analysis of recurrent events, with or without the presence of a
(possibly) informative terminal event. The modeling framework is based on
a joint frailty scale-change model, that includes models described in Wang
et al. (2001) <doi:10.1198/016214501753209031>, Huang and Wang (2004)
<doi:10.1198/016214504000001033>, Xu et al. (2017)
<doi:10.1080/01621459.2016.1173557>, and Xu et al. (2019)
<doi:10.5705/SS.202018.0224> as special cases. The implemented estimating
procedure does not require any parametric assumption on the frailty
distribution. The package also allows the users to specify different model
forms for both the recurrent event process and the terminal event.

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
