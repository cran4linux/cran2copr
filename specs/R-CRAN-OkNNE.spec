%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OkNNE
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A k-Nearest Neighbours Ensemble via Optimal Model Selection for Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-stats 
Requires:         R-CRAN-FNN 
Requires:         R-stats 

%description
Optimal k Nearest Neighbours Ensemble is an ensemble of base k nearest
neighbour models each constructed on a bootstrap sample with a random
subset of features. k closest observations are identified for a test point
"x" (say), in each base k nearest neighbour model to fit a stepwise
regression to predict the output value of "x". The final predicted value
of "x" is the mean of estimates given by all the models. The implemented
model takes training and test datasets and trains the model on training
data to predict the test data. Ali, A., Hamraz, M., Kumam, P., Khan, D.M.,
Khalil, U., Sulaiman, M. and Khan, Z. (2020)
<DOI:10.1109/ACCESS.2020.3010099>.

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
