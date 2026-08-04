%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deriva
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Drift Detection for Monitored Machine Learning Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vctrs 

%description
Detects concept drift and data drift in streams produced by deployed
machine learning models, using a tidy interface that composes with the
'tidymodels' ecosystem. Detectors are specified, fitted on a baseline
period, and advanced over new batches of observations, returning tibbles
annotated with warning and drift flags. A catalogue of 22 sequential drift
detectors is provided. Error-based methods include the Drift Detection
Method (DDM) of Gama et al. (2004) <doi:10.1007/978-3-540-28645-5_29>, the
Early Drift Detection Method (EDDM) of Baena-Garcia et al. (2006), the
Hoeffding's inequality based Drift Detection Methods (HDDM) of
Frias-Blanco et al. (2015) <doi:10.1109/TKDE.2014.2345382>, and the
Exponentially Weighted Moving Average (EWMA) chart of Ross et al. (2012)
<doi:10.1016/j.patrec.2011.08.019>. Distribution-based methods include
Adaptive Windowing (ADWIN) of Bifet and Gavalda (2007)
<doi:10.1137/1.9781611972771.42>, Kolmogorov-Smirnov Windowing (KSWIN) of
Raab et al. (2020) <doi:10.1016/j.neucom.2019.11.111>, and the
Page-Hinkley test of Page (1954) <doi:10.1093/biomet/41.1-2.100>.

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
