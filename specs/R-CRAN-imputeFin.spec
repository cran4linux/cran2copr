%global packname  imputeFin
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Imputation of Financial Time Series with Missing Values and/orOutliers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-zoo 
Requires:         R-MASS 
Requires:         R-CRAN-zoo 

%description
Missing values often occur in financial data due to a variety of reasons
(errors in the collection process or in the processing stage, lack of
asset liquidity, lack of reporting of funds, etc.). However, most data
analysis methods expect complete data and cannot be employed with missing
values. One convenient way to deal with this issue without having to
redesign the data analysis method is to impute the missing values. This
package provides an efficient way to impute the missing values based on
modeling the time series with a random walk or an autoregressive (AR)
model, convenient to model log-prices and log-volumes in financial data.
In the current version, the imputation is univariate-based (so no asset
correlation is used). In addition, outliers can be detected and removed.
The package is based on the paper: J. Liu, S. Kumar, and D. P. Palomar
(2019). Parameter Estimation of Heavy-Tailed AR Model With Missing Data
Via Stochastic EM. IEEE Trans. on Signal Processing, vol. 67, no. 8, pp.
2159-2172. <doi:10.1109/TSP.2019.2899816>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
