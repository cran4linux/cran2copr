%global __brp_check_rpaths %{nil}
%global packname  SBMSplitMerge
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Inference for a Generalised SBM with a Split Merge Sampler

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-reshape2 

%description
Inference in a Bayesian framework for a generalised stochastic block
model. The generalised stochastic block model (SBM) can capture group
structure in network data without requiring conjugate priors on the
edge-states. Two sampling methods are provided to perform inference on
edge parameters and block structure: a split-merge Markov chain Monte
Carlo algorithm and a Dirichlet process sampler. Green, Richardson (2001)
<doi:10.1111/1467-9469.00242>; Neal (2000)
<doi:10.1080/10618600.2000.10474879>; Ludkin (2019) <arXiv:1909.09421>.

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
%{rlibdir}/%{packname}
