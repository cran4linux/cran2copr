%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDNRA
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Location Testing with Normal-Reference Approaches

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-readr 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides inverse-free high-dimensional location tests for two-sample and
general linear hypothesis testing (GLHT) problems under equal or unequal
covariance structures. The package implements classical
normal-approximation procedures, scale-invariant procedures,
normal-reference procedures based on covariance-matched Gaussian
companions, and F-type normal-reference calibrations for heteroscedastic
Behrens-Fisher and GLHT settings. Implemented two-sample
normal-approximation and scale-invariant procedures include Bai and
Saranadasa (1996) <https://www.jstor.org/stable/24306018>, Chen and Qin
(2010) <doi:10.1214/09-aos716>, Srivastava and Du (2008)
<doi:10.1016/j.jmva.2006.11.002>, and Srivastava et al. (2013)
<doi:10.1016/j.jmva.2012.08.014>. Implemented two-sample normal-reference
procedures include Zhang, Guo, Zhou and Cheng (2020)
<doi:10.1080/01621459.2019.1604366>, Zhang, Zhou, Guo and Zhu (2021)
<doi:10.1016/j.jspi.2020.11.008>, Zhang, Zhu and Zhang (2020)
<doi:10.1016/j.ecosta.2019.12.002>, Zhang, Zhu and Zhang (2023)
<doi:10.1080/02664763.2020.1834516>, Zhang and Zhu (2022)
<doi:10.1080/10485252.2021.2015768>, Zhang and Zhu (2022)
<doi:10.1007/s42519-021-00232-w>, and Zhu, Wang and Zhang (2023)
<doi:10.1007/s00180-023-01433-6>. Implemented GLHT normal-approximation
procedures include Fujikoshi et al. (2004) <doi:10.14490/jjss.34.19>,
Srivastava and Fujikoshi (2006) <doi:10.1016/j.jmva.2005.08.010>, Yamada
and Srivastava (2012) <doi:10.1080/03610926.2011.581786>, Schott (2007)
<doi:10.1016/j.jmva.2006.11.007>, and Zhou, Guo and Zhang (2017)
<doi:10.1016/j.jspi.2017.03.005>. Implemented GLHT normal-reference
procedures include Zhang, Guo and Zhou (2017)
<doi:10.1016/j.jmva.2017.01.002>, Zhang, Zhou and Guo (2022)
<doi:10.1016/j.jmva.2021.104816>, Zhu, Zhang and Zhang (2022)
<doi:10.5705/ss.202020.0362>, Zhu and Zhang (2022)
<doi:10.1007/s00180-021-01110-6>, Zhang and Zhu (2022)
<doi:10.1016/j.csda.2021.107385>, and Cao et al. (2024)
<doi:10.1007/s00362-024-01530-8>. The package also includes the
random-integration normal-approximation GLHT procedure of Li et al. (2025)
<doi:10.1007/s00362-024-01624-3>. A package-level overview is given in
Wang, Zhu and Zhang (2026) <doi:10.1016/j.csda.2025.108269>.

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
