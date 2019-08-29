%global packname  CIEE
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Estimating and Testing Direct Effects in Directed Acyclic Graphsusing Estimating Equations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-survival 
Requires:         R-stats 
Requires:         R-survival 

%description
In many studies across different disciplines, detailed measures of the
variables of interest are available. If assumptions can be made regarding
the direction of effects between the assessed variables, this has to be
considered in the analysis. The functions in this package implement the
novel approach CIEE (causal inference using estimating equations;
Konigorski et al., 2018, <DOI:10.1002/gepi.22107>) for estimating and
testing the direct effect of an exposure variable on a primary outcome,
while adjusting for indirect effects of the exposure on the primary
outcome through a secondary intermediate outcome and potential factors
influencing the secondary outcome. The underlying directed acyclic graph
(DAG) of this considered model is described in the vignette. CIEE can be
applied to studies in many different fields, and it is implemented here
for the analysis of a continuous primary outcome and a time-to-event
primary outcome subject to censoring. CIEE uses estimating equations to
obtain estimates of the direct effect and robust sandwich standard error
estimates. Then, a large-sample Wald-type test statistic is computed for
testing the absence of the direct effect. Additionally, standard multiple
regression, regression of residuals, and the structural equation modeling
approach are implemented for comparison.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
