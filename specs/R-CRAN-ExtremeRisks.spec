%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ExtremeRisks
%global packver   0.0.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extreme Risk Measures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-pracma 

%description
A set of procedures for estimating risks related to extreme events via
risk measures such as Expectile, Value-at-Risk, etc. is provided.
Estimation methods for univariate independent observations and temporal
dependent observations are available. The methodology is extended to the
case of independent multidimensional observations.  The statistical
inference is performed through parametric and non-parametric estimators.
Inferential procedures such as confidence intervals, confidence regions
and hypothesis testing are obtained by exploiting the asymptotic theory.
Adapts the methodologies derived in Padoan and Stupfler (2022)
<doi:10.3150/21-BEJ1375>, Davison et al. (2023)
<doi:10.1080/07350015.2022.2078332>, Daouia et al. (2018)
<doi:10.1111/rssb.12254>, Drees (2000) <doi:10.1214/aoap/1019487617>,
Drees (2003) <doi:10.3150/bj/1066223272>, de Haan and Ferreira (2006)
<doi:10.1007/0-387-34471-3>, de Haan et al. (2016)
<doi:10.1007/s00780-015-0287-6>.

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
