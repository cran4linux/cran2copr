%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IgorR
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read Binary Files Saved by 'Igor Pro' (Including 'Neuromatic' Data)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-timechange 
Requires:         R-CRAN-bitops 
Requires:         R-tools 
Requires:         R-CRAN-timechange 

%description
Provides function to read data from the 'Igor Pro' data analysis program
by 'Wavemetrics'. The data formats supported are 'Igor' packed experiment
format ('pxp') and 'Igor' binary wave ('ibw'). See:
<https://www.wavemetrics.com/> for details. Also includes functions to
load special 'pxp' files produced by the 'Igor Pro' 'Neuromatic' and
'Nclamp' packages for recording and analysing neuronal data. See
<https://github.com/SilverLabUCL/NeuroMatic> for details.

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
