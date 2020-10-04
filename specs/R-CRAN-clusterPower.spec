%global packname  clusterPower
%global packver   0.6.111
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.111
Release:          3%{?dist}%{?buildtag}
Summary:          Power Calculations for Cluster-Randomized and Cluster-RandomizedCrossover Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.0
Requires:         R-CRAN-lme4 >= 1.0

%description
Calculate power for cluster randomized trials (CRTs) that compare two
means, two proportions, or two counts using closed-form solutions. In
addition, calculate power for cluster randomized crossover trials using
Monte Carlo methods. For more information, see Reich et al. (2012)
<doi:10.1371/journal.pone.0035564>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
