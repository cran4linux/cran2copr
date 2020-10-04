%global packname  diverge
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Evolutionary Trait Divergence Between Sister Species and OtherPaired Lineages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-parallel 
Requires:         R-CRAN-truncnorm 

%description
Compares the fit of alternative models of continuous trait differentiation
between sister species and other paired lineages. Differences in trait
means between two lineages arise as they diverge from a common ancestor,
and alternative processes of evolutionary divergence are expected to leave
unique signatures in the distribution of trait differentiation in datasets
comprised of many lineage pairs. Models include approximations of
divergent selection, drift, and stabilizing selection. A variety of model
extensions facilitate the testing of process-to-pattern hypotheses. Users
supply trait data and divergence times for each lineage pair. The fit of
alternative models is compared in a likelihood framework.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/INDEX
