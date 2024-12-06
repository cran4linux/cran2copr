%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RSquaredMI
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          R-Squared with Multiply Imputed Data

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-altR2 >= 1.1.0
BuildRequires:    R-CRAN-lm.beta 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mice 
Requires:         R-CRAN-altR2 >= 1.1.0
Requires:         R-CRAN-lm.beta 
Requires:         R-CRAN-matrixStats 
Requires:         R-stats 
Requires:         R-CRAN-mice 

%description
Provides R-squared values and standardized regression coefficients for
linear models applied to multiply imputed datasets as obtained by 'mice'.
Confidence intervals, zero-order correlations, and alternative adjusted
R-squared estimates are also available. The methods are described in Van
Ginkel and Karch (2024) <doi:10.1111/bmsp.12344> and in Van Ginkel (2020)
<doi:10.1007/s11336-020-09696-4>.

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
