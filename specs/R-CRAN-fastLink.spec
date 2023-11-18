%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastLink
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Probabilistic Record Linkage with Missing Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-adagio 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-adagio 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plotrix 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 

%description
Implements a Fellegi-Sunter probabilistic record linkage model that allows
for missing data and the inclusion of auxiliary information. This includes
functionalities to conduct a merge of two datasets under the
Fellegi-Sunter model using the Expectation-Maximization algorithm. In
addition, tools for preparing, adjusting, and summarizing data merges are
included. The package implements methods described in Enamorado, Fifield,
and Imai (2019) ''Using a Probabilistic Model to Assist Merging of
Large-scale Administrative Records'' <doi:10.1017/S0003055418000783> and
is available at <https://imai.fas.harvard.edu/research/linkage.html>.

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
