%global __brp_check_rpaths %{nil}
%global packname  metasens
%global packver   1.5-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Sensitivity Analysis in Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 5.5.0
Requires:         R-CRAN-meta >= 5.5.0

%description
The following methods are implemented to evaluate how sensitive the
results of a meta-analysis are to potential bias in meta-analysis and to
support Schwarzer et al. (2015) <DOI:10.1007/978-3-319-21416-0>, Chapter 5
'Small-Study Effects in Meta-Analysis': - Copas selection model described
in Copas & Shi (2001) <DOI:10.1177/096228020101000402>; - limit
meta-analysis by Rücker et al. (2011) <DOI:10.1093/biostatistics/kxq046>;
- upper bound for outcome reporting bias by Copas & Jackson (2004)
<DOI:10.1111/j.0006-341X.2004.00161.x>; - imputation methods for missing
binary data by Gamble & Hollis (2005) <DOI:10.1016/j.jclinepi.2004.09.013>
and Higgins et al. (2008) <DOI:10.1177/1740774508091600>; - LFK index test
and Doi plot by Furuya-Kanamori et al. (2018)
<DOI:10.1097/XEB.0000000000000141>.

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
