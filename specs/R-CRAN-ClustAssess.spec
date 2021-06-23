%global __brp_check_rpaths %{nil}
%global packname  ClustAssess
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Assessing Clustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-stats 

%description
A set of tools for evaluating clustering similarity across methods and
method stability using element-centric clustering comparison (Gates et al.
(2019) <doi:10.1038/s41598-019-44892-y>). Additionally, this package
enables data-wide assessment of clustering robustness using proportion of
ambiguously clustered pairs (Senbabaoglu et al. (2014)
<doi:10.1038/srep06207>), which can be used to infer the optimal number of
clusters in the data.

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
