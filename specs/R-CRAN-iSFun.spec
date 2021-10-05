%global __brp_check_rpaths %{nil}
%global packname  iSFun
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Integrative Dimension Reduction Analysis for Multi-Source Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-stats 
Requires:         R-CRAN-caret 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-irlba 
Requires:         R-stats 

%description
An implementation of integrative dimension reduction analysis procedures
for multi-source data, which provides integrative sparse partial least
squares, integrative sparse principal component analysis, integrative
sparse canonical correlation analysis and corresponding meta-analysis
versions, etc. The work is built and improved upon the references: (1)
Fang, K., Fan, X., Zhang, Q., and Ma, S. (2018). "Integrative sparse
principal component analysis." Journal of Multivariate Analysis,
<doi:10.1016/j.jmva.2018.02.002>. (2) Liang, W., Ma, S., Zhang, Q., and
Zhu, T. (2021). "Integrative sparse partial least squares." Statistics in
Medicine, <doi:10.1002/sim.8900>.

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
