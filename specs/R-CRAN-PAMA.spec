%global __brp_check_rpaths %{nil}
%global packname  PAMA
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rank Aggregation with Partition Mallows Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-ExtMallows 
BuildRequires:    R-CRAN-mc2d 
BuildRequires:    R-CRAN-PerMallows 
BuildRequires:    R-CRAN-rankdist 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
Requires:         R-CRAN-ExtMallows 
Requires:         R-CRAN-mc2d 
Requires:         R-CRAN-PerMallows 
Requires:         R-CRAN-rankdist 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Rank aggregation aims to achieve a better ranking list given multiple
observations. 'PAMA' implements Partition-Mallows model for rank
aggregation where the rankers' quality are different. Both Bayesian
inference and Maximum likelihood estimation (MLE) are provided. It can
handle partial list as well. When covariates information is available,
this package can make inference by incorporating the covariate
information. More information can be found in the paper "Integrated
Partition-Mallows Model and Its Inference for Rank Aggregation".

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
