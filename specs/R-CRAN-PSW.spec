%global __brp_check_rpaths %{nil}
%global packname  PSW
%global packver   1.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Propensity Score Weighting Methods for Dichotomous Treatments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-gtools 
Requires:         R-graphics 

%description
Provides propensity score weighting methods to control for confounding in
causal inference with dichotomous treatments and continuous/binary
outcomes. It includes the following functional modules: (1) visualization
of the propensity score distribution in both treatment groups with mirror
histogram, (2) covariate balance diagnosis, (3) propensity score model
specification test, (4) weighted estimation of treatment effect, and (5)
augmented estimation of treatment effect with outcome regression. The
weighting methods include the inverse probability weight (IPW) for
estimating the average treatment effect (ATE), the IPW for average
treatment effect of the treated (ATT), the IPW for the average treatment
effect of the controls (ATC), the matching weight (MW), the overlap weight
(OVERLAP), and the trapezoidal weight (TRAPEZOIDAL). Sandwich variance
estimation is provided to adjust for the sampling variability of the
estimated propensity score. These methods are discussed by Hirano et al
(2003) <DOI:10.1111/1468-0262.00442>, Lunceford and Davidian (2004)
<DOI:10.1002/sim.1903>, Li and Greene (2013) <DOI:10.1515/ijb-2012-0030>,
and Li et al (2016) <DOI:10.1080/01621459.2016.1260466>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
