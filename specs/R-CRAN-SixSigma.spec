%global __brp_check_rpaths %{nil}
%global packname  SixSigma
%global packver   0.9-52
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.52
Release:          3%{?dist}%{?buildtag}
Summary:          Six Sigma Tools for Quality Control and Improvement

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-qcc 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-xtable 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-qcc 
Requires:         R-lattice 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-xtable 

%description
Functions and utilities to perform Statistical Analyses in the Six Sigma
way. Through the DMAIC cycle (Define, Measure, Analyze, Improve, Control),
you can manage several Quality Management studies: Gage R&R, Capability
Analysis, Control Charts, Loss Function Analysis, etc. Data frames used in
the books "Six Sigma with R", Cano et al. (2012) [ISBN 978-1-4614-3652-2]
and "Quality Control with R", Cano et al. (2015) [ISBN 978-3-319-24046-6],
are also included in the package.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
