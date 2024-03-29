%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PDFEstimator
%global packver   4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Nonparametric Probability Density Estimator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-MultiRNG 
BuildRequires:    R-methods 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-MultiRNG 
Requires:         R-methods 

%description
Farmer, J., D. Jacobs (2108) <DOI:10.1371/journal.pone.0196937>. A
multivariate nonparametric density estimator based on the maximum-entropy
method.  Accurately predicts a probability density function (PDF) for
random data using a novel iterative scoring function to determine the best
fit without overfitting to the sample.

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
