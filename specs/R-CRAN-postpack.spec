%global packname  postpack
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Processing Posterior Samples Stored in 'mcmc.lists'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-abind 

%description
The aim of 'postpack' is to provide the infrastructure for a standardized
workflow for 'mcmc.list' objects. These objects can be used to store
output from models fitted with Bayesian inference using 'JAGS', 'WinBUGS',
'OpenBUGS', 'NIMBLE', 'Stan', or even custom MCMC algorithms. Although the
'coda' R package provides some methods for these objects, it is somewhat
limited in easily performing post-processing tasks for specific nodes.
Models are ever increasing in their complexity and the number of tracked
nodes, and oftentimes a user may wish to summarize/diagnose sampling
behavior for only a small subset of nodes at a time for a particular
question or figure. Thus, many 'postpack' functions support performing
tasks on a subset of nodes, where the subset is specified with regular
expressions. The functions in 'postpack' streamline the extraction,
summarization, and diagnostics of specific monitored nodes after model
fitting. Further, because there is rarely only ever one model under
consideration, 'postpack' scales efficiently to perform the same tasks on
output from multiple models simultaneously, facilitating rapid assessment
of model sensitivity to changes in assumptions.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
