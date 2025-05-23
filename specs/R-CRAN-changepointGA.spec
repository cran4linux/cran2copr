%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  changepointGA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Changepoint Detection via Modified Genetic Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-stats 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-clue 
Requires:         R-stats 

%description
The Genetic Algorithm (GA) is used to perform changepoint analysis in time
series data. The package also includes an extended island version of GA,
as described in Lu, Lund, and Lee (2010, <doi:10.1214/09-AOAS289>). By
mimicking the principles of natural selection and evolution, GA provides a
powerful stochastic search technique for solving combinatorial
optimization problems. In 'changepointGA', each chromosome represents a
changepoint configuration, including the number and locations of
changepoints, hyperparameters, and model parameters. The package employs
genetic operators—selection, crossover, and mutation—to iteratively
improve solutions based on the given fitness (objective) function. Key
features of 'changepointGA' include encoding changepoint configurations in
an integer format, enabling dynamic and simultaneous estimation of model
hyperparameters, changepoint configurations, and associated parameters.
The detailed algorithmic implementation can be found in the package
vignettes and in the paper of Li (2024, <doi:10.48550/arXiv.2410.15571>).

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
