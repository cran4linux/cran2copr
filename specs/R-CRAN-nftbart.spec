%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nftbart
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Failure Time Bayesian Additive Regression Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-Rcpp 

%description
Nonparametric Failure Time (NFT) Bayesian Additive Regression Trees
(BART): Time-to-event Machine Learning with Heteroskedastic Bayesian
Additive Regression Trees (HBART) and Low Information Omnibus (LIO)
Dirichlet Process Mixtures (DPM). An NFT BART model is of the form Y = mu
+ f(x) + sd(x) E where functions f and sd have BART and HBART priors,
respectively, while E is a nonparametric error distribution due to a DPM
LIO prior hierarchy. See the following for a technical description of the
model
<https://www.mcw.edu/-/media/MCW/Departments/Biostatistics/tr72.pdf?la=en>.

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
