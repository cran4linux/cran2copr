%global packname  LMERConvenienceFunctions
%global packver   2.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.10
Release:          1%{?dist}
Summary:          Model Selection and Post-hoc Analysis for (G)LMER Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-LCFdata 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-mgcv 
BuildRequires:    R-parallel 
Requires:         R-Matrix 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-LCFdata 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-fields 
Requires:         R-mgcv 
Requires:         R-parallel 

%description
The main function of the package is to perform backward selection of fixed
effects, forward fitting of the random effects, and post-hoc analysis
using parallel capabilities. Other functionality includes the computation
of ANOVAs with upper- or lower-bound p-values and R-squared values for
each model term, model criticism plots, data trimming on model residuals,
and data visualization. The data to run examples is contained in package
LCF_data.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
