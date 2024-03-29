%global __brp_check_rpaths %{nil}
%global packname  semiArtificial
%global packver   2.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generator of Semi-Artificial Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CORElearn >= 1.50.3
BuildRequires:    R-CRAN-RSNNS 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-logspline 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mcclust 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-StatMatch 
Requires:         R-CRAN-CORElearn >= 1.50.3
Requires:         R-CRAN-RSNNS 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-fpc 
Requires:         R-stats 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-logspline 
Requires:         R-methods 
Requires:         R-CRAN-mcclust 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-StatMatch 

%description
Contains methods to generate and evaluate semi-artificial data sets. Based
on a given data set different methods learn data properties using machine
learning algorithms and generate new data with the same properties. The
package currently includes the following data generators: i) a RBF network
based generator using rbfDDA() from package 'RSNNS', ii) a Random Forest
based generator for both classification and regression problems iii) a
density forest based generator for unsupervised data Data evaluation
support tools include: a) single attribute based statistical evaluation:
mean, median, standard deviation, skewness, kurtosis, medcouple, L/RMC, KS
test, Hellinger distance b) evaluation based on clustering using Adjusted
Rand Index (ARI) and FM c) evaluation based on classification performance
with various learning models, e.g., random forests.

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
