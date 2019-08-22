%global packname  casebase
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Fitting Flexible Smooth-in-Time Hazards and Risk Functions viaLogistic and Multinomial Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-survival 
Requires:         R-CRAN-VGAM 

%description
Implements the case-base sampling approach of Hanley and Miettinen (2009)
<DOI:10.2202/1557-4679.1125>, Saarela and Arjas (2015)
<DOI:10.1111/sjos.12125>, and Saarela (2015)
<DOI:10.1007/s10985-015-9352-x>, for fitting flexible hazard regression
models to survival data with single event type or multiple competing
causes via logistic and multinomial regression. From the fitted hazard
function, cumulative incidence, risk functions of time, treatment and
profile can be derived. This approach accommodates any log-linear hazard
function of prognostic time, treatment, and covariates, and readily allows
for non-proportionality. We also provide a plot method for visualizing
incidence density via population time plots.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
