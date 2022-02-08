%global __brp_check_rpaths %{nil}
%global packname  miclust
%global packver   1.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Imputation in Cluster Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-flexclust 
Requires:         R-graphics 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-matrixStats 
Requires:         R-stats 
Requires:         R-utils 

%description
Implementation of a framework for cluster analysis with selection of the
final number of clusters and an optional variable selection procedure. The
package is designed to integrate the results of multiple imputed datasets
while accounting for the uncertainty that the imputations introduce in the
final results. In addition, the package can also be used for a cluster
analysis of the complete cases of a single dataset. The package also
includes specific methods to summarize and plot the results. The methods
are described in Basagana et al. (2013) <doi:10.1093/aje/kws289>.

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
