%global packname  EHRtemporalVariability
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Delineating Temporal Dataset Shifts in Electronic Health Records

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-scales 
Requires:         R-methods 
Requires:         R-MASS 

%description
Functions to delineate temporal dataset shifts in Electronic Health
Records through the projection and visualization of dissimilarities among
data temporal batches. This is done through the estimation of data
statistical distributions over time and their projection in non-parametric
statistical manifolds, uncovering the patterns of the data latent temporal
variability. 'EHRtemporalVariability' is particularly suitable for
multi-modal data and categorical variables with a high number of values,
common features of biomedical data where traditional statistical process
control or time-series methods may not be appropriate.
'EHRtemporalVariability' allows you to explore and identify dataset shifts
through visual analytics formats such as Data Temporal heatmaps and
Information Geometric Temporal (IGT) plots. An additional
'EHRtemporalVariability' Shiny app can be used to load and explore the
package results and even to allow the use of these functions to those
users non-experienced in R coding. Preprint published in medRxiv (Sáez et
al. 2020) <doi:10.1101/2020.04.07.20056564>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
