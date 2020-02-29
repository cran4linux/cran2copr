%global packname  dynwrap
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Representing and Inferring Single-Cell Trajectories

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dynutils >= 1.0.3
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-babelwhale 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dynparam 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-hdf5r 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-dynutils >= 1.0.3
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-babelwhale 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dynparam 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-hdf5r 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-crayon 

%description
Provides functionality to infer trajectories from single-cell data,
represent them into a common format, and adapt them. Other biological
information can also be added, such as cellular grouping, RNA velocity and
annotation. Saelens et al. (2019) <doi:10.1038/s41587-019-0071-9>.

%prep
%setup -q -c -n %{packname}
find %{packname} -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \;
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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
