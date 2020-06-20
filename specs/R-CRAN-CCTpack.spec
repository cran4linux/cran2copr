%global packname  CCTpack
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          1%{?dist}
Summary:          Consensus Analysis, Model-Based Clustering, and CulturalConsensus Theory Applications

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R2jags >= 0.04.03
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-R2jags >= 0.04.03
Requires:         R-tcltk 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-polycor 
Requires:         R-MASS 
Requires:         R-methods 

%description
Consensus analysis, model-based clustering, and cultural consensus theory
applications to response data (e.g. questionnaires). The models are
applied using hierarchical Bayesian inference. The current package version
supports binary, ordinal, and continuous data formats.

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
