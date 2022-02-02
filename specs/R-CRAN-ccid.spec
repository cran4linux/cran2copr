%global __brp_check_rpaths %{nil}
%global packname  ccid
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Covariance Isolate Detect: a New Change-Point Method for Estimating Dynamic Functional Connectivity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-IDetect 
BuildRequires:    R-CRAN-hdbinseg 
BuildRequires:    R-CRAN-GeneNet 
BuildRequires:    R-CRAN-gdata 
Requires:         R-CRAN-IDetect 
Requires:         R-CRAN-hdbinseg 
Requires:         R-CRAN-GeneNet 
Requires:         R-CRAN-gdata 

%description
Provides efficient implementation of the Cross-Covariance Isolate Detect
(CCID) methodology for the estimation of the number and location of
multiple change-points in the second-order (cross-covariance or network)
structure of multivariate, possibly high-dimensional time series. The
method is motivated by the detection of change points in functional
connectivity networks for functional magnetic resonance imaging (fMRI),
electroencephalography (EEG), magentoencephalography (MEG) and
electrocorticography (ECoG) data. The main routines in the package have
been extensively tested on fMRI data. For details on the CCID methodology,
please see Anastasiou et al (2022), Cross-covariance isolate detect: A new
change-point method for estimating dynamic functional connectivity.
Medical Image Analysis, Volume 75.

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
