%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LVGP
%global packver   2.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Variable Gaussian Process Modeling with Qualitative and Quantitative Input Variables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.2.5
BuildRequires:    R-parallel >= 3.2.5
BuildRequires:    R-CRAN-randtoolbox >= 1.17
BuildRequires:    R-CRAN-lhs >= 0.14
Requires:         R-stats >= 3.2.5
Requires:         R-parallel >= 3.2.5
Requires:         R-CRAN-randtoolbox >= 1.17
Requires:         R-CRAN-lhs >= 0.14

%description
Fit response surfaces for datasets with latent-variable Gaussian process
modeling, predict responses for new inputs, and plot latent variables
locations in the latent space (only 1D or 2D). The input variables of the
datasets can be quantitative, qualitative/categorical or mixed. The output
variable of the datasets is a scalar (quantitative). The optimization of
the likelihood function is done using a successive
approximation/relaxation algorithm similar to another GP modeling package
"GPM". The modeling method is published in "A Latent Variable Approach to
Gaussian Process Modeling with Qualitative and Quantitative Factors" by
Yichi Zhang, Siyu Tao, Wei Chen, and Daniel W. Apley (2018)
<doi:10.48550/arXiv.1806.07504>. The package is developed in IDEAL of
Northwestern University.

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
