%global packname  survxai
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Visualization of the Local and Global Survival ModelExplanations

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-breakDown 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-survminer 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-breakDown 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-scales 
Requires:         R-survival 
Requires:         R-CRAN-survminer 

%description
Survival models may have very different structures. This package contains
functions for creating a unified representation of a survival models,
which can be further processed by various survival explainers. Tools
implemented in 'survxai' help to understand how input variables are used
in the model and what impact do they have on the final model prediction.
Currently, four explanation methods are implemented. We can divide them
into two groups: local and global.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
