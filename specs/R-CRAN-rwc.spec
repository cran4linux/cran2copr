%global __brp_check_rpaths %{nil}
%global packname  rwc
%global packver   1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11
Release:          3%{?dist}%{?buildtag}
Summary:          Random Walk Covariance Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-MASS 
Requires:         R-CRAN-raster 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-MASS 

%description
Code to facilitate simulation and inference when connectivity is defined
by underlying random walks. Methods for spatially-correlated pairwise
distance data are especially considered. This provides core code to
conduct analyses similar to that in Hanks and Hooten (2013)
<doi:10.1080/01621459.2012.724647>.

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
