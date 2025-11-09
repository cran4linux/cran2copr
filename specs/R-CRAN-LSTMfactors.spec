%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LSTMfactors
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Determining the Number of Factors in Exploratory Factor Analysis by LSTM

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-EFAfactors 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-EFAfactors 

%description
A method for factor retention using a pre-trained Long Short Term Memory
(LSTM) Network, which is originally developed by Hochreiter and
Schmidhuber (1997) <doi:10.1162/neco.1997.9.8.1735>, is provided. The
sample size of the dataset used to train the LSTM model is 1,000,000. Each
sample is a batch of simulated response data with a specific latent factor
structure. The eigenvalues of these response data will be used as
sequential data to train the LSTM. The pre-trained LSTM is capable of
factor retention for real response data with a true latent factor number
ranging from 1 to 10, that is, determining the number of factors.

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
