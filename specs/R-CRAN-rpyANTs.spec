%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rpyANTs
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          An Alternative Advanced Normalization Tools ('ANTs')

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RNifti >= 1.5.0
BuildRequires:    R-CRAN-reticulate >= 1.26
BuildRequires:    R-CRAN-rpymat >= 0.1.6
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-RNifti >= 1.5.0
Requires:         R-CRAN-reticulate >= 1.26
Requires:         R-CRAN-rpymat >= 0.1.6
Requires:         R-grDevices 
Requires:         R-stats 

%description
Provides portable access from 'R' to biomedical image processing toolbox
'ANTs' by Avants et al. (2009) <doi:10.54294/uvnhin> via seamless
integration with the 'Python' implementation 'ANTsPy'. Allows biomedical
images to be processed in 'Python' and analyzed in 'R', and vice versa via
shared memory. See 'citation("rpyANTs")' for more reference information.

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
