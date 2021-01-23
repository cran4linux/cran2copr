%global packname  mifa
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Imputation for Exploratory Factor Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-stats 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-checkmate 

%description
Impute the covariance matrix of incomplete data so that factor analysis
can be performed. Imputations are made using multiple imputation by
Multivariate Imputation with Chained Equations (MICE) and combined with
Rubin's rules. Parametric Fieller confidence intervals and nonparametric
bootstrap confidence intervals can be obtained for the variance explained
by different numbers of principal components. The method is described in
Nassiri et al. (2018) <doi:10.3758/s13428-017-1013-4>.

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
