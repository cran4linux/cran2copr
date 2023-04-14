%global __brp_check_rpaths %{nil}
%global packname  PoiClaClu
%global packver   1.0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Classification and Clustering of Sequencing Data Based on aPoisson Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Implements the methods described in the paper, Witten (2011)
Classification and Clustering of Sequencing Data using a Poisson Model,
Annals of Applied Statistics 5(4) 2493-2518.

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
