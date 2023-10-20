%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scaper
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Single Cell Transcriptomics-Level Cytokine Activity Prediction and Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-CRAN-SeuratObject 
BuildRequires:    R-CRAN-VAM 
BuildRequires:    R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Seurat 
Requires:         R-CRAN-SeuratObject 
Requires:         R-CRAN-VAM 
Requires:         R-utils 

%description
Generates cell-level cytokine activity estimates using relevant
information from gene sets constructed with the 'CytoSig' and the
'Reactome' databases and scored using the modified 'Variance-adjusted
Mahalanobis (VAM)' framework for single-cell RNA-sequencing (scRNA-seq)
data. 'CytoSig' database is described in: Jiang at al., (2021)
<doi:10.1038/s41592-021-01274-5>. 'Reactome' database is described in:
Gillespie et al., (2021) <doi:10.1093/nar/gkab1028>. The 'VAM' method is
outlined in: Frost (2020) <doi:10.1093/nar/gkaa582>.

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
