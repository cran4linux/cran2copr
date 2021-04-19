%global packname  EFDR
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Wavelet-Based Enhanced FDR for Detecting Signals from Complete or Incomplete Spatially Aggregated Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-waveslim >= 1.7.5
BuildRequires:    R-CRAN-foreach >= 1.4.2
BuildRequires:    R-CRAN-doParallel >= 1.0.8
BuildRequires:    R-CRAN-gstat >= 1.0.19
BuildRequires:    R-CRAN-sp >= 1.0.15
BuildRequires:    R-CRAN-dplyr >= 0.3.0.2
BuildRequires:    R-CRAN-tidyr >= 0.1.0.9000
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-waveslim >= 1.7.5
Requires:         R-CRAN-foreach >= 1.4.2
Requires:         R-CRAN-doParallel >= 1.0.8
Requires:         R-CRAN-gstat >= 1.0.19
Requires:         R-CRAN-sp >= 1.0.15
Requires:         R-CRAN-dplyr >= 0.3.0.2
Requires:         R-CRAN-tidyr >= 0.1.0.9000
Requires:         R-CRAN-copula 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-parallel 

%description
Enhanced False Discovery Rate (EFDR) is a tool to detect anomalies in an
image. The image is first transformed into the wavelet domain in order to
decorrelate any noise components, following which the coefficients at each
resolution are standardised. Statistical tests (in a multiple hypothesis
testing setting) are then carried out to find the anomalies. The power of
EFDR exceeds that of standard FDR, which would carry out tests on every
wavelet coefficient: EFDR choose which wavelets to test based on a
criterion described in Shen et al. (2002). The package also provides
elementary tools to interpolate spatially irregular data onto a grid of
the required size. The work is based on Shen, X., Huang, H.-C., and
Cressie, N. 'Nonparametric hypothesis testing for a spatial signal.'
Journal of the American Statistical Association 97.460 (2002): 1122-1140.

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
