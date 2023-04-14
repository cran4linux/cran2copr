%global __brp_check_rpaths %{nil}
%global packname  optimus
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Model Based Diagnostics for Multivariate Cluster Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvabund >= 3.1
BuildRequires:    R-CRAN-ordinal >= 2015.1.21
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-mvabund >= 3.1
Requires:         R-CRAN-ordinal >= 2015.1.21
Requires:         R-stats 
Requires:         R-methods 

%description
Assessment and diagnostics for comparing competing clustering solutions,
using predictive models. The main intended use is for comparing
clustering/classification solutions of ecological data (e.g.
presence/absence, counts, ordinal scores) to 1) find an optimal
partitioning solution, 2) identify characteristic species and 3) refine a
classification by merging clusters that increase predictive performance.
However, in a more general sense, this package can do the above for any
set of clustering solutions for i observations of j variables.

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
