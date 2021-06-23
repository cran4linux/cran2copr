%global __brp_check_rpaths %{nil}
%global packname  chipPCR
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Toolkit of Helper Functions to Pre-Process Amplification Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-outliers 
BuildRequires:    R-CRAN-ptw 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-Rfit 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-signal 
Requires:         R-methods 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-outliers 
Requires:         R-CRAN-ptw 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-Rfit 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-signal 

%description
A collection of functions to pre-process amplification curve data from
polymerase chain reaction (PCR) or isothermal amplification reactions.
Contains functions to normalize and baseline amplification curves, to
detect both the start and end of an amplification reaction, several
smoothers (e.g., LOWESS, moving average, cubic splines, Savitzky-Golay), a
function to detect false positive amplification reactions and a function
to determine the amplification efficiency. Quantification point (Cq)
methods include the first (FDM) and second approximate derivative maximum
(SDM) methods (calculated by a 5-point-stencil) and the cycle threshold
method. Data sets of experimental nucleic acid amplification systems
('VideoScan HCU', capillary convective PCR (ccPCR)) and commercial systems
are included. Amplification curves were generated by helicase dependent
amplification (HDA), ccPCR or PCR. As detection system intercalating dyes
(EvaGreen, SYBR Green) and hydrolysis probes (TaqMan) were used. For more
information see: Roediger et al. (2015)
<doi:10.1093/bioinformatics/btv205>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
