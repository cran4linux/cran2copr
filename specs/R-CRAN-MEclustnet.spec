%global __brp_check_rpaths %{nil}
%global packname  MEclustnet
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Fit the Mixture of Experts Latent Position Cluster Model toNetwork Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-latentnet 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-e1071 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-nnet 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-latentnet 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-e1071 

%description
Functions to facilitate model-based clustering of nodes in a network in a
mixture of experts setting, which incorporates covariate information on
the nodes in the modelling process. Isobel Claire Gormley and Thomas
Brendan Murphy (2010) <doi:10.1016/j.stamet.2010.01.002>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
