%global packname  sentometrics
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          2%{?dist}
Summary:          An Integrated Framework for Textual Sentiment Time SeriesAggregation and Prediction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ISOweek 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-caret 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ISOweek 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-RcppRoll 
Requires:         R-CRAN-RcppParallel 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-utils 

%description
Optimized prediction based on textual sentiment, accounting for the
intrinsic challenge that sentiment can be computed and pooled across texts
and time in various ways. See Ardia et al. (2020)
<doi:10.2139/ssrn.3067734>.

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
