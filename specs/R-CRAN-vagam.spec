%global __brp_check_rpaths %{nil}
%global packname  vagam
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Variational Approximations for Generalized Additive Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-gamm4 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-mgcv 
Requires:         R-CRAN-gamm4 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-truncnorm 

%description
Fits generalized additive models (GAMs) using a variational approximations
(VA) framework. In brief, the VA framework provides a fully or at least
closed to fully tractable lower bound approximation to the marginal
likelihood of a GAM when it is parameterized as a mixed model (using
penalized splines, say). In doing so, the VA framework aims offers both
the stability and natural inference tools available in the mixed model
approach to GAMs, while achieving computation times comparable to that of
using the penalized likelihood approach to GAMs. See Hui et al. (2018)
<doi:10.1080/01621459.2018.1518235>.

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
