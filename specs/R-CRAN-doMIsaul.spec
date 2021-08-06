%global __brp_check_rpaths %{nil}
%global packname  doMIsaul
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Do Multiple Imputation-Based Semi-Supervised and Unsupervised Learning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-aricode 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-clusterCrit 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Gmedian 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-NbClust 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-aricode 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-clusterCrit 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Gmedian 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-NbClust 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Algorithms for (i) unsupervised learning for dataset with missing data
and/or left-censored data, using multiple imputation and consensus
clustering ; (ii) semi-supervised learning with a survival endpoint
(right-censored) for complete or incomplete datasets, using multiple
imputation and consensus clustering in the latter case. The methods are
described in Faucheux et al. (2021) <doi:10.1002/bimj.201900366> and
Faucheux et al. (2021) <doi:10.1002/bimj.202000365>, respectively.

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
