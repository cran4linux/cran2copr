%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  grafzahl
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Supervised Machine Learning for Textual Data Using Transformers and 'Quanteda'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lime 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lime 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-reticulate 
Requires:         R-utils 
Requires:         R-stats 

%description
Duct tape the 'quanteda' ecosystem (Benoit et al., 2018)
<doi:10.21105/joss.00774> to modern Transformer-based text classification
models (Wolf et al., 2020) <doi:10.18653/v1/2020.emnlp-demos.6>, in order
to facilitate supervised machine learning for textual data. This package
mimics the behaviors of 'quanteda.textmodels' and provides a function to
setup the 'Python' environment to use the pretrained models from 'Hugging
Face' <https://huggingface.co/>.

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
