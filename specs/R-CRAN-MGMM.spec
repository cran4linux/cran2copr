%global packname  MGMM
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Missingness Aware Gaussian Mixture Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-cluster 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-cluster 
Requires:         R-methods 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-plyr 
Requires:         R-stats 

%description
Parameter estimation and classification for Gaussian Mixture Models (GMMs)
in the presence of missing data. This package uses an expectation
conditional maximization algorithm to obtain maximum likelihood estimates
for all model parameters and maximum a posteriori classifications of the
input vectors. For additional details, please see McCaw ZR, Julienne H,
Aschard H. "MGMM: an R package for fitting Gaussian Mixture Models on
Incomplete Data." <doi:10.1101/2019.12.20.884551>.

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
