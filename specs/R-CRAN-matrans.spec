%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  matrans
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model Averaging-Assisted Optimal Transfer Learning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-quadprog 
Requires:         R-splines 
Requires:         R-stats 

%description
Transfer learning, as a prevailing technique in computer sciences, aims to
improve the performance of a target model by leveraging auxiliary
information from heterogeneous source data. We provide novel tools for
multi-source transfer learning under statistical models based on model
averaging strategies, including linear regression models, partially linear
models. Unlike existing transfer learning approaches, this method
integrates the auxiliary information through data-driven weight
assignments to avoid negative transfer. This is the first package for
transfer learning based on the optimal model averaging frameworks,
providing efficient implementations for practitioners in multi-source data
modeling. The details are described in Hu and Zhang (2023)
<https://jmlr.org/papers/v24/23-0030.html>.

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
