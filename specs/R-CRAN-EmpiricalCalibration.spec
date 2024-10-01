%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EmpiricalCalibration
%global packver   3.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Routines for Performing Empirical Calibration of Observational Study Estimates

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rcpp 

%description
Routines for performing empirical calibration of observational study
estimates. By using a set of negative control hypotheses we can estimate
the empirical null distribution of a particular observational study setup.
This empirical null distribution can be used to compute a calibrated
p-value, which reflects the probability of observing an estimated effect
size when the null hypothesis is true taking both random and systematic
error into account. A similar approach can be used to calibrate confidence
intervals, using both negative and positive controls. For more details,
see Schuemie et al. (2013) <doi:10.1002/sim.5925> and Schuemie et al.
(2018) <doi:10.1073/pnas.1708282114>.

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
