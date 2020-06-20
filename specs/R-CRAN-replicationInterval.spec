%global packname  replicationInterval
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Replication Interval Functions

License:          MIT License + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MBESS 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-pbapply 

%description
A common problem faced by journal reviewers and authors is the question of
whether the results of a replication study are consistent with the
original published study. One solution to this problem is to examine the
effect size from the original study and generate the range of effect sizes
that could reasonably be obtained (due to random sampling) in a
replication attempt (i.e., calculate a replication interval). If a
replication effect size falls outside the replication interval, then that
effect likely did not occur due to the effects of sampling error alone.
Alternatively, if a replication effect size falls within the replication
interval, then the replication effect could have reasonably occurred due
to the effects of sampling error alone. This package has functions that
calculate the replication interval for the correlation (i.e., r),
standardized mean difference (i.e., d-value), and mean. The calculations
used in version 2.0.0 and onward differ from past calculations due to
feedback during the journal review process. The new calculations allow for
a more precise interpretation of the replication interval.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
