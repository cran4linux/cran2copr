%global __brp_check_rpaths %{nil}
%global packname  OWEA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Optimal Weight Exchange Algorithm for Optimal Designs for ThreeModels

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.8.1
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-MASS 
Requires:         R-CRAN-gtools >= 3.8.1
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-MASS 

%description
An implementation of optimal weight exchange algorithm Yang(2013)
<doi:10.1080/01621459.2013.806268> for three models. They are Crossover
model with subject dropout, crossover model with proportional first order
residual effects and interference model. You can use it to find either
A-opt or D-opt approximate designs. Exact designs can be automatically
rounded from approximate designs and relative efficiency is provided as
well.

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
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/test
%{rlibdir}/%{packname}/INDEX
