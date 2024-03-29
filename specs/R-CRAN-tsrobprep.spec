%global __brp_check_rpaths %{nil}
%global packname  tsrobprep
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Preprocessing of Time Series Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-textTinyR 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-Rdpack 
Requires:         R-splines 
Requires:         R-CRAN-textTinyR 
Requires:         R-CRAN-zoo 

%description
Methods for handling the missing values outliers are introduced in this
package. The recognized missing values and outliers are replaced using a
model-based approach. The model may consist of both autoregressive
components and external regressors. The methods work robust and efficient,
and they are fully tunable. The primary motivation for writing the package
was preprocessing of the energy systems data, e.g. power plant production
time series, but the package could be used with any time series data. For
details, see Narajewski et al. (2021) <doi:10.1016/j.softx.2021.100809>.

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
