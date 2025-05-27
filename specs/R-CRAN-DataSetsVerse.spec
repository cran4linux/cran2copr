%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DataSetsVerse
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Metapackage for Thematic and Domain-Specific Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-timeSeriesDataSets 
BuildRequires:    R-CRAN-educationR 
BuildRequires:    R-CRAN-crimedatasets 
BuildRequires:    R-CRAN-MedDataSets 
BuildRequires:    R-CRAN-OncoDataSets 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-utils 
Requires:         R-CRAN-timeSeriesDataSets 
Requires:         R-CRAN-educationR 
Requires:         R-CRAN-crimedatasets 
Requires:         R-CRAN-MedDataSets 
Requires:         R-CRAN-OncoDataSets 
Requires:         R-CRAN-cli 
Requires:         R-utils 

%description
A metapackage that brings together a curated collection of R packages
containing domain-specific datasets. It includes time series data,
educational metrics, crime records, medical datasets, and oncology
research data. Designed to provide researchers, analysts, educators, and
data scientists with centralized access to structured and well-documented
datasets, this metapackage facilitates reproducible research, data
exploration, and teaching applications across a wide range of domains.
Included packages: - 'timeSeriesDataSets': Time series data from
economics, finance, energy, and healthcare. - 'educationR': Datasets
related to education, learning outcomes, and school metrics. -
'crimedatasets': Datasets on global and local crime and criminal behavior.
- 'MedDataSets': Datasets related to medicine, public health, treatments,
and clinical trials. - 'OncoDataSets': Datasets focused on cancer
research, survival, genetics, and biomarkers.

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
