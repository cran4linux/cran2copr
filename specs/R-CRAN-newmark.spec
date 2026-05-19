%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  newmark
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Uncertainty Analysis in Dynamic Site and Slope Response

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-readxl 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-triangle 
Requires:         R-utils 

%description
Implements a four-stage pipeline for probabilistic seismic performance
analysis of slopes and embankments. The package takes a uniform-hazard
spectrum at multiple return periods as input (any source) and produces:
(1) synthetic soil profile generation and fundamental period estimation
from USCS classification via Ishihara's small-strain shear-modulus model
and the inhomogeneous truncated shear-beam theory of Gazetas and Dakoulas;
(2) nonlinear site amplification using the Seyhan & Stewart (2014) model
<doi:10.1193/063013EQS181M>, with inter-period correlation via Baker &
Jayaram (2008) <doi:10.1193/1.2857544>; (3) Monte Carlo ensemble of six
empirical Newmark sliding-block displacement models (Ambraseys & Menu
(1988) <doi:10.1002/eqe.4290160704>, Jibson (2007)
<doi:10.1016/j.enggeo.2007.01.013>, Saygili & Rathje (2008)
<doi:10.1061/(ASCE)1090-0241(2008)134:6(790)>, Bray & Travasarou (2007)
<doi:10.1061/(ASCE)1090-0241(2007)133:4(381)>, Bray & Macedo (2017)
<doi:10.1016/j.soildyn.2017.05.024>, and the Bray and Macedo
shallow-crustal update) with coherent correlated draws; (4) log-log
inversion to the performance-based seismic coefficient kmax at
user-specified displacement targets. All outputs are 'data.table' objects.

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
