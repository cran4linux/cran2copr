%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMediation
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mediation Analysis Confidence Intervals

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-base >= 3.5.0
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-graphics >= 3.5.0
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-grDevices >= 3.5
BuildRequires:    R-CRAN-OpenMx >= 2.13
BuildRequires:    R-CRAN-e1071 >= 1.6.7
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-doParallel >= 1.0.0
BuildRequires:    R-CRAN-iterators >= 1.0.0
BuildRequires:    R-CRAN-lavaan >= 0.5.20
BuildRequires:    R-CRAN-modelr >= 0.1.4
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-base >= 3.5.0
Requires:         R-stats >= 3.5.0
Requires:         R-graphics >= 3.5.0
Requires:         R-methods >= 3.5.0
Requires:         R-grDevices >= 3.5
Requires:         R-CRAN-OpenMx >= 2.13
Requires:         R-CRAN-e1071 >= 1.6.7
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-doParallel >= 1.0.0
Requires:         R-CRAN-iterators >= 1.0.0
Requires:         R-CRAN-lavaan >= 0.5.20
Requires:         R-CRAN-modelr >= 0.1.4

%description
We provide functions to compute confidence intervals for a well-defined
nonlinear function of the model parameters (e.g., product of k
coefficients) in single--level and multilevel structural equation models.
It also computes a chi-square test statistic for a function of indirect
effects. 'Tofighi', D. and 'MacKinnon', D. P. (2011). 'RMediation' An R
package for mediation analysis confidence intervals. Behavior Research
Methods, 43, 692--700. <doi:10.3758/s13428-011-0076-x>. 'Tofighi', D.
(2020). Bootstrap Model-Based Constrained Optimization Tests of Indirect
Effects. Frontiers in Psychology, 10, 2989.
<doi:10.3389/fpsyg.2019.02989>.

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
