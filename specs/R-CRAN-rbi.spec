%global __brp_check_rpaths %{nil}
%global packname  rbi
%global packver   0.10.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.3
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to 'LibBi'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-reshape2 

%description
Provides a complete interface to 'LibBi', a library for Bayesian inference
(see <http://libbi.org> and <doi:10.18637/jss.v067.i10> for more
information). This includes functions for manipulating 'LibBi' models, for
reading and writing 'LibBi' input/output files, for converting 'LibBi'
output to provide traces for use with the coda package, and for running
'LibBi' to conduct inference.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/example_dataset.nc
%doc %{rlibdir}/%{packname}/example_output.nc
%doc %{rlibdir}/%{packname}/PZ.bi
%doc %{rlibdir}/%{packname}/SIR.bi
%{rlibdir}/%{packname}/INDEX
