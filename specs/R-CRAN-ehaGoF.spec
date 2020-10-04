%global packname  ehaGoF
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates Goodness of Fit Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
Calculates 15 different goodness of fit criteria. These are; standard
deviation ratio (SDR), coefficient of variation (CV), relative root mean
square error (RRMSE), Pearson's correlation coefficients (PC), root mean
square error (RMSE), performance index (PI), mean error (ME), global
relative approximation error (RAE), mean relative approximation error
(MRAE), mean absolute percentage error (MAPE), mean absolute deviation
(MAD), coefficient of determination (R-squared), adjusted coefficient of
determination (adjusted R-squared), Akaike's information criterion (AIC),
corrected Akaike's information criterion (CAIC), Mean Square Error (MSE),
Bayesian Information Criterion (BIC) and Normalized Mean Square Error
(NMSE).

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
