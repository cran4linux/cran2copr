%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CARRoT
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predicting Categorical and Continuous Outcomes Using One in Ten Rule

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-Rdpack 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
Predicts categorical or continuous outcomes while concentrating on a
number of key points. These are Cross-validation, Accuracy, Regression and
Rule of Ten or "one in ten rule" (CARRoT), and, in addition to it
R-squared statistics, prior knowledge on the dataset etc. It performs the
cross-validation specified number of times by partitioning the input into
training and test set and fitting linear/multinomial/binary regression
models to the training set. All regression models satisfying chosen
constraints are fitted and the ones with the best predictive power are
given as an output. Best predictive power is understood as highest
accuracy in case of binary/multinomial outcomes, smallest absolute and
relative errors in case of continuous outcomes. For binary case there is
also an option of finding a regression model which gives the highest AUROC
(Area Under Receiver Operating Curve) value. The option of parallel
toolbox is also available. Methods are described in Peduzzi et al. (1996)
<doi:10.1016/S0895-4356(96)00236-3> , Rhemtulla et al. (2012)
<doi:10.1037/a0029315>, Riley et al. (2018) <doi:10.1002/sim.7993>, Riley
et al. (2019) <doi:10.1002/sim.7992>.

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
