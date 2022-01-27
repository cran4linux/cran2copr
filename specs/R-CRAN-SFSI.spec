%global __brp_check_rpaths %{nil}
%global packname  SFSI
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Family and Selection Index

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-float 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Here we provide tools for the estimation of coefficients in penalized
regressions when the (co)variance matrix of predictors and the covariance
vector between predictors and response, are provided. These methods are
extended to the context of a Selection Index (commonly used for breeding
value prediction). The approaches offer opportunities such as the
integration of high-throughput traits in genetic evaluations ('Lopez-Cruz
et al., 2020') <doi:10.1038/s41598-020-65011-2> and solutions for training
set optimization in Genomic Prediction ('Lopez-Cruz & de los Campos,
2021') <doi:10.1093/genetics/iyab030>.

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
