%global __brp_check_rpaths %{nil}
%global packname  sregsurvey
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Semiparametric Model-Assisted Estimation in Finite Population

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-TeachingSampling 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-TeachingSampling 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-magrittr 

%description
It is a framework to fit semiparametric regression estimators for the
total parameter of a finite population when the interest variable is
asymmetric distributed. The main references for this package are: Sarndal
C.E., Swensson B., and Wretman J. (2003,ISBN: 978-0-387-40620-6, "Model
Assisted Survey Sampling." Springer-Verlag) and Cardozo C.A and
Alonso-Malaver C.E. (2021). "Semi-parametric model assisted estimation in
finite populations." In preparation.

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
