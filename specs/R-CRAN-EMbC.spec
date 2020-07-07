%global packname  EMbC
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          2%{?dist}
Summary:          Expectation-Maximization Binary Clustering

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-maptools 

%description
Unsupervised, multivariate, binary clustering for meaningful annotation of
data, taking into account the uncertainty in the data. A specific
constructor for trajectory analysis in movement ecology yields behavioural
annotation of trajectories based on estimated local measures of velocity
and turning angle, eventually with solar position covariate as a daytime
indicator, ("Expectation-Maximization Binary Clustering for Behavioural
Annotation").

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
