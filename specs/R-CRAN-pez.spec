%global packname  pez
%global packver   1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetics for the Environmental Sciences

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.05
BuildRequires:    R-CRAN-ape >= 3.1
BuildRequires:    R-methods >= 3.1.0
BuildRequires:    R-CRAN-animation >= 2.4
BuildRequires:    R-CRAN-vegan >= 2.0.10
BuildRequires:    R-CRAN-picante >= 1.6.2
BuildRequires:    R-CRAN-ade4 >= 1.6.2
BuildRequires:    R-CRAN-apTreeshape >= 1.4.5
BuildRequires:    R-Matrix >= 1.1.4
BuildRequires:    R-CRAN-FD >= 1.0.12
BuildRequires:    R-CRAN-mvtnorm >= 1.0.0
BuildRequires:    R-CRAN-phytools >= 0.6.60
BuildRequires:    R-CRAN-caper >= 0.5.2
Requires:         R-CRAN-quantreg >= 5.05
Requires:         R-CRAN-ape >= 3.1
Requires:         R-methods >= 3.1.0
Requires:         R-CRAN-animation >= 2.4
Requires:         R-CRAN-vegan >= 2.0.10
Requires:         R-CRAN-picante >= 1.6.2
Requires:         R-CRAN-ade4 >= 1.6.2
Requires:         R-CRAN-apTreeshape >= 1.4.5
Requires:         R-Matrix >= 1.1.4
Requires:         R-CRAN-FD >= 1.0.12
Requires:         R-CRAN-mvtnorm >= 1.0.0
Requires:         R-CRAN-phytools >= 0.6.60
Requires:         R-CRAN-caper >= 0.5.2

%description
Eco-phylogenetic and community phylogenetic analyses. Keeps community
ecological and phylogenetic data matched up and comparable using
'comparative.comm' objects. Wrappers for common community phylogenetic
indices ('pez.shape', 'pez.evenness', 'pez.dispersion', and
'pez.dissimilarity' metrics). Implementation of Cavender-Bares (2004)
correlation of phylogenetic and ecological matrices
('fingerprint.regression'). Phylogenetic Generalised Linear Mixed Models
(PGLMMs; 'pglmm') following Ives & Helmus (2011) and Rafferty & Ives
(2013). Simulation of null assemblages, traits, and phylogenies ('scape',
'sim.meta.comm').

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
