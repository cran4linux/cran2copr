%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMediation
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mediation Analysis Confidence Intervals

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-base >= 4.1.0
BuildRequires:    R-stats >= 4.1.0
BuildRequires:    R-graphics >= 4.1.0
BuildRequires:    R-grDevices >= 4.1.0
BuildRequires:    R-CRAN-OpenMx >= 2.13
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-e1071 >= 1.6.7
BuildRequires:    R-CRAN-lavaan >= 0.5.20
BuildRequires:    R-CRAN-modelr >= 0.1.8
BuildRequires:    R-CRAN-generics >= 0.0.2
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-base >= 4.1.0
Requires:         R-stats >= 4.1.0
Requires:         R-graphics >= 4.1.0
Requires:         R-grDevices >= 4.1.0
Requires:         R-CRAN-OpenMx >= 2.13
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-e1071 >= 1.6.7
Requires:         R-CRAN-lavaan >= 0.5.20
Requires:         R-CRAN-modelr >= 0.1.8
Requires:         R-CRAN-generics >= 0.0.2

%description
Computes confidence intervals for nonlinear functions of model parameters
(e.g., product of k coefficients) in single-level and multilevel
structural equation models. Methods include the distribution of the
product, Monte Carlo simulation, and bootstrap methods. It also performs
the Model-Based Constrained Optimization (MBCO) procedure for hypothesis
testing of indirect effects. References: Tofighi, D., and MacKinnon, D. P.
(2011). RMediation: An R package for mediation analysis confidence
intervals. Behavior Research Methods, 43, 692-700.
<doi:10.3758/s13428-011-0076-x>; Tofighi, D., and Kelley, K. (2020).
Improved inference in mediation analysis: Introducing the model-based
constrained optimization procedure. Psychological Methods, 25(4), 496-515.
<doi:10.1037/met0000259>; Tofighi, D. (2020). Bootstrap Model-Based
Constrained Optimization Tests of Indirect Effects. Frontiers in
Psychology, 10, 2989. <doi:10.3389/fpsyg.2019.02989>.

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
