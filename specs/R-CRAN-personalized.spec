%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  personalized
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Validation Methods for Subgroup Identification and Personalized Medicine

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xgboost >= 3.1.2.1
BuildRequires:    R-CRAN-glmnet >= 2.0.13
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-xgboost >= 3.1.2.1
Requires:         R-CRAN-glmnet >= 2.0.13
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-survival 
Requires:         R-methods 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-foreach 

%description
Provides functions for fitting and validation of models for subgroup
identification and personalized medicine / precision medicine under the
general subgroup identification framework of Chen et al. (2017)
<doi:10.1111/biom.12676>. This package is intended for use for both
randomized controlled trials and observational studies and is described in
detail in Huling and Yu (2021) <doi:10.18637/jss.v098.i05>.

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
