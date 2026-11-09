%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlAEWMA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Based Adaptive EWMA Control Charts for Process Dispersion

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-qrnn 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-stats 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-nnet 
Requires:         R-parallel 
Requires:         R-CRAN-qrnn 
Requires:         R-CRAN-rpart 
Requires:         R-stats 

%description
Monitors the variance of a process with adaptive exponentially weighted
moving average (AEWMA) control charts whose smoothing weight is predicted
by a regression model fitted to the transformed subgroup variance. The
subgroup variance is transformed as in Castagliola (2005)
<doi:10.1002/qre.686>; the smoothing weight is predicted by one of nine
pre-fitted models from four families (neural networks, support vector
machines, regression trees and boosting, and a quantile regression with
lagged inputs), following the parameter-free approach of Noor-ul-Amin et
al. (2024) <doi:10.1038/s41598-024-82699-8>, related work on support
vector regression based adaptive EWMA charts by Kazmi and Noor-ul-Amin
(2024) <doi:10.1002/qre.3603>, and the adaptive EWMA idea of Capizzi and
Masarotto (2003) <doi:10.1198/004017003000000023>. The comparison of the
models is described in Atar, Purutçuoğlu and Bursalı (2026), accepted at
the 3rd International Congress on Data Science and Information
Technologies (INFTEC 2026). Control limits are calibrated by Monte Carlo
simulation to a common in-control average run length of 370 for subgroups
of size five. Functions are provided to run a chart on data, to compare
all nine charts, and to estimate average run lengths by simulation.

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
