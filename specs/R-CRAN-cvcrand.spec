%global packname  cvcrand
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}
Summary:          Efficient Design and Analysis of Cluster Randomized Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tableone 
Requires:         R-CRAN-tableone 

%description
Constrained randomization by Raab and Butcher (2001)
<doi:10.1002/1097-0258(20010215)20:3%3C351::AID-SIM797%3E3.0.CO;2-C> is
suitable for cluster randomized trials (CRTs) with a small number of
clusters (e.g., 20 or fewer). The procedure of constrained randomization
is based on the baseline values of some cluster-level covariates
specified. The intervention effect on the individual outcome can then be
analyzed through clustered permutation test introduced by Gail, et al.
(1996)
<doi:10.1002/(SICI)1097-0258(19960615)15:11%3C1069::AID-SIM220%3E3.0.CO;2-Q>.
Motivated from Li, et al. (2016) <doi:10.1002/sim.7410>, the package
performs constrained randomization on the baseline values of cluster-level
covariates and cluster permutation test on the individual-level outcome
for cluster randomized trials.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/dickinson_constrained.csv
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
