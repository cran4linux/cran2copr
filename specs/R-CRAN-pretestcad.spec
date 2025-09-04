%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pretestcad
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pretest Probability for Coronary Artery Disease

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 

%description
An application to calculate a patient's pretest probability (PTP) for
obstructive Coronary Artery Disease (CAD) from a collection of guidelines
or studies. Guidelines usually comes from the American Heart Association
(AHA), American College of Cardiology (ACC) or European Society of
Cardiology (ESC). Examples of PTP scores that comes from studies are the
2020 Winther et al. basic, Risk Factor-weighted Clinical Likelihood
(RF-CL) and Coronary Artery Calcium Score-weighted Clinical Likelihood
(CACS-CL) models <doi:10.1016/j.jacc.2020.09.585>, 2019 Reeh et al. basic
and clinical models <doi:10.1093/eurheartj/ehy806> and 2017 Fordyce et al.
PROMISE Minimal-Risk Tool <doi:10.1001/jamacardio.2016.5501>.  As
diagnosis of CAD involves a costly and invasive coronary angiography
procedure for patients, having a reliable PTP for CAD helps doctors to
make better decisions during patient management.  This ensures high risk
patients can be diagnosed and treated early for CAD while avoiding
unnecessary testing for low risk patients.

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
