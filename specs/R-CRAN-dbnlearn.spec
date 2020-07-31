%global packname  dbnlearn
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Dynamic Bayesian Network Structure Learning, Parameter Learningand Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-bnviewer 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-bnviewer 
Requires:         R-CRAN-ggplot2 

%description
It allows to learn the structure of univariate time series, learning
parameters and forecasting. Implements a model of Dynamic Bayesian
Networks with temporal windows, with collections of linear regressors for
Gaussian nodes, based on the introductory texts of Korb and Nicholson
(2010) <doi:10.1201/b10391> and Nagarajan, Scutari and Lèbre (2013)
<doi:10.1007/978-1-4614-6446-4>.

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
