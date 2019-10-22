%global packname  Surrogate
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Evaluation of Surrogate Endpoints in Clinical Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-survival 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-OrdinalLogisticBiplot 
BuildRequires:    R-CRAN-logistf 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-extraDistr 
Requires:         R-MASS 
Requires:         R-CRAN-rgl 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-survival 
Requires:         R-nlme 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-OrdinalLogisticBiplot 
Requires:         R-CRAN-logistf 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-mixtools 
Requires:         R-parallel 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-extraDistr 

%description
In a clinical trial, it frequently occurs that the most credible outcome
to evaluate the effectiveness of a new therapy (the true endpoint) is
difficult to measure. In such a situation, it can be an effective strategy
to replace the true endpoint by a (bio)marker that is easier to measure
and that allows for a prediction of the treatment effect on the true
endpoint (a surrogate endpoint). The package 'Surrogate' allows for an
evaluation of the appropriateness of a candidate surrogate endpoint based
on the meta-analytic, information-theoretic, and causal-inference
frameworks. Part of this software has been developed using funding
provided from the European Union's Seventh Framework Programme for
research, technological development and demonstration under Grant
Agreement no 602552.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
