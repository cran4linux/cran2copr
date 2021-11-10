%global __brp_check_rpaths %{nil}
%global packname  Rtropical
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Analysis Tools over Space of Phylogenetic Trees Using Tropical Geometry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-RcppAlgos 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-parallel 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-RcppAlgos 
Requires:         R-CRAN-caret 

%description
Process phylogenetic trees with tropical support vector machine and
principal component analysis defined with tropical geometry. Details about
tropical support vector machine are available in : Tang, X., Wang, H. &
Yoshida, R. (2020) <arXiv:2003.00677>. Details about tropical principle
component analysis are available in : Page, R., Yoshida, R. & Zhang L.
(2020) <doi:10.1093/bioinformatics/btaa564> and Yoshida, R., Zhang, L. &
Zhang, X. (2019) <doi:10.1007/s11538-018-0493-4>.

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
