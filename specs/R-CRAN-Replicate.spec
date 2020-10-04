%global packname  Replicate
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Metrics for Multisite Replication Studies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-metafor 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 

%description
For a multisite replication project, computes the consistency metric
P_orig, which is the probability that the original study would observe an
estimated effect size as extreme or more extreme than it actually did, if
in fact the original study were statistically consistent with the
replications. Other recommended metrics are: (1) the probability of a true
effect of scientifically meaningful size in the same direction as the
estimate the original study; and (2) the probability of a true effect of
meaningful size in the direction opposite the original study's estimate.
These two can be computed using the package
code{MetaUtility::prop_stronger}. Additionally computes older metrics
used in replication projects (namely expected agreement in "statistical
significance" between an original study and replication studies as well as
prediction intervals for the replication estimates). See Mathur and
VanderWeele (under review; <https://osf.io/apnjk/>) for details.

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
