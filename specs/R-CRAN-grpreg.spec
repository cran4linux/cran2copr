%global __brp_check_rpaths %{nil}
%global packname  grpreg
%global packver   3.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regularization Paths for Regression Models with Grouped Covariates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-Matrix 

%description
Efficient algorithms for fitting the regularization path of linear
regression, GLM, and Cox regression models with grouped penalties.  This
includes group selection methods such as group lasso, group MCP, and group
SCAD as well as bi-level selection methods such as the group exponential
lasso, the composite MCP, and the group bridge.  For more information, see
Breheny and Huang (2009) <doi:10.4310/sii.2009.v2.n3.a10>, Huang, Breheny,
and Ma (2012) <doi:10.1214/12-sts392>, Breheny and Huang (2015)
<doi:10.1007/s11222-013-9424-2>, and Breheny (2015)
<doi:10.1111/biom.12300>, or visit the package homepage
<https://pbreheny.github.io/grpreg/>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
