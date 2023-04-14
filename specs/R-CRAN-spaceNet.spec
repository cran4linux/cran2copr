%global __brp_check_rpaths %{nil}
%global packname  spaceNet
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Latent Space Models for Multidimensional Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust >= 5.3
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-RcppTN 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-mclust >= 5.3
Requires:         R-MASS 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-RcppTN 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-vegan 

%description
Latent space models for multivariate networks (multiplex) estimated via
MCMC algorithm. See D Angelo et al. (2018) <arXiv:1803.07166> and D Angelo
et al. (2018) <arXiv:1807.03874>.

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
