%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MRFA
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting and Predicting Large-Scale Nonlinear Regression Problems using Multi-Resolution Functional ANOVA (MRFA) Approach

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-grplasso 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-grplasso 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Performs the MRFA approach proposed by Sung et al. (2020)
<doi:10.1080/01621459.2019.1595630> to fit and predict nonlinear
regression problems, particularly for large-scale and high-dimensional
problems. The application includes deterministic or stochastic computer
experiments, spatial datasets, and so on.

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
