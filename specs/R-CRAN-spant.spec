%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spant
%global packver   3.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          MR Spectroscopy Analysis Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-expm >= 1.0.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ptw 
BuildRequires:    R-CRAN-mmand 
BuildRequires:    R-CRAN-RNifti 
BuildRequires:    R-CRAN-RNiftyReg 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-expm >= 1.0.0
Requires:         R-CRAN-abind 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-minpack.lm 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-ptw 
Requires:         R-CRAN-mmand 
Requires:         R-CRAN-RNifti 
Requires:         R-CRAN-RNiftyReg 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-jsonlite 

%description
Tools for reading, visualising and processing Magnetic Resonance
Spectroscopy data. The package includes methods for spectral fitting:
Wilson (2021) <DOI:10.1002/mrm.28385>, Wilson (2025)
<DOI:10.1002/mrm.30462> and spectral alignment: Wilson (2018)
<DOI:10.1002/mrm.27605>.

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
