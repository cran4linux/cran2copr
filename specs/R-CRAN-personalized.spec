%global packname  personalized
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          2%{?dist}
Summary:          Estimation and Validation Methods for Subgroup Identificationand Personalized Medicine

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 2.0.13
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-survival 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-glmnet >= 2.0.13
Requires:         R-mgcv 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-survival 
Requires:         R-methods 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-foreach 

%description
Provides functions for fitting and validation of models for subgroup
identification and personalized medicine / precision medicine under the
general subgroup identification framework of Chen et al. (2017)
<doi:10.1111/biom.12676>. This package is intended for use for both
randomized controlled trials and observational studies.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
