%global __brp_check_rpaths %{nil}
%global packname  emdi
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating and Mapping Disaggregated Indicators

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-parallelMap 
BuildRequires:    R-CRAN-HLMdiag 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-readODS 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-saeRobust 
BuildRequires:    R-CRAN-spdep 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-parallelMap 
Requires:         R-CRAN-HLMdiag 
Requires:         R-parallel 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-readODS 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-saeRobust 
Requires:         R-CRAN-spdep 

%description
Functions that support estimating, assessing and mapping regional
disaggregated indicators. So far, estimation methods comprise direct
estimation, the model-based unit-level approach Empirical Best Prediction
(see "Small area estimation of poverty indicators" by Molina and Rao
(2010) doi{10.1002/cjs.10051}), the area-level model (see "Estimates of
income for small places: An application of James-Stein procedures to
Census Data" by Fay and Herriot (1979)
doi{10.1080/01621459.1979.10482505}) and various extensions of it
(adjusted variance estimation methods, log and arcsin transformation,
spatial, robust and measurement error models), as well as their precision
estimates. The assessment of the used model is supported by a summary and
diagnostic plots. For a suitable presentation of estimates, map plots can
be easily created. Furthermore, results can easily be exported to excel.
For a detailed description of the package and the methods used see "The
{R} Package {emdi} for Estimating and Mapping Regionally Disaggregated
Indicators" by Kreutzmann et al. (2019) <doi:10.18637/jss.v091.i07> and
the second package vignette "A Framework for Producing Small Area
Estimates Based on Area-Level Models in {R}".

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
