%global packname  sirus
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Stable and Interpretable RUle Set

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 

%description
A regression and classification algorithm based on random forests, which
takes the form of a short list of rules. SIRUS combines the simplicity of
decision trees with a predictivity close to random forests. The core
aggregation principle of random forests is kept, but instead of
aggregating predictions, SIRUS aggregates the forest structure: the most
frequent nodes of the forest are selected to form a stable rule ensemble
model. The algorithm is fully described in the following articles: Benard
C., Biau G., da Veiga S., Scornet E. (2021), Electron. J. Statist.,
15:427-505 <DOI:10.1214/20-EJS1792> for classification, and Benard C.,
Biau G., da Veiga S., Scornet E. (2020) <arXiv:2004.14841> for regression.
This R package is a fork from the project ranger
(<https://github.com/imbs-hl/ranger>).

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
