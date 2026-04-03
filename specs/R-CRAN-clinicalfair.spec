%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clinicalfair
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithmic Fairness Assessment for Clinical Prediction Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-stats 
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-stats 

%description
Post-hoc fairness auditing toolkit for clinical prediction models. Unlike
in-processing approaches that modify model training, this package
evaluates existing models by computing group-wise fairness metrics
(demographic parity, equalized odds, predictive parity, calibration
disparity), visualizing disparities across protected attributes, and
performing threshold-based mitigation. Supports intersectional analysis
across multiple attributes and generates audit reports useful for
fairness-oriented auditing in clinical AI settings. Methods described in
Obermeyer et al. (2019) <doi:10.1126/science.aax2342> and Hardt, Price,
and Srebro (2016) <doi:10.48550/arXiv.1610.02413>.

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
