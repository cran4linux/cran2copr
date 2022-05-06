%global __brp_check_rpaths %{nil}
%global packname  biosensors.usc
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Distributional Data Analysis Techniques for Biosensor Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-parallelDist 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-parallelDist 
Requires:         R-CRAN-osqp 
Requires:         R-CRAN-truncnorm 

%description
Unified and user-friendly framework for using new distributional
representations of biosensors data in different statistical modeling
tasks: regression models, hypothesis testing, cluster analysis,
visualization, and descriptive analysis. Distributional representations
are a functional extension of compositional time-range metrics and we have
used them successfully so far in modeling glucose profiles and
accelerometer data. However, these functional representations can be used
to represent any biosensor data such as ECG or medical imaging such as
fMRI. Matabuena M, Petersen A, Vidal JC, Gude F. "Glucodensities: A new
representation of glucose profiles using distributional data analysis"
(2021) <doi:10.1177/0962280221998064>.

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
