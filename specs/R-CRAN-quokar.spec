%global packname  quokar
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Quantile Regression Outlier Diagnostics with K Left Out Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ALDqr 
BuildRequires:    R-CRAN-bayesQR 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ald 
Requires:         R-stats 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ALDqr 
Requires:         R-CRAN-bayesQR 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ald 

%description
Diagnostics methods for quantile regression models for detecting
influential observations: robust distance methods for general quantile
regression models; generalized Cook's distance and Q-function distance
method for quantile regression models using aymmetric Laplace
distribution. Reference of this method can be found in Luis E. Benites,
Víctor H. Lachos, Filidor E. Vilca (2015) <arXiv:1509.05099v1>; mean
posterior probability and Kullback–Leibler divergence methods for Bayes
quantile regression model. Reference of this method is Bruno Santos,
Heleno Bolfarine (2016) <arXiv:1601.07344v1>.

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

%files
%{rlibdir}/%{packname}
