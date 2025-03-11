%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pda
%global packver   1.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Privacy-Preserving Distributed Algorithms

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-stats 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-plyr 

%description
A collection of privacy-preserving distributed algorithms for conducting
multi-site data analyses. The regression analyses can be linear regression
for continuous outcome, logistic regression for binary outcome, Cox
proportional hazard regression for time-to event outcome, Poisson
regression for count outcome, or multi-categorical regression for nominal
or ordinal outcome. The PDA algorithm runs on a lead site and only
requires summary statistics from collaborating sites, with one or few
iterations. The package can be used together with the online system
(<https://pda-ota.pdamethods.org/>) for safe and convenient collaboration.
For more information, please visit our software websites:
<https://github.com/Penncil/pda>, and <https://pdamethods.org/>.

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
