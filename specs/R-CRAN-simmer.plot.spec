%global packname  simmer.plot
%global packver   0.1.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.16
Release:          3%{?dist}
Summary:          Plotting Methods for 'simmer'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-simmer >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-tidyr >= 0.7.0
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
Requires:         R-CRAN-simmer >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-tidyr >= 0.7.0
Requires:         R-CRAN-scales 
Requires:         R-utils 

%description
A set of plotting methods for 'simmer' trajectories and simulations.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
