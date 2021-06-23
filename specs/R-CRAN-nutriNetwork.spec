%global __brp_check_rpaths %{nil}
%global packname  nutriNetwork
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Structure Learning with Copula Graphical Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-tmvtnorm 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-tmvtnorm 

%description
Statistical tool for learning the structure of direct associations among
variables for continuous data, discrete data and mixed discrete-continuous
data. The package is based on the copula graphical model in Behrouzi and
Wit (2017) <doi:10.1111/rssc.12287>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
