%global packname  quantspec
%global packver   1.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile-Based Spectral Analysis of Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats4 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-snowfall 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats4 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-snowfall 

%description
Methods to determine, smooth and plot quantile periodograms for univariate
and multivariate time series. See Kley (2016) <doi:10.18637/jss.v070.i03>
for a description and tutorial.

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
