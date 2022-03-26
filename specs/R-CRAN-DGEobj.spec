%global __brp_check_rpaths %{nil}
%global packname  DGEobj
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Differential Gene Expression (DGE) Analysis Results Data Object

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Provides a flexible container to manage and annotate Differential Gene
Expression (DGE) analysis results (Smythe et. al (2015)
<doi:10.1093/nar/gkv007>). The DGEobj has data slots for row (gene), col
(samples), assays (matrix n-rows by m-samples dimensions) and metadata
(not keyed to row, col, or assays). A set of accessory functions to
deposit, query and retrieve subsets of a data workflow has been provided.
Attributes are used to capture metadata such as species and gene model,
including reproducibility information such that a 3rd party can access a
DGEobj history to see how each data object was created or modified.  Since
the DGEobj is customizable and extensible it is not limited to RNA-seq
analysis types of workflows -- it can accommodate nearly any data analysis
workflow that starts from a matrix of assays (rows) by samples (columns).

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
