%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IFANN
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Intuitionistic Fuzzy Artificial Neural Network for Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-nnet 
Requires:         R-stats 
Requires:         R-utils 

%description
Time series forecasting with an intuitionistic fuzzy artificial neural
network. Lagged values of the series and their intuitionistic fuzzy
membership and non-membership degrees, obtained by intuitionistic fuzzy
c-means clustering, are used as inputs of a feed-forward neural network
with one hidden layer, averaged over several random starts. The lag order
and the network hyper-parameters (number of hidden neurons and weight
decay) can be set manually or tuned automatically by grid search over
user-defined minimum, maximum and step ranges, with time-ordered
validation and a progress display. The intuitionistic fuzzy approach
follows Yolcu and Yolcu (2023) <doi:10.1016/j.eswa.2022.119336>.

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
