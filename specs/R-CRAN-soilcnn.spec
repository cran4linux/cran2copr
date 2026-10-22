%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  soilcnn
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Convolutional Neural Networks for Digital Soil Mapping

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ps 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-utils 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-coro 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-matrixStats 
Requires:         R-parallel 
Requires:         R-CRAN-ps 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-CRAN-torch 
Requires:         R-utils 

%description
A framework, built on 'torch', for mapping a soil property from point
observations and a stack of aligned rasters with a convolutional network
that reads the neighbourhood of each point. It extracts the patches;
resamples by spatial blocks or by k-fold nearest neighbour distance
matching, after Linnenbrink et al. (2024) <doi:10.5194/gmd-17-5897-2024>;
tunes and selects under a noise floor and the one-standard-error rule;
refits the selected configuration under several seeds; and predicts
median, mean and interval maps over rasters of any extent. The map's
centre is the ensemble median over seeds; the mean corrects its
back-transformation by smearing, after Duan (1983)
<doi:10.1080/01621459.1983.10478017>. The intervals are conformal,
calibrated three ways and each checked on the test set: on the
cross-validated residuals; on a calibration set held out of every fold, as
split conformal, after Lei et al. (2018)
<doi:10.1080/01621459.2017.1307116>; or with every fold's model at each
pixel, as CV+, after Barber et al. (2021) <doi:10.1214/20-AOS1965> -- with
points, or whole groups of them, weighing alike, after Dunn et al. (2023)
<doi:10.1080/01621459.2022.2060112>. The area of applicability of Meyer
and Pebesma (2021) <doi:10.1111/2041-210X.13650> is mapped beside them.
What a model learned is read by permutation, by SHAP values from expected
gradients, after Erion et al. (2021) <doi:10.1038/s42256-021-00343-w>, by
SAGE, after Covert et al. (2020) <doi:10.48550/arXiv.2004.00668>, by
accumulated local effects, after Apley and Zhu (2020)
<doi:10.1111/rssb.12377>, and by refits without each variable. Random
forest and multilayer perceptron baselines run under the same folds.

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
