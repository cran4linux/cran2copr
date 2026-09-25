%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rxode2lincmt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Compartment Model Solutions and Gradients for 'rxode2'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-StanHeaders >= 2.21.0.7
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.9.2
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppParallel 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-checkmate 

%description
Analytic one, two and three compartment linear pharmacokinetic solutions
with their parameter gradients from 'stan' automatic differentiation
(Carpenter et al (2015) <doi:10.48550/arXiv.1509.07164>), eigen
decompositions and derived-parameter conversions used by 'rxode2' (Wang,
Hallow and James (2016) <doi:10.1002/psp4.12052>).  Split out of 'rxode2'
so its installation does not compile 'stan' AD items which made it take
too long to compile by itself. The closed-form solutions follow the idea
of the 'wnl' package (Bae, <https://CRAN.R-project.org/package=wnl>),
though the implementation here is different.

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
