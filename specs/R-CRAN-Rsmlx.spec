%global packname  Rsmlx
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}
Summary:          R Speaks 'Monolix'

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-tools 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-tcltk 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-tools 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-tcltk 
Requires:         R-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Provides methods for model building and model evaluation of mixed effects
models using 'Monolix' <http://monolix.lixoft.com>. 'Monolix' is a
software tool for nonlinear mixed effects modeling that must have been
installed in order to use 'Rsmlx'. Among other tasks, 'Rsmlx' provides a
powerful tool for automatic PK model building, performs statistical tests
for model assessment, bootstrap simulation and likelihood profiling for
computing confidence intervals. 'Rsmlx' also proposes several automatic
covariate search methods for mixed effects models.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
