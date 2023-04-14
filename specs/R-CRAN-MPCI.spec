%global __brp_check_rpaths %{nil}
%global packname  MPCI
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Multivariate Process Capability Indices (MPCI)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
It performs the followings Multivariate Process Capability Indices:
Shahriari et al. (1995) Multivariate Capability Vector, Taam et al. (1993)
Multivariate Capability Index (MCpm), Pan and Lee (2010) proposal (NMCpm)
and the followings based on Principal Component Analysis (PCA):Wang and
Chen (1998), Xekalaki and Perakis (2002) and Wang (2005). Two datasets are
included.

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
