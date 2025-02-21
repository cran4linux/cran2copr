%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pdynmc
%global packver   0.9.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.12
Release:          1%{?dist}%{?buildtag}
Summary:          Moment Condition Based Estimation of Linear Dynamic Panel Data Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.4
BuildRequires:    R-methods >= 3.6.2
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-CRAN-optimx >= 2018.07.10
BuildRequires:    R-CRAN-Matrix >= 1.2.17
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-Rdpack >= 0.11.0
Requires:         R-CRAN-MASS >= 7.3.51.4
Requires:         R-methods >= 3.6.2
Requires:         R-stats >= 3.6.0
Requires:         R-CRAN-optimx >= 2018.07.10
Requires:         R-CRAN-Matrix >= 1.2.17
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-Rdpack >= 0.11.0

%description
Linear dynamic panel data modeling based on linear and nonlinear moment
conditions as proposed by Holtz-Eakin, Newey, and Rosen (1988)
<doi:10.2307/1913103>, Ahn and Schmidt (1995)
<doi:10.1016/0304-4076(94)01641-C>, and Arellano and Bover (1995)
<doi:10.1016/0304-4076(94)01642-D>. Estimation of the model parameters
relies on the Generalized Method of Moments (GMM) and instrumental
variables (IV) estimation, numerical optimization (when nonlinear moment
conditions are employed) and the computation of closed form solutions
(when estimation is based on linear moment conditions). One-step, two-step
and iterated estimation is available. For inference and specification
testing, Windmeijer (2005) <doi:10.1016/j.jeconom.2004.02.005> and doubly
corrected standard errors (Hwang, Kang, Lee, 2021
<doi:10.1016/j.jeconom.2020.09.010>) are available. Additionally, serial
correlation tests, tests for overidentification, and Wald tests are
provided. Functions for visualizing panel data structures and modeling
results obtained from GMM estimation are also available. The plot methods
include functions to plot unbalanced panel structure, coefficient ranges
and coefficient paths across GMM iterations (the latter is implemented
according to the plot shown in Hansen and Lee, 2021
<doi:10.3982/ECTA16274>). For a more detailed description of the GMM-based
functionality, please see Fritsch, Pua, Schnurbus (2021)
<doi:10.32614/RJ-2021-035>. For more details on the IV-based estimation
routines, see Fritsch, Pua, and Schnurbus (WP, 2024) and Han and Phillips
(2010) <doi:10.1017/S026646660909063X>.

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
