%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hybridts
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hybrid Time Series Forecasting Using Error Remodeling Approach

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-nnfor 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-WaveletArima 
BuildRequires:    R-CRAN-Metrics 
Requires:         R-datasets 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-nnfor 
Requires:         R-stats 
Requires:         R-CRAN-WaveletArima 
Requires:         R-CRAN-Metrics 

%description
Method and tool for generating hybrid time series forecasts using an error
remodeling approach. These forecasting approaches utilize a recursive
technique for modeling the linearity of the series using a linear method
(e.g., ARIMA, Theta, etc.) and then models (forecasts) the residuals of
the linear forecaster using non-linear neural networks (e.g., ANN, ARNN,
etc.). The hybrid architectures comprise three steps: firstly, the linear
patterns of the series are forecasted which are followed by an error
re-modeling step, and finally, the forecasts from both the steps are
combined to produce the final output. This method additionally provides
the confidence intervals as needed. Ten different models can be
implemented using this package. This package generates different types of
hybrid error correction models for time series forecasting based on the
algorithms by Zhang. (2003), Chakraborty et al. (2019), Chakraborty et al.
(2020), Bhattacharyya et al. (2021), Chakraborty et al. (2022), and
Bhattacharyya et al. (2022) <doi:10.1016/S0925-2312(01)00702-0>
<doi:10.1016/j.physa.2019.121266> <doi:10.1016/j.chaos.2020.109850>
<doi:10.1109/IJCNN52387.2021.9533747> <doi:10.1007/978-3-030-72834-2_29>
<doi:10.1007/s11071-021-07099-3>.

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
