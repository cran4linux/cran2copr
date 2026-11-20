%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ngvb
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Non-Gaussian Modelling with 'INLA' and Variational Bayes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-codetools 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 

%description
Diagnoses whether the latent Gaussian assumption of a model fitted with
the 'INLA' package is adequate, and fits latent non-Gaussian extensions
that relax it. The function ng.check() reports a Bayes-factor sensitivity
diagnostic that says whether, and where, the Gaussian assumption is
inadequate; ngvb() then fits the non-Gaussian model by a variational-Bayes
loop around 'INLA', adding local flexibility only where the data support
it. A single unified engine implements the conditional precision Q(theta,
V) = D(theta)^T diag(1/V) D(theta) and owns its normalizing constant, and
a model registry covers iid, random-walk, autoregressive,
Ornstein-Uhlenbeck, intrinsic-CAR (besag), simultaneous-autoregression,
'SPDE'/Matern and seasonal models. Methods follow Cabral, Bolin and Rue
(2024) <doi:10.1080/01621459.2023.2296704> and Cabral, Bolin and Rue
(2025) <doi:10.1093/jrsssb/qkae107>.

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
