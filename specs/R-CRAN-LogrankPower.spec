%global packname  LogrankPower
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Log-Rank Test Power Calculation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-survminer 
Requires:         R-survival 
Requires:         R-CRAN-survminer 

%description
Power of the log-rank test is estimated using simulation datasets, with
user specified total sample size (in one simulation dataset), type I
error, effect size, the total number of simulation datasets, sample size
ratio between two comparison groups, the death rate in the reference
group, and the distribution of follow-up time (simulated from a negative
binomial distribution). Method reference: Hogg, R. V., McKean, J., and
Craig, A. T. (2004, ISBN 10: 0130085073).
<https://github.com/RongUTSW/Methods/blob/master/LRPowerSimulation.pdf>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
