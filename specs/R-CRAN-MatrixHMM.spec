%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MatrixHMM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parsimonious Families of Hidden Markov Models for Matrix-Variate Longitudinal Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-tensor 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-tensor 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-withr 

%description
Implements three families of parsimonious hidden Markov models (HMMs) for
matrix-variate longitudinal data using the Expectation-Conditional
Maximization (ECM) algorithm. The package supports matrix-variate normal,
t, and contaminated normal distributions as emission distributions. For
each hidden state, parsimony is achieved through the eigen-decomposition
of the covariance matrices associated with the emission distribution. This
approach results in a comprehensive set of 98 parsimonious HMMs for each
type of emission distribution. Atypical matrix detection is also
supported, utilizing the fitted (heavy-tailed) models.

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
