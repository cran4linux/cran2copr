%global packname  cvCovEst
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Validated Covariance Matrix Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-origami 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-coop 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-origami 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-coop 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-RColorBrewer 

%description
An efficient cross-validated approach for covariance matrix estimation,
particularly useful in high-dimensional settings. This method relies upon
the theory of loss-based estimator selection to identify the optimal
estimator of the covariance matrix from among a prespecified set of
candidate.

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
