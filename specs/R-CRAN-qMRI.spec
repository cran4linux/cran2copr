%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qMRI
%global packver   1.2.7.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7.8
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Quantitative Magnetic Resonance Imaging ('qMRI')

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-aws >= 2.4
BuildRequires:    R-CRAN-awsMethods >= 1.0
BuildRequires:    R-CRAN-oro.nifti >= 0.9
BuildRequires:    R-CRAN-adimpro >= 0.9
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-aws >= 2.4
Requires:         R-CRAN-awsMethods >= 1.0
Requires:         R-CRAN-oro.nifti >= 0.9
Requires:         R-CRAN-adimpro >= 0.9
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-stringr 

%description
Implementation of methods for estimation of quantitative maps from
Multi-Parameter Mapping (MPM) acquisitions (Weiskopf et al. (2013)
<doi:10.3389/fnins.2013.00095>) and analysis of Inversion Recovery MRI
data. Usage of the package is described in Polzehl and Tabelow (2023),
"Magnetic Resonance Brain Imaging", 2nd Edition, Chapter 6 and 7,
Springer, Use R! Series. <doi:10.1007/978-3-031-38949-8>. J. Polzehl and
K. Tabelow (2023), "Magnetic Resonance Brain Imaging - Modeling and Data
Analysis Using R: Code and Data." <doi:10.20347/WIAS.DATA.6> provides
extensive example code and data.

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
