%global __brp_check_rpaths %{nil}
%global packname  fmf
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Class Noise Detector with Multi-Factor-Based Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-solitude 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-solitude 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-C50 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-ggplot2 

%description
A fast class noise detector which provides noise score for each
observations. The package takes advantage of 'RcppArmadillo' to speed up
the calculation of distances between observations.

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
