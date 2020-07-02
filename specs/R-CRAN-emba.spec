%global packname  emba
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Ensemble Boolean Model Biomarker Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Ckmeans.1d.dp >= 4.2.2
BuildRequires:    R-CRAN-visNetwork >= 2.0.9
BuildRequires:    R-CRAN-igraph >= 1.2.4
BuildRequires:    R-CRAN-rje >= 1.10
BuildRequires:    R-CRAN-usefun >= 0.4.3
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-Ckmeans.1d.dp >= 4.2.2
Requires:         R-CRAN-visNetwork >= 2.0.9
Requires:         R-CRAN-igraph >= 1.2.4
Requires:         R-CRAN-rje >= 1.10
Requires:         R-CRAN-usefun >= 0.4.3
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 

%description
Analysis and visualization of an ensemble of boolean models for biomarker
discovery in cancer cell networks. The package allows to easily load the
simulation data results of the DrugLogics software pipeline which predicts
synergistic drug combinations in cancer cell lines (developed by the
DrugLogics research group in NTNU). It has generic functions that can be
used to split a boolean model dataset to model groups with regards to the
models predictive performance (number of true positive
predictions/Matthews correlation coefficient score) or synergy prediction
based on a given set of gold standard synergies and find the average
activity difference per network node between all model group pairs. Thus,
given user-specific thresholds, important nodes (biomarkers) can be
accessed in the sense that they make the models predict specific synergies
(synergy biomarkers) or have better performance in general (performance
biomarkers). Lastly, if the boolean models have a specific equation form
and differ only in their link operator, link operator biomarkers can also
be found.

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
