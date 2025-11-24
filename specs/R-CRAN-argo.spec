%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  argo
%global packver   3.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Accurate Estimation of Influenza Epidemics using Google Search Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-boot 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-boot 

%description
Augmented Regression with General Online data (ARGO) for accurate
estimation of influenza epidemics in United States on national level,
regional level and state level. It replicates the method introduced in
paper Yang, S., Santillana, M. and Kou, S.C. (2015)
<doi:10.1073/pnas.1515373112>; Ning, S., Yang, S. and Kou, S.C. (2019)
<doi:10.1038/s41598-019-41559-6>; Yang, S., Ning, S. and Kou, S.C. (2021)
<doi:10.1038/s41598-021-83084-5>.

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
