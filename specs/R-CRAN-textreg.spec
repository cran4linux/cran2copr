%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  textreg
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          n-Gram Text Regression, aka Concise Comparative Summarization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-tm >= 0.7
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-NLP >= 0.1.10
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-tm >= 0.7
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-NLP >= 0.1.10
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Function for sparse regression on raw text, regressing a labeling vector
onto a feature space consisting of all possible phrases.

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
