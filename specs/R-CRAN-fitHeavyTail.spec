%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fitHeavyTail
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mean and Covariance Matrix Estimation under Heavy Tails

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ICSNP 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ghyp 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
Requires:         R-CRAN-ICSNP 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ghyp 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 

%description
Robust estimation methods for the mean vector, scatter matrix, and
covariance matrix (if it exists) from data (possibly containing NAs) under
multivariate heavy-tailed distributions such as angular Gaussian (via
Tyler's method), Cauchy, and Student's t distributions. Additionally, a
factor model structure can be specified for the covariance matrix. The
latest revision also includes the multivariate skewed t distribution. The
package is based on the papers: Sun, Babu, and Palomar (2014); Sun, Babu,
and Palomar (2015); Liu and Rubin (1995); Zhou, Liu, Kumar, and Palomar
(2019); Pascal, Ollila, and Palomar (2021).

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
