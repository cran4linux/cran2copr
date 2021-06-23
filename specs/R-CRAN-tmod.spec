%global __brp_check_rpaths %{nil}
%global packname  tmod
%global packver   0.46.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.46.2
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Set Enrichment Analysis for Metabolomics and Transcriptomics

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-beeswarm 
BuildRequires:    R-CRAN-tagcloud 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotwidgets 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-colorDF 
Requires:         R-CRAN-beeswarm 
Requires:         R-CRAN-tagcloud 
Requires:         R-CRAN-XML 
Requires:         R-methods 
Requires:         R-CRAN-plotwidgets 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-colorDF 

%description
Methods and feature set definitions for feature or gene set enrichment
analysis in transcriptional and metabolic profiling data. Package includes
tests for enrichment based on ranked lists of features, functions for
visualisation and multivariate functional analysis.

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
