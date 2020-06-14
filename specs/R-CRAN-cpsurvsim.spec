%global packname  cpsurvsim
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Simulating Survival Data from Change-Point Hazard Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.3.0
BuildRequires:    R-CRAN-plyr >= 1.8.5
BuildRequires:    R-CRAN-knitr >= 1.27
BuildRequires:    R-stats 
Requires:         R-CRAN-Hmisc >= 4.3.0
Requires:         R-CRAN-plyr >= 1.8.5
Requires:         R-CRAN-knitr >= 1.27
Requires:         R-stats 

%description
Simulates time-to-event data with type I right censoring using two
methods: the inverse CDF method and our proposed memoryless method. The
latter method takes advantage of the memoryless property of survival and
simulates a separate distribution between change-points. We include two
parametric distributions: exponential and Weibull. Inverse CDF method
draws on the work of Rainer Walke (2010),
<https://www.demogr.mpg.de/papers/technicalreports/tr-2010-003.pdf>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
