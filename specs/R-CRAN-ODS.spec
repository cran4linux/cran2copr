%global packname  ODS
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Methods for Outcome-Dependent Sampling Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-survival >= 2.42.3
BuildRequires:    R-CRAN-cubature >= 1.4.1
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-survival >= 2.42.3
Requires:         R-CRAN-cubature >= 1.4.1
Requires:         R-utils 
Requires:         R-stats 

%description
Outcome-dependent sampling (ODS) schemes are cost-effective ways to
enhance study efficiency. In ODS designs, one observes the
exposure/covariates with a probability that depends on the outcome
variable. Popular ODS designs include case-control for binary outcome,
case-cohort for time-to-event outcome, and continuous outcome ODS design
(Zhou et al. 2002) <doi: 10.1111/j.0006-341X.2002.00413.x>. Because ODS
data has biased sampling nature, standard statistical analysis such as
linear regression will lead to biases estimates of the population
parameters. This package implements four statistical methods related to
ODS designs: (1) An empirical likelihood method analyzing the primary
continuous outcome with respect to exposure variables in continuous ODS
design (Zhou et al., 2002). (2) A partial linear model analyzing the
primary outcome in continuous ODS design (Zhou, Qin and Longnecker, 2011)
<doi: 10.1111/j.1541-0420.2010.01500.x>. (3) Analyze a secondary outcome
in continuous ODS design (Pan et al. 2018) <doi: 10.1002/sim.7672>. (4) An
estimated likelihood method analyzing a secondary outcome in case-cohort
data (Pan et al. 2017) <doi: 10.1111/biom.12838>.

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
%{rlibdir}/%{packname}/INDEX
