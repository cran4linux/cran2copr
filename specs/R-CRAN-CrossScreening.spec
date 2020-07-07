%global packname  CrossScreening
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Cross-Screening in Observational Studies that Test ManyHypotheses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tables 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tables 

%description
Cross-screening is a new method that uses both random halves of the sample
to screen and test many hypotheses. It generally improves statistical
power in observational studies when many hypotheses are tested
simultaneously. References: 1. Qingyuan Zhao, Dylan S Small, and Paul R
Rosenbaum. Cross-screening in observational studies that test many
hypotheses. <arXiv:1703.02078>. 2. Qingyuan Zhao. On sensitivity value of
pair-matched observational studies. <arXiv:1702.03442>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
