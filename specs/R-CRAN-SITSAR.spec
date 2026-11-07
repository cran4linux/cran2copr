%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SITSAR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Information Theory, Geometry and Statistics for Synthetic Aperture Radar Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-parsnip >= 1.0.0
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-parsnip >= 1.0.0
Requires:         R-CRAN-generics 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Statistical models, information-theoretic measures and image analysis
tools for Synthetic Aperture Radar (SAR) and polarimetric SAR (PolSAR)
data. It implements intensity models (Gamma, generalized Gamma and G0I)
and matrix models (scaled complex Wishart, G0 polarimetric and the
compound truncated Poisson and compound geometric complex Wishart laws),
maximum likelihood and expectation-maximization estimation, closed-form
Shannon entropies with their asymptotic variances, entropy-based
hypothesis tests and change detection, entropy-based image segmentation by
(stochastic) expectation-maximization, stochastic distances and a family
of divergence-based classifiers (Kullback-Leibler, Jeffreys, Bhattacharyya
and Renyi) for Gaussian vector features and complex Wishart matrix
features. The main tools are 'R6' classes and the classifiers are
available as a 'parsnip' model, so they can be used inside 'tidymodels'
workflows. Methods are described in Ferreira, Coelho and Nascimento (2021)
<doi:10.1080/01431161.2020.1826060>, Ferreira and Nascimento (2020)
<doi:10.1109/JSTARS.2020.2997666>, Ferreira, Nascimento and Frery (2022)
<doi:10.3390/rs14205083> and Nascimento, Ferreira and Frery (2023)
<doi:10.1007/s11222-023-10298-0>.

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
