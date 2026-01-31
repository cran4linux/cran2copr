%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glioblastomaEHRsData
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Descriptive Analysis on Three Glioblastoma EHRs Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-DataExplorer 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-summarytools 
BuildRequires:    R-CRAN-table1 
BuildRequires:    R-CRAN-tinytex 
Requires:         R-CRAN-DataExplorer 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-summarytools 
Requires:         R-CRAN-table1 
Requires:         R-CRAN-tinytex 

%description
Provides functions to load and analyze three open Electronic Health
Records (EHRs) datasets of patients diagnosed with glioblastoma,
previously released under the Creative Common Attribution 4.0
International (CC BY 4.0) license.  Users can generate basic descriptive
statistics, frequency tables and save descriptive summary tables, as well
as create and export univariate or bivariate plots.  The package is
designed to work with the included datasets and to facilitate quick
exploratory data analysis and reporting.  More information about these
three datasets of EHRs of patients with glioblastoma can be found in this
article: Gabriel Cerono, Ombretta Melaiu, and Davide Chicco, 'Clinical
feature ranking based on ensemble machine learning reveals top survival
factors for glioblastoma multiforme', Journal of Healthcare Informatics
Research 8, 1-18 (March 2024).  <doi:10.1007/s41666-023-00138-1>.

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
