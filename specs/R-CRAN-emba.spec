%global packname  emba
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
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
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-igraph >= 1.2.4
BuildRequires:    R-CRAN-rje >= 1.10
BuildRequires:    R-CRAN-usefun >= 0.4.3
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-Ckmeans.1d.dp >= 4.2.2
Requires:         R-CRAN-visNetwork >= 2.0.9
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-igraph >= 1.2.4
Requires:         R-CRAN-rje >= 1.10
Requires:         R-CRAN-usefun >= 0.4.3
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 

%description
Analysis and visualization of an ensemble of boolean models for biomarker
discovery in cancer cell networks. The package allows to easily import the
data results of a software pipeline that predicts synergistic drug
combinations in cancer cell lines, developed by the DrugLogics research
group in NTNU. It has generic functions that can be used to split a
boolean model dataset to model groups with regards to the models
predictive performance (number of true positive predictions or Matthews
correlation coefficient score) or synergy prediction based on a given set
of observed synergies and find the average activity difference per network
node between all group pairs. Thus, given user-specific thresholds,
important nodes (biomarkers) can be accessed in the sense that they make
the models predict specific synergies (synergy biomarkers) or have better
performance in general (performance biomarkers). Lastly, if the boolean
models have a specific equation form and differ only in their link
operator, link operator biomarkers can also be assessed.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
