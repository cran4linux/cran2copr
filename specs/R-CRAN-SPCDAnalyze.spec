%global packname  SPCDAnalyze
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Design and Analyze Studies using the Sequential ParallelComparison Design

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-plyr 
Requires:         R-nlme 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-plyr 

%description
Programs to find the sample size or power of studies using the Sequential
Parallel Comparison Design (SPCD) and programs to analyze such studies.
This is a clinical trial design where patients initially on placebo who
did not respond are re-randomized between placebo and active drug in a
second phase and the results of the two phases are pooled. The method of
analyzing binary data with this design is described in Fava,Evins, Dorer
and Schoenfeld(2003) <doi:10.1159/000069738>, and the method of analyzing
continuous data is described in Chen, Yang, Hung and Wang (2011)
<doi:10.1016/j.cct.2011.04.006>.

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
