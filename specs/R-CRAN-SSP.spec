%global packname  SSP
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Simulated Sampling Procedure for Community Ecology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-vegan 
Requires:         R-stats 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-ggplot2 

%description
Simulation-based sampling protocol (SSP) is an R package design to
estimate sampling effort in studies of ecological communities based on the
definition of pseudo-multivariate standard error (MultSE) (Anderson &
Santana-Garcon, 2015) <doi:10.1111/ele.12385> and simulation of ecological
data. The theoretical background is described in Guerra-Castro et al.
(2020) <doi:10.1101/2020.03.19.996991>.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
