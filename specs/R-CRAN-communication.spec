%global packname  communication
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Extraction and Model Estimation for Audio of Human Speech

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.700.2.0
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-useful 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-wrassp 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-gtable 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-GGally 
Requires:         R-grid 
Requires:         R-CRAN-useful 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-wrassp 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-gtable 

%description
Provides fast, easy feature extraction of human speech and model
estimation with hidden Markov models. Flexible extraction of phonetic
features and their derivatives, with necessary preprocessing options like
feature standardization. Communication can estimate supervised and
unsupervised hidden Markov models with these features, with cross
validation and corrections for auto-correlation in features. Methods
developed in Knox and Lucas (2021) <doi:10.7910/DVN.8BTOHQ>.

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
