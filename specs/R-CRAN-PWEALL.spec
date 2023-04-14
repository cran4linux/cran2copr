%global __brp_check_rpaths %{nil}
%global packname  PWEALL
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Design and Monitoring of Survival Trials Accounting for ComplexSituations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-survival 
BuildRequires:    R-stats 
Requires:         R-survival 
Requires:         R-stats 

%description
Calculates various functions needed for design and monitoring survival
trials accounting for complex situations such as delayed treatment effect,
treatment crossover, non-uniform accrual, and different censoring
distributions between groups. The event time distribution is assumed to be
piecewise exponential (PWE) distribution and the entry time is assumed to
be piecewise uniform distribution. As compared with Version 1.2.1, two
more types of hybrid crossover are added. A bug is corrected in the
function "pwecx" that calculates the crossover-adjusted survival,
distribution, density, hazard and cumulative hazard functions. Also, to
generate the crossover-adjusted event time random variable, a more
efficient algorithm is used and the output includes crossover indicators.

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
