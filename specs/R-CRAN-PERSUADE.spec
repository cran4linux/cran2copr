%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PERSUADE
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Survival Model Selection for Decision-Analytic Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-flexsurvcure 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-muhaz 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-sft 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-survminer 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-flexsurvcure 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-muhaz 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-sft 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-survminer 

%description
Provides a standardized framework to support the selection and evaluation
of parametric survival models for time-to-event data. Includes tools for
visualizing survival data, checking proportional hazards assumptions
(Grambsch and Therneau, 1994, <doi:10.1093/biomet/81.3.515>), comparing
parametric (Ishak and colleagues, 2013, <doi:10.1007/s40273-013-0064-3>),
spline (Royston and Parmar, 2002, <doi:10.1002/sim.1203>) and cure models,
examining hazard functions, and evaluating model extrapolation. Methods
are consistent with recommendations in the NICE Decision Support Unit
Technical Support Documents (14 and 21
<https://sheffield.ac.uk/nice-dsu/tsds/survival-analysis>). Results are
structured to facilitate integration into decision-analytic models, and
reports can be generated with 'rmarkdown'. The package builds on existing
tools including 'flexsurv' (Jackson, 2016, <doi:10.18637/jss.v070.i08>))
and 'flexsurvcure' for estimating cure models.

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
