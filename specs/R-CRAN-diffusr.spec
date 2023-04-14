%global __brp_check_rpaths %{nil}
%global packname  diffusr
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Network Diffusion Algorithms

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-igraph 
Requires:         R-methods 

%description
Implementation of network diffusion algorithms such as heat diffusion or
Markov random walks. Network diffusion algorithms generally spread
information in the form of node weights along the edges of a graph to
other nodes. These weights can for example be interpreted as temperature,
an initial amount of water, the activation of neurons in the brain, or the
location of a random surfer in the internet. The information (node
weights) is iteratively propagated to other nodes until a equilibrium
state or stop criterion occurs.

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
