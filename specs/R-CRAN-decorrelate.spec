%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  decorrelate
%global packver   0.1.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Decorrelation Projection Scalable to High Dimensional Data

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-CholWishart 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-irlba 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-CholWishart 
Requires:         R-CRAN-Matrix 
Requires:         R-utils 
Requires:         R-stats 

%description
Data whitening is a widely used preprocessing step to remove correlation
structure since statistical models often assume independence. Here we use
a probabilistic model of the observed data to apply a whitening
transformation. Our Gaussian Inverse Wishart Empirical Bayes model
substantially reduces computational complexity, and regularizes the
eigen-values of the sample covariance matrix to improve out-of-sample
performance.

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
