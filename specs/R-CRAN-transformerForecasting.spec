%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  transformerForecasting
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Transformer Deep Learning Model for Time Series Forecasting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.20
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-reticulate >= 1.20
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-magrittr 

%description
Time series forecasting faces challenges due to the non-stationarity,
nonlinearity, and chaotic nature of the data. Traditional deep learning
models like Recurrent Neural Network (RNN), Long Short-Term Memory (LSTM),
and Gated Recurrent Unit (GRU) process data sequentially but are
inefficient for long sequences. To overcome the limitations of these
models, we proposed a transformer-based deep learning architecture
utilizing an attention mechanism for parallel processing, enhancing
prediction accuracy and efficiency. This paper presents user-friendly code
for the implementation of the proposed transformer-based deep learning
architecture utilizing an attention mechanism for parallel processing.
References: Nayak et al. (2024) <doi:10.1007/s40808-023-01944-7> and Nayak
et al. (2024) <doi:10.1016/j.simpa.2024.100716>.

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
