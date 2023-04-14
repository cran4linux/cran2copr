%global __brp_check_rpaths %{nil}
%global packname  pop
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Flexible Syntax for Population Dynamic Modelling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-MASS 

%description
Population dynamic models underpin a range of analyses and applications in
ecology and epidemiology. The various approaches for analysing population
dynamics models (MPMs, IPMs, ODEs, POMPs, PVA) each require the model to
be defined in a different way. This makes it difficult to combine
different modelling approaches and data types to solve a given problem.
'pop' aims to provide a flexible and easy to use common interface for
constructing population dynamic models and enabling to them to be fitted
and analysed in lots of different ways.

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
