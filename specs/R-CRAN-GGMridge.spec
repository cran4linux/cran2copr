%global __brp_check_rpaths %{nil}
%global packname  GGMridge
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Gaussian Graphical Models Using Ridge Penalty Followed byThresholding and Reestimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 

%description
Estimation of partial correlation matrix using ridge penalty followed by
thresholding and reestimation. Under multivariate Gaussian assumption, the
matrix constitutes an Gaussian graphical model (GGM).

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
