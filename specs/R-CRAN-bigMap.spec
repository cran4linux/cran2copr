%global packname  bigMap
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Big Data Mapping

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-bigmemory >= 4.5.0
BuildRequires:    R-parallel >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-bigmemory >= 4.5.0
Requires:         R-parallel >= 3.5.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-colorspace 

%description
Unsupervised clustering protocol for large scale structured data, based on
a low dimensional representation of the data. Dimensionality reduction is
performed using a parallelized implementation of the t-Stochastic
Neighboring Embedding algorithm (Garriga J. and Bartumeus F. (2018),
<arXiv:1812.09869>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
