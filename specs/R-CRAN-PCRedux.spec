%global __brp_check_rpaths %{nil}
%global packname  PCRedux
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Quantitative Polymerase Chain Reaction (qPCR) Data Mining and Machine Learning Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bcp 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-chipPCR 
BuildRequires:    R-CRAN-ecp 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-MBmca 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-qpcR 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-bcp 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-chipPCR 
Requires:         R-CRAN-ecp 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-MBmca 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-qpcR 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-segmented 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Extracts features from amplification curve data of quantitative Polymerase
Chain Reactions (qPCR) (Pabinger S. et al. (2014)
<doi:10.1016/j.bdq.2014.08.002>) for machine learning purposes. Helper
functions prepare the amplification curve data for processing as
functional data (e.g., Hausdorff distance) or enable the plotting of
amplification curve classes (negative, ambiguous, positive). The hookreg()
and hookregNL() functions (Burdukiewicz M. et al. (2018)
<doi:10.1016/j.bdq.2018.08.001>) can be used to predict amplification
curves with an hook effect-like curvature. The pcrfit_single() function
can be used to extract features from an amplification curve.

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
