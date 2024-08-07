%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fmri
%global packver   1.9.12.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.12.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of fMRI Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-aws >= 2.5.1
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-oro.nifti 
Requires:         R-CRAN-aws >= 2.5.1
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-metafor 
Requires:         R-methods 
Requires:         R-CRAN-oro.nifti 

%description
Contains R-functions to perform an fMRI analysis as described in Polzehl
and Tabelow (2019) <DOI:10.1007/978-3-030-29184-6>, Tabelow et al. (2006)
<DOI:10.1016/j.neuroimage.2006.06.029>, Polzehl et al. (2010)
<DOI:10.1016/j.neuroimage.2010.04.241>, Tabelow and Polzehl (2011)
<DOI:10.18637/jss.v044.i11>.

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
