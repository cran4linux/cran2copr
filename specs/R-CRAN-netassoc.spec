%global packname  netassoc
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          3%{?dist}
Summary:          Inference of Species Associations from Co-Occurrence Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-vegan 

%description
Infers species associations from community matrices. Uses local and
(optional) regional-scale co-occurrence data by comparing observed partial
correlation coefficients between species to those estimated from regional
species distributions. Extends Gaussian graphical models to a null
modeling framework. Provides interface to a variety of inverse covariance
matrix estimation methods.

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
