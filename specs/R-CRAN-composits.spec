%global __brp_check_rpaths %{nil}
%global packname  composits
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Compositional, Multivariate and Univariate Time Series Outlier Ensemble

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-otsad 
BuildRequires:    R-CRAN-tsoutliers 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-anomalize 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-dobin 
BuildRequires:    R-CRAN-ICS 
BuildRequires:    R-CRAN-fastICA 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-kableExtra 
Requires:         R-CRAN-otsad 
Requires:         R-CRAN-tsoutliers 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-anomalize 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-dobin 
Requires:         R-CRAN-ICS 
Requires:         R-CRAN-fastICA 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-kableExtra 

%description
A compositional, multivariate and univariate time series outlier ensemble.
It uses the four R packages 'forecast', 'tsoutliers', 'otsad' and
'anomalize' to detect time series outliers (Kandanaarachchi, Menendez
2020) <doi:10.13140/RG.2.2.32217.95845>.

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
