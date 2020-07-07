%global packname  tricolore
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}
Summary:          A Flexible Color Scale for Ternary Compositions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-ggtern >= 3.3.0
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-ggtern >= 3.3.0
Requires:         R-grDevices 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-assertthat 

%description
A flexible color scale for ternary compositions with options for
discretization, centering and scaling.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/figures
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
