%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global packname  dfped
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Extrapolation and Bridging of Adult Information in Early PhaseDose-Finding Paediatrics Studies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan >= 2.8.1
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-stats4 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-rstan >= 2.8.1
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-stats4 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
A unified method for designing and analysing dose-finding trials in
paediatrics, while bridging information from adults, is proposed in the
'dfped' package. The dose range can be calculated under three
extrapolation methods: linear, allometry and maturation adjustment, using
pharmacokinetic (PK) data. To do this, it is assumed that target exposures
are the same in both populations. The working model and prior distribution
parameters of the dose-toxicity and dose-efficacy relationships can be
obtained using early phase adult toxicity and efficacy data at several
dose levels through 'dfped' package. Priors are used into the dose finding
process through a Bayesian model selection or adaptive priors, to
facilitate adjusting the amount of prior information to differences
between adults and children. This calibrates the model to adjust for
misspecification if the adult and paediatric data are very different. User
can use his/her own Bayesian model written in Stan code through the
'dfped' package. A template of this model is proposed in the examples of
the corresponding R functions in the package. Finally, in this package you
can find a simulation function for one trial or for more than one trial.
These methods are proposed by Petit et al, (2016)
<doi:10.1177/0962280216671348>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
