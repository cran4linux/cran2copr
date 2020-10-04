%global packname  baycn
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference for Causal Networks

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-egg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-egg 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-igraph 
Requires:         R-MASS 
Requires:         R-methods 

%description
A Bayesian hybrid approach for inferring Directed Acyclic Graphs (DAGs)
for continuous, discrete, and mixed data. The algorithm can use the graph
inferred by another more efficient graph inference method as input; the
input graph may contain false edges or undirected edges but can help
reduce the search space to a more manageable size. A Bayesian Markov chain
Monte Carlo algorithm is then used to infer the probability of direction
and absence for the edges in the network. References: Martin and Fu (2019)
<arXiv:1909.10678>.

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
