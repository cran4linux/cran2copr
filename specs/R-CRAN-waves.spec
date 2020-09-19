%global packname  waves
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vis-NIR Spectral Analysis Wrapper

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-prospectr 
BuildRequires:    R-CRAN-spectacles 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-wesanderson 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-tidyr >= 1.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-prospectr 
Requires:         R-CRAN-spectacles 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-wesanderson 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 

%description
Originally designed application in the context of resource-limited plant
research and breeding programs, 'waves' provides an open-source solution
to spectral data processing and model development by bringing useful
packages together into a streamlined pipeline. This package is wrapper for
functions related to the analysis of point visible and near-infrared
reflectance measurements. It includes visualization, filtering,
aggregation, preprocessing, cross-validation set formation, model
training, and prediction functions to enable open-source association of
spectral and reference data. Specialized cross-validation schemes are
described in detail in Jarquín et al. (2017)
<doi:10.3835/plantgenome2016.12.0130>. Example data is from Ikeogu et al.
(2017) <doi:10.1371/journal.pone.0188918>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
