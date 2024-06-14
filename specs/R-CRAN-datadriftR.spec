%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datadriftR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Concept Drift Detection Methods for Stream Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.2
Requires:         R-core >= 3.5.2
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-R6 

%description
A system designed for detecting concept drift in streaming datasets. It
offers a comprehensive suite of statistical methods to detect concept
drift, including methods for monitoring changes in data distributions over
time. The package supports several tests, such as Drift Detection Method
(DDM), Early Drift Detection Method (EDDM), Hoeffding Drift Detection
Methods (HDDM_A, HDDM_W), Kolmogorov-Smirnov test-based Windowing (KSWIN)
and Page Hinkley (PH) tests. The methods implemented in this package are
based on established research and have been demonstrated to be effective
in real-time data analysis. For more details on the methods, please check
to the following sources. Gama et al. (2004)
<doi:10.1007/978-3-540-28645-5_29>, Baena-Garcia et al. (2006)
<https://www.researchgate.net/publication/245999704_Early_Drift_Detection_Method>,
Frías-Blanco et al. (2014) <https://ieeexplore.ieee.org/document/6871418>,
Raab et al. (2020) <doi:10.1016/j.neucom.2019.11.111>, Page (1954)
<doi:10.1093/biomet/41.1-2.100>, Montiel et al. (2018)
<https://jmlr.org/papers/volume19/18-251/18-251.pdf>.

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
