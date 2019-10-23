%global packname  miceMNAR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Missing not at Random Imputation Models for Multiple Imputationby Chained Equation

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-mice >= 3.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-GJRM 
BuildRequires:    R-CRAN-sampleSelection 
Requires:         R-CRAN-mice >= 3.0.0
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-GJRM 
Requires:         R-CRAN-sampleSelection 

%description
Provides imputation models and functions for binary or continuous Missing
Not At Random (MNAR) outcomes through the use of the 'mice' package. The
mice.impute.hecknorm() function provides imputation model for continuous
outcome based on Heckman's model also named sample selection model as
described in Galimard et al (2018) and Galimard et al (2016)
<doi:10.1002/sim.6902>. The mice.impute.heckprob() function provides
imputation model for binary outcome based on bivariate probit model as
described in Galimard et al (2018).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
