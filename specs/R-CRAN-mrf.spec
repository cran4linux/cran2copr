%global __brp_check_rpaths %{nil}
%global packname  mrf
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multiresolution Forecasting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-monmlp 
BuildRequires:    R-CRAN-nnfor 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-DEoptim 
Requires:         R-stats 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-monmlp 
Requires:         R-CRAN-nnfor 

%description
Forecasting of univariate time series using feature extraction with
variable prediction methods is provided. Feature extraction is done with a
redundant Haar wavelet transform with filter h = (0.5, 0.5). The advantage
of the approach compared to typical Fourier based methods is an dynamic
adaptation to varying seasonalities. Currently implemented prediction
methods based on the selected wavelets levels and scales are a regression
and a multi-layer perceptron. Forecasts can be computed for horizon 1 or
higher. Model selection is performed with an evolutionary optimization.
Selection criteria are currently the AIC criterion, the Mean Absolute
Error or the Mean Root Error. The data is split into three parts for model
selection: Training, test, and evaluation dataset. The training data is
for computing the weights of a parameter set. The test data is for
choosing the best parameter set. The evaluation data is for assessing the
forecast performance of the best parameter set on new data unknown to the
model. This work is published in Stier, Q.; Gehlert, T.; Thrun, M.C.
Multiresolution Forecasting for Industrial Applications, in press,
Processes 2021.

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
