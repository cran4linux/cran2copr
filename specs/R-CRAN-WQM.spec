%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WQM
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Wavelet-Based Quantile Mapping for Postprocessing Numerical Weather Predictions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MBC 
BuildRequires:    R-CRAN-WaveletComp 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-MBC 
Requires:         R-CRAN-WaveletComp 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-ggplot2 

%description
The wavelet-based quantile mapping (WQM) technique is designed to correct
biases in spatio-temporal precipitation forecasts across multiple time
scales. The WQM method effectively enhances forecast accuracy by
generating an ensemble of precipitation forecasts that account for
uncertainties in the prediction process. For a comprehensive overview of
the methodologies employed in this package, please refer to Jiang, Z., and
Johnson, F. (2023) <doi:10.1029/2022EF003350>. The package relies on two
packages for continuous wavelet transforms: 'WaveletComp', which can be
installed automatically, and 'wmtsa', which is optional and available from
the CRAN archive <https://cran.r-project.org/src/contrib/Archive/wmtsa/>.
Users need to manually install 'wmtsa' from this archive if they prefer to
use 'wmtsa' based decomposition.

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
