%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LBBNN
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Binary Bayesian Neural Networks Using 'torch'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-CRAN-svglite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-coro 
Requires:         R-CRAN-svglite 

%description
Latent binary Bayesian neural networks (LBBNNs) are implemented using
'torch', an R interface to the LibTorch backend. Supports mean-field
variational inference as well as flexible variational posteriors using
normalizing flows. The standard LBBNN implementation follows Hubin and
Storvik (2024) <doi:10.3390/math12060788>, using the local
reparametrization trick as in Skaaret-Lund et al. (2024)
<https://openreview.net/pdf?id=d6kqUKzG3V>. Input-skip connections are
also supported, as described in Høyheim et al. (2025)
<doi:10.48550/arXiv.2503.10496>.

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
