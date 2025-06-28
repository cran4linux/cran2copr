%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gemR
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          General Effect Modelling

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-plsVarSel 
BuildRequires:    R-CRAN-mixlm 
BuildRequires:    R-CRAN-HDANOVA 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-neuralnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-plsVarSel 
Requires:         R-CRAN-mixlm 
Requires:         R-CRAN-HDANOVA 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-neuralnet 

%description
Two-step modeling with separation of sources of variation through analysis
of variance and subsequent multivariate modeling through a range of
unsupervised and supervised statistical methods. Separation can focus on
removal of interfering effects or isolation of effects of interest. EF
Mosleth et al. (2021) <doi:10.1038/s41598-021-82388-w> and EF Mosleth et
al. (2020) <doi:10.1016/B978-0-12-409547-2.14882-6>.

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
