%global packname  hmi
%global packver   0.9.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.18
Release:          1%{?dist}
Summary:          Hierarchical Multiple Imputation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.49
BuildRequires:    R-nnet >= 7.3.12
BuildRequires:    R-CRAN-mice >= 3.5.0
BuildRequires:    R-nlme >= 3.1.131.1
BuildRequires:    R-graphics >= 3.0.0
BuildRequires:    R-stats >= 3.0.0
BuildRequires:    R-CRAN-ordinal >= 2015.6.28
BuildRequires:    R-CRAN-MCMCglmm >= 2.25
BuildRequires:    R-CRAN-msm >= 1.6.6
BuildRequires:    R-CRAN-tmvtnorm >= 1.4.10
BuildRequires:    R-boot >= 1.3.20
BuildRequires:    R-Matrix >= 1.2.12
BuildRequires:    R-CRAN-lme4 >= 1.1.15
BuildRequires:    R-CRAN-linLIR >= 1.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.7
BuildRequires:    R-CRAN-pbivnorm >= 0.6.0
BuildRequires:    R-CRAN-rlang >= 0.3.0.1
BuildRequires:    R-CRAN-coda >= 0.19.1
BuildRequires:    R-utils 
Requires:         R-MASS >= 7.3.49
Requires:         R-nnet >= 7.3.12
Requires:         R-CRAN-mice >= 3.5.0
Requires:         R-nlme >= 3.1.131.1
Requires:         R-graphics >= 3.0.0
Requires:         R-stats >= 3.0.0
Requires:         R-CRAN-ordinal >= 2015.6.28
Requires:         R-CRAN-MCMCglmm >= 2.25
Requires:         R-CRAN-msm >= 1.6.6
Requires:         R-CRAN-tmvtnorm >= 1.4.10
Requires:         R-boot >= 1.3.20
Requires:         R-Matrix >= 1.2.12
Requires:         R-CRAN-lme4 >= 1.1.15
Requires:         R-CRAN-linLIR >= 1.1
Requires:         R-CRAN-mvtnorm >= 1.0.7
Requires:         R-CRAN-pbivnorm >= 0.6.0
Requires:         R-CRAN-rlang >= 0.3.0.1
Requires:         R-CRAN-coda >= 0.19.1
Requires:         R-utils 

%description
Runs single level and multilevel imputation models. The user just has to
pass the data to the main function and, optionally, his analysis model.
Basically the package then translates this analysis model into commands to
impute the data according to it with functions from 'mice', 'MCMCglmm' or
routines build for this package.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
