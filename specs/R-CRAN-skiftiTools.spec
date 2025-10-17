%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  skiftiTools
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools and Operations for Reading, Writing, Viewing, and Manipulating SKIFTI Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RNifti 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-rmarchingcubes 
BuildRequires:    R-CRAN-Rvcg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-oce 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-s2dv 
Requires:         R-CRAN-RNifti 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-rmarchingcubes 
Requires:         R-CRAN-Rvcg 
Requires:         R-CRAN-png 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-oce 
Requires:         R-CRAN-abind 
Requires:         R-methods 
Requires:         R-CRAN-s2dv 

%description
SKIFTI files contain brain imaging data in coordinates across Tract Based
Spatial Statistics (TBSS) skeleton, which represent the brain white matter
intensity values. 'skiftiTools' provides a unified environment for
reading, writing, visualizing and manipulating SKIFTI-format data. It
supports the "subsetting", "concatenating", and using data as data.frame
for R statistical functions. The SKIFTI data is structured for convenient
access to the data and metadata, and includes support for visualizations.
For more information see Merisaari et al. (2024) <doi:10.57736/87d2-0608>.

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
