%global __brp_check_rpaths %{nil}
%global packname  mediationsens
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          2%{?dist}%{?buildtag}
Summary:          Simulation-Based Sensitivity Analysis for Causal MediationStudies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mediation 
BuildRequires:    R-CRAN-distr 
Requires:         R-CRAN-mediation 
Requires:         R-CRAN-distr 

%description
Simulation-based sensitivity analysis for causal mediation studies. It
numerically and graphically evaluates the sensitivity of causal mediation
analysis results to the presence of unmeasured pretreatment confounding.
The proposed method has primary advantages over existing methods. First,
using an unmeasured pretreatment confounder conditional associations with
the treatment, mediator, and outcome as sensitivity parameters, the method
enables users to intuitively assess sensitivity in reference to prior
knowledge about the strength of a potential unmeasured pretreatment
confounder. Second, the method accurately reflects the influence of
unmeasured pretreatment confounding on the efficiency of estimation of the
causal effects. Third, the method can be implemented in different causal
mediation analysis approaches, including regression-based,
simulation-based, and propensity score-based methods. It is applicable to
both randomized experiments and observational studies.

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
%{rlibdir}/%{packname}
