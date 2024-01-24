%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clustEff
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clusters of Effects Curves in Quantile Regression Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-qrcm 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-qrcm 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggplot2 

%description
Clustering method to cluster both effects curves, through quantile
regression coefficient modeling, and curves in functional data analysis.
Sottile G. and Adelfio G. (2019) <doi:10.1007/s00180-018-0817-8>.

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
