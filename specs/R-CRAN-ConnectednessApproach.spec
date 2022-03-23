%global __brp_check_rpaths %{nil}
%global packname  ConnectednessApproach
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Connectedness Approach

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rmgarch 
BuildRequires:    R-CRAN-frequencyConnectedness 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-WeightedPortTest 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-moments 
Requires:         R-CRAN-rmgarch 
Requires:         R-CRAN-frequencyConnectedness 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-WeightedPortTest 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-moments 

%description
The estimation of static and dynamic connectedness measures is created in
a modular and user-friendly way. Besides, the time domain connectedness
approaches, this package further allows to estimate the frequency
connectedness approach, the joint spillover index and the extended joint
connectedness approach. In addition, all connectedness frameworks can be
based upon orthogonalized and generalized VAR, QVAR, LASSO VAR, Ridge VAR,
Elastic Net VAR and TVP-VAR models. Furthermore, the package includes the
conditional, decomposed and partial connectedness measures as well as the
pairwise connectedness index, influence index and corrected total
connectedness index. Finally, a battery of datasets are available allowing
to replicate a variety of connectedness papers.

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
