%global packname  jomo
%global packver   2.6-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.9
Release:          1%{?dist}
Summary:          Multilevel Joint Modelling Multiple Imputation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-survival 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ordinal 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-survival 
Requires:         R-MASS 
Requires:         R-CRAN-ordinal 

%description
Similarly to Schafer's package 'pan', 'jomo' is a package for multilevel
joint modelling multiple imputation (Carpenter and Kenward, 2013) <doi:
10.1002/9781119942283>. Novel aspects of 'jomo' are the possibility of
handling binary and categorical data through latent normal variables, the
option to use cluster-specific covariance matrices and to impute
compatibly with the substantive model.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
