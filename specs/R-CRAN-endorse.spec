%global __brp_check_rpaths %{nil}
%global packname  endorse
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Measurement Models for Analyzing EndorsementExperiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-utils 
Requires:         R-CRAN-coda 
Requires:         R-utils 

%description
Fit the hierarchical and non-hierarchical Bayesian measurement models
proposed by Bullock, Imai, and Shapiro (2011) <DOI:10.1093/pan/mpr031> to
analyze endorsement experiments.  Endorsement experiments are a survey
methodology for eliciting truthful responses to sensitive questions.  This
methodology is helpful when measuring support for socially sensitive
political actors such as militant groups.  The model is fitted with a
Markov chain Monte Carlo algorithm and produces the output containing
draws from the posterior distribution.

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
%{rlibdir}/%{packname}/libs
