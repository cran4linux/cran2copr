%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kuenm2
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Detailed Development of Ecological Niche Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 4.1
BuildRequires:    R-CRAN-mgcv >= 1.9
BuildRequires:    R-CRAN-terra >= 1.6
BuildRequires:    R-CRAN-foreach >= 1.5
BuildRequires:    R-CRAN-enmpa >= 0.2.1
BuildRequires:    R-CRAN-mop >= 0.1.3
BuildRequires:    R-CRAN-fpROC >= 0.1.0
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-glmnet >= 4.1
Requires:         R-CRAN-mgcv >= 1.9
Requires:         R-CRAN-terra >= 1.6
Requires:         R-CRAN-foreach >= 1.5
Requires:         R-CRAN-enmpa >= 0.2.1
Requires:         R-CRAN-mop >= 0.1.3
Requires:         R-CRAN-fpROC >= 0.1.0
Requires:         R-CRAN-doSNOW 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
A new set of tools to help with the development of detailed ecological
niche models using multiple algorithms. Pre-modeling analyses and
explorations can be done to prepare data. Model calibration (model
selection) can be done by creating and testing models with several
parameter combinations. Handy options for producing final models with
transfers are included. Other tools to assess extrapolation risks and
variability in model transfers are also available. Methodological and
theoretical basis for the methods implemented here can be found in:
Peterson et al. (2011)
<https://www.degruyter.com/princetonup/view/title/506966>, Radosavljevic
and Anderson (2014) <doi:10.1111/jbi.12227>, Peterson et al. (2018)
<doi:10.1111/nyas.13873>, Cobos et al. (2019) <doi:10.7717/peerj.6281>,
Alkishe et al. (2020) <doi:10.1016/j.pecon.2020.03.002>, Machado-Stredel
et al. (2021) <doi:10.21425/F5FBG48814>, Arias-Giraldo and Cobos (2024)
<doi:10.17161/bi.v18i.21742>, Cobos et al. (2024)
<doi:10.17161/bi.v18i.21742>.

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
